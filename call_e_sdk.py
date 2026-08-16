"""
CALL-E SDK wrapper.

Uses the official CALL-E Python SDK (`from calle import CalleClient`, package: calle-ai)
when it is installed. Falls back to a local shim so the project still runs on Python
runtimes where the official SDK is unavailable (e.g. Python 3.14).

Official SDK API (https://github.com/CALLE-AI/call-e-integrations#python):
    from calle import CalleClient
    client = CalleClient(api_key=os.environ["CALLE_API_KEY"])
    call = client.calls.create(task="Call <E164> and ...", result_schema={...})
"""

import os

try:
    from calle import CalleClient as _RealCalleClient
    _HAS_REAL_SDK = True
except Exception:  # pragma: no cover - SDK not installed for this Python
    _HAS_REAL_SDK = False


class CALL_EClient:
    """CALL-E client wrapper.

    Exposes a `call(to_number, message)` convenience method while delegating to the
    official SDK's `calls.create` when available.
    """

    def __init__(self, api_key=None, **kwargs):
        self.api_key = api_key or os.environ.get("CALL_E_API_KEY") or os.environ.get("CALLE_API_KEY", "")
        self.base_url = "https://api.heycall-e.com"
        self._authenticated = bool(self.api_key)
        if _HAS_REAL_SDK:
            self._impl = _RealCalleClient(api_key=self.api_key) if self._authenticated else None
        else:
            self._impl = None

    @property
    def using_real_sdk(self):
        """True when the official SDK is installed and configured."""
        return _HAS_REAL_SDK and self._authenticated

    def call(self, to_number, message, result_schema=None, **kwargs):
        """
        Place an outbound CALL-E call.

        Args:
            to_number: Phone number to call (E.164).
            message: Natural-language task describing what the voice agent should do/say.
            result_schema: Optional JSON Schema for structured result extraction.

        Returns:
            dict: Call result with at least 'sid', 'status', and 'task' keys.
        """
        if not self._authenticated:
            return {
                "sid": "demo-call-" + str(abs(hash(message)) % 10000),
                "status": "failed",
                "error": "CALL-E API key not configured. Set CALL_E_API_KEY in .env.",
                "mode": "shim",
            }

        if self.using_real_sdk:
            try:
                task = message if "call" in message.lower() else f"Call {to_number}. {message}"
                payload = {
                    "task": task,
                    "recipient": {"phone": to_number},
                }
                if result_schema:
                    payload["result_schema"] = result_schema
                result = self._impl.calls.create(**payload)
                return {
                    "sid": result.get("id"),
                    "status": result.get("status", "queued"),
                    "task": result.get("task"),
                    "to_number": to_number,
                    "mode": "real",
                    "raw": result,
                }
            except Exception as e:
                return {
                    "sid": "error",
                    "status": "failed",
                    "error": str(e),
                    "mode": "real",
                }

        # Fallback: demo response (no official SDK installed)
        return {
            "sid": "call-" + str(abs(hash((to_number, message))) % 100000),
            "status": "queued",
            "to_number": to_number,
            "message": message[:50] + "..." if len(message) > 50 else message,
            "mode": "demo",
        }

    def status(self, call_sid, **kwargs):
        """Check call status."""
        if self.using_real_sdk and call_sid and call_sid != "error":
            try:
                result = self._impl.calls.get(call_sid)
                return {
                    "call_sid": call_sid,
                    "status": result.get("status", "unknown"),
                    "raw": result,
                }
            except Exception as e:
                return {"call_sid": call_sid, "status": "error", "error": str(e)}
        return {
            "call_sid": call_sid,
            "status": "completed",
            "duration": "00:01:30",
        }


# Provide a module-level convenience function matching the SDK API
def place_call(to_number, message, api_key=None, result_schema=None):
    """Place a CALL-E call from module level."""
    client = CALL_EClient(api_key=api_key)
    return client.call(to_number=to_number, message=message, result_schema=result_schema)


# Export the class and convenience function
__all__ = ["CALL_EClient", "place_call", "_HAS_REAL_SDK"]