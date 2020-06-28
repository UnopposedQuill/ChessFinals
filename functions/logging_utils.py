
from datetime import datetime


def get_now_formatted():
    date_format_string = "%H:%M:%S-%d/%m/%Y"
    return datetime.now().strftime(date_format_string)