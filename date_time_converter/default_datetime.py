from datetime import date, time, timedelta

from date_time_converter.date_time_converter import DateTimeConverter


class DefaultDataTimeConverter(DateTimeConverter):
    def is_valid_date(self, date_str: str) -> bool:
        try:
            date.fromisoformat(date_str.replace("/", '-'))
            return True
        except ValueError:
            return False

    def is_valid_time(self, time_str: str) -> bool:
        try:
            time.fromisoformat(time_str)
            return True
        except ValueError:
            return False

    def convert_to_date(self, date_str: str) -> date:
        return date.fromisoformat(date_str.replace("/", '-'))

    def convert_to_time(self, time_str: str) -> time:
        return time.fromisoformat(time_str)
