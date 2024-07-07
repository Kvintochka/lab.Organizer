from datetime import datetime

from date_time_converter.date_time_converter import DateTimeConverter
from flow.flow import Flow

from service.service import EventService


class DateTimeFlow(Flow):
    def __init__(self, event_service: EventService, date_time_converter: DateTimeConverter):
        self.event_service = event_service
        self.date_time_converter = date_time_converter
    def is_applicable(self, args: list[str]) -> bool:
        one_time = (2 <= len(args) <= 3 and
                    self.date_time_converter.is_valid_date(args[0]) and
                    self.date_time_converter.is_valid_time(args[1]))
        return one_time if len(args) == 2 else one_time and self.date_time_converter.is_valid_time(args[2])

    def execute(self, args: list[str]):

        date_value = self.date_time_converter.convert_to_date(args[0])
        start = datetime.combine(date_value, self.date_time_converter.convert_to_time(args[1]))
        if len(args) == 2:
            end = start
        if len(args) == 3:
            end = datetime.combine(date_value, self.date_time_converter.convert_to_time(args[2]))
        self.event_service.write_by_datetime_intercept(start, end)
