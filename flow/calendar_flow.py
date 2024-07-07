from calendar import monthrange
from datetime import datetime
import re

from date_time_converter.date_time_converter import DateTimeConverter
from flow.flow import Flow

from service.service import EventService


class CalendarFlow(Flow):
    def __init__(self, event_service: EventService, date_time_converter: DateTimeConverter):
        self.event_service = event_service
        self.date_time_converter = date_time_converter

    def is_applicable(self, args: list[str]) -> bool:
        return (len(args) == 1 and re.fullmatch(r"\d{2}/\d{4}:\d{2}/\d{4}", args[0]))

    def execute(self, args: list[str]):
        start, end = args[0].split(':')

        start_date = datetime.strptime(start, "%m/%Y")
        end_date = datetime.strptime(end, "%m/%Y")

        last_day_of_month = monthrange(end_date.year, end_date.month)[1]
        end_date = end_date.replace(day=last_day_of_month)

        self.event_service.write_calendar(start_date, end_date)
