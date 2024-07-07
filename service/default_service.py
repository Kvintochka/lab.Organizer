from datetime import datetime, timedelta

from repository.memory_repository import InMemoryEventRepository
from repository.model import Event
from repository.repository import EventRepository
from service.service import EventService
from writer.console_event_writer import ConsoleEventWriter
from writer.event_writer import EventWriter


class DefaultEventService(EventService):
    def __init__(self, repository: EventRepository, writer: EventWriter):
        self.repository = repository
        self.writer = writer
        self.id_counter = 1

    def create(self, event: Event):
        if event.id is None:
            event.id = self.id_counter
            self.id_counter += 1
        self.repository.add(event)

    def write_in_datatime_range(self, start: datetime, end: datetime):
        self.writer.write_all(self.repository.get_by_in_datetime_range(start, end))

    def write_by_datetime_intercept(self, start: datetime, end: datetime):
        self.writer.write_all(self.repository.get_by_datetime_intercept(start, end))

    def write_calendar(self, start: datetime, end: datetime):
        self.writer.write_calendar_in_range(self.repository.get_by_in_datetime_range(start, end), start, end)


