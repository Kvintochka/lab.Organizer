from date_time_converter.default_datetime import DefaultDataTimeConverter
from flow.calendar_flow import CalendarFlow
from flow.compose_flow import ComposeFlow
from flow.create_flow import CreateFlow
from flow.date_only_flow import DateOnlyFlow
from flow.date_time_flow import DateTimeFlow
from repository.file_repository import FileSystemEventRepository
from repository.memory_repository import InMemoryEventRepository
from service.default_service import DefaultEventService
from writer.console_event_writer import ConsoleEventWriter


event_service = DefaultEventService(FileSystemEventRepository('gipa.json'), ConsoleEventWriter())
date_time_converter = DefaultDataTimeConverter()

com_f = ComposeFlow([DateOnlyFlow(event_service, date_time_converter),
                     DateTimeFlow(event_service, date_time_converter),
                     CreateFlow(event_service, date_time_converter),
                     CalendarFlow(event_service, date_time_converter)])

com_f.try_execute(["2024/04/13", "01:00:00", "03:00:00", "Foreword"])
com_f.try_execute(["2024/04/13", "02:00:00", "05:00:00", "Don't Stay"])
com_f.try_execute(["2024/04/16", "03:00:00", "06:00:00", "Somewhere I Belong"])
com_f.try_execute(["2024/04/18", "04:00:00", "05:00:00", "Lying from You"])
com_f.try_execute(["2024/04/27", "05:00:00", "07:00:00", "Hit the Floor"])
com_f.try_execute(["2024/05/06", "06:00:00", "10:00:00", "Easier to Run", 67])
com_f.try_execute(["2024/05/06", "07:00:00", "17:00:00", "Faint"])
com_f.try_execute(["2024/05/06", "08:00:00", "09:00:00", "Figure.09"])
com_f.try_execute(["2024/05/27", "09:00:00", "11:00:00", "Breaking the Habit"])
com_f.try_execute(["2024/06/02", "10:00:00", "12:00:00", "From The Inside"])
com_f.try_execute(["2024/06/08", "11:00:00", "14:00:00", "Nobody's Listening"])
com_f.try_execute(["2024/06/10", "12:00:00", "20:00:00", "Session"])
com_f.try_execute(["2024/06/12", "13:00:00", "18:00:00", "Numb"])

com_f.try_execute(["2024/05/06", "07:00:00"])
com_f.try_execute(["2024/05/06"])
com_f.try_execute(["04/2024:06/2024"])