from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
def get_current_datetime(
    timezone: str = "UTC"
) -> dict:

    try:
        tz = ZoneInfo(timezone)

    except (ZoneInfoNotFoundError, ValueError):
        raise ValueError(
            f"Invalid timezone: {timezone}"
        )

    now = datetime.now(tz)

    return {
        "timezone": timezone,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "weekday": now.strftime("%A"),
        "utc_offset": now.strftime("%z"),
        "iso_datetime": now.isoformat()
    }