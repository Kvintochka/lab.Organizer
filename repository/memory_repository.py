from datetime import datetime

from repository.model import Event
from repository.repository import EventRepository


class InMemoryEventRepository(EventRepository):

    def __init__(self):
        self._data_source = []

    def get_all(self) -> list[Event]:
        return self._data_source

    def get_by_id(self, id: int) -> Event:
        return next((event for event in self._data_source if event.id == id), None)

    def get_by_in_datetime_range(self, start: datetime, end: datetime) -> list[Event]:
        return [event for event in self._data_source if start <= event.start_datetime <= end]

    def get_by_datetime_intercept(self, start: datetime, end: datetime) -> list[Event]:
        return [event for event in self._data_source if
                (start <= event.start_datetime <= end) or
                (start <= event.end_datetime <= end) or
                (event.start_datetime <= start and event.end_datetime >= end)]

    def get_by_datetime_range_and_name(self, start: datetime, end: datetime, name: str) -> list[Event]:
        return [event for event in self._data_source if
                start <= event.start_datetime <= end and event.name.lower() == name.lower()]

    def add(self, item: Event):
        self._data_source.append(item)

    def update(self, item: Event):
        for index, event in enumerate(self._data_source):
            if event.id == item.id:
                self._data_source[index] = item
                return
        raise ValueError(f"Event with id {item.id} not found.")

    def delete(self, id: int):
        self._data_source = [event for event in self._data_source if event.id != id]
