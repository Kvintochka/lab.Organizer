from abc import ABC, abstractmethod
from datetime import date

from repository.model import Event


class EventWriter(ABC):

    @abstractmethod
    def write(self, event: Event):
        raise NotImplementedError

    def write_all(self, events: list[Event]):
        [self.write(event) for event in events]

    @abstractmethod
    def write_calendar_in_range(self, events: list[Event], start: date, end: date):
        raise NotImplementedError
