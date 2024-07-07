from abc import ABC, abstractmethod

from repository.model import Event


class EventRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Event]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id) -> Event:
        raise NotImplementedError

    @abstractmethod
    def get_by_in_datetime_range(self, start, end) -> list[Event]:
        raise NotImplementedError

    @abstractmethod
    def get_by_datetime_intercept(self, start, end) -> list[Event]:
        raise NotImplementedError

    @abstractmethod
    def get_by_datetime_range_and_name(self, start, end, name) -> list[Event]:
        raise NotImplementedError

    @abstractmethod
    def add(self, item):
        raise NotImplementedError

    @abstractmethod
    def update(self, item):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError
