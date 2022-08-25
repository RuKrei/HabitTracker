from datetime import datetime, timezone


class Utils:
    pass

    def __init__(self):
        pass


def get_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def get_timedelta_days(date1: str, date2: str) -> int:
    return (
        datetime.strptime(date1, "%Y-%m-%d") - datetime.strptime(date2, "%Y-%m-%d")
    ).days
