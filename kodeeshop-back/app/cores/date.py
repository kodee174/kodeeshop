from datetime import datetime, date


def get_today_date():
    today = datetime.now()
    return date(today.year, today.month, today.day)


def get_today_datetime():
    today = datetime.now()
    return datetime(today.year, today.month, today.day, today.hour, today.minute, today.second)
