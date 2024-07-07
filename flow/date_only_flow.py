from datetime import datetime

from date_time_converter.date_time_converter import DateTimeConverter
from flow.flow import Flow

from service.service import EventService


class DateOnlyFlow(Flow):
    def __init__(self, event_service: EventService, date_time_converter: DateTimeConverter):
        self.event_service = event_service
        self.date_time_converter = date_time_converter

    def is_applicable(self, args: list[str]) -> bool:
        return len(args) == 1 and self.date_time_converter.is_valid_date(args[0])

    def execute(self, args: list[str]):
        date_value = self.date_time_converter.convert_to_date(args[0])
        start = datetime.combine(date_value, datetime.min.time())
        end = datetime.combine(date_value, datetime.max.time())

        self.event_service.write_in_datatime_range(start, end)
