from abc import ABC, abstractmethod
from datetime import date, time


class DateTimeConverter(ABC):
    @abstractmethod
    def is_valid_date(self, date_str: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_valid_time(self, time_str: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def convert_to_date(self, date_str: str) -> date:
        raise NotImplementedError

    @abstractmethod
    def convert_to_time(self, time_str: str) -> time:
        raise NotImplementedError

    def try_convert_to_date(self, date_str: str) -> date:
        return self.convert_to_date(date_str) if self.is_valid_date(date_str) else None

    def try_convert_to_time(self, time_str: str) -> time:
        return self.convert_to_time(time_str) if self.is_valid_time(time_str) else None
