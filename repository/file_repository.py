import json
from datetime import datetime, timedelta
from typing import List

from repository.model import Event
from repository.repository import EventRepository


class FileSystemEventRepository(EventRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._data_source = self._load_from_file()

    def _load_from_file(self) -> List[Event]:
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Event(
                    id=event['id'],
                    name=event['name'],
                    start_datetime=datetime.fromisoformat(event['start_datetime']),
                    duration=timedelta(hours=int(event['duration'].split(':')[0]),
                                       minutes=int(event['duration'].split(':')[1]),
                                       seconds=int(event['duration'].split(':')[2]))
                ) for event in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _save_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump([event.__dict__ for event in self._data_source], file, default=str)

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
        return [event for event in self._data_source if start <= event.start_datetime <= end and event.name == name]


    def add(self, item: Event):
        self._data_source.append(item)
        self._save_to_file()

    def update(self, item: Event):
        for index, event in enumerate(self._data_source):
            if event.id == item.id:
                self._data_source[index] = item
                self._save_to_file()
                return
        raise ValueError(f"Event with id {item.id} not found.")

    def delete(self, id: int):
        self._data_source = [event for event in self._data_source if event.id != id]
        self._save_to_file()
