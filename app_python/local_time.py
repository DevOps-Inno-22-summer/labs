from datetime import datetime, timezone, timedelta

def get_current_time(tzone: int) -> str:
    tz = timezone(timedelta(hours=tzone))
    date = datetime.now(tz).strftime("%H:%M:%S")
    return date
