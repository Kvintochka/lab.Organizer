from datetime import datetime

from date_time_converter.date_time_converter import DateTimeConverter
from flow.flow import Flow

from repository.model import Event

from service.service import EventService


class CreateFlow(Flow):
    def __init__(self, event_service: EventService, date_time_converter: DateTimeConverter):
        self.event_service = event_service
        self.date_time_converter = date_time_converter

    def is_applicable(self, args: list[str]) -> bool:
        return (len(args) > 3 and self.date_time_converter.is_valid_date(args[0]) and
                self.date_time_converter.is_valid_time(args[1]) and self.date_time_converter.is_valid_time(args[2]))

    def execute(self, args: list[str]):
        date_value = self.date_time_converter.convert_to_date(args[0])
        time_format = "%H:%M:%S"
        start_time = datetime.strptime(args[1], time_format)
        end_time = datetime.strptime(args[2], time_format)
        event_id = int(args[4]) if len(args) > 4 else None
        self.event_service.create(Event(name=args[3],start_datetime= datetime.combine(date_value, self.date_time_converter.convert_to_time(args[1])),
                                        duration= end_time - start_time, id=event_id))
