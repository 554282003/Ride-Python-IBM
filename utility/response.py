from datetime import datetime

def response(success: bool, message: str, data=None, status_code: int = 200):
    """Generate a standard JSON response."""
    return {
        "success": success,
        "message": message,
        "data": data if data is not None else {},
        "status_code": status_code,
        "timestamp": datetime.utcnow().isoformat()
    }

