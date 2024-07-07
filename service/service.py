from abc import ABC, abstractmethod

from repository.model import Event


class EventService(ABC):
    @abstractmethod
    def create(self, event: Event):
        raise NotImplementedError

    @abstractmethod
    def write_in_datatime_range(self, start, end):
        raise NotImplementedError

    @abstractmethod
    def write_by_datetime_intercept(self, start, end):
        raise NotImplementedError

    @abstractmethod
    def write_calendar(self, start, end):
        raise NotImplementedError
