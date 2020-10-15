from datetime import datetime

SPLITTER = '::'


def clean_text(text: str):
    return ''.join([char for char in text if char.isalnum() or char == ' '])


def join_key(*args):
    return SPLITTER.join(args)


def split_key(key: str):
    return key.split(SPLITTER)


def date_to_text(date: datetime) -> str:
    return date.strftime("%d-%m-%Y")


def text_to_date(date: str) -> datetime:
    return datetime.strptime(date, "%d-%m-%Y")
