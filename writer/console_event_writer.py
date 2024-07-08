import calendar as cal
from collections import defaultdict
from datetime import date, datetime

from writer.event_writer import EventWriter
from repository.model import Event


class ConsoleEventWriter(EventWriter):
    def write(self, event: Event):
        print(
            f"{event.id} {event.name} on {event.start_datetime.strftime("%A, %d %B %Y at %I:%M%p")} for {event.end_datetime.strftime("%I:%M%p")}\n")

    def write_calendar_in_range(self, events: list[Event], start: date, end: date):
        current_date = start
        while current_date <= end:
            self.__display_calendar(current_date.year, current_date.month, events)
            next_month = current_date.month + 1
            if next_month > 12:
                current_date = datetime(current_date.year + 1, 1, 1)

            else:
                current_date = datetime(current_date.year, next_month, 1)

    def __map_events_to_date_count(self, events: list[Event]) -> dict[date, int]:
        date_count = defaultdict(int)
        for event in events:
            event_date = event.start_datetime.date()
            date_count[event_date] += 1
        return dict(date_count)

    def __display_calendar(self, year, month, events):
        event_counts = self.__map_events_to_date_count(events)
        cal_mon = cal.monthcalendar(year, month)
        event_calendar = []

        month_event_count = sum(count for event_date, count in event_counts.items() if event_date.month == month)

        month_name = cal.month_name[month]
        event_calendar.append(f"{month_name} ({month_event_count}) {year}".center(50))
        event_calendar.append("Mo      Tu      We      Th      Fr      Sa      Su")
        for week in cal_mon:
            new_line = ""
            for day in week:
                if not day:
                    new_line += " " * 8
                    continue
                current_date = date(year, month, day)
                if current_date in event_counts:
                    new_line += f"{day:>{2}}[{event_counts[current_date]}]" + (4 - len(str(event_counts[current_date])))*" "
                else:
                    new_line += f"{day:>{2}}" + 6 * ' '

            event_calendar.append(new_line.rstrip())
        event_calendar.append("\n")

        # Print the final event calendar
        print('\n'.join(event_calendar))

