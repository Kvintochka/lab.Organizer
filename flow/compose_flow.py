from date_time_converter.default_datetime import DefaultDataTimeConverter

from flow.create_flow import CreateFlow
from flow.date_only_flow import DateOnlyFlow
from flow.date_time_flow import DateTimeFlow
from flow.flow import Flow
from repository.memory_repository import InMemoryEventRepository
from service.default_service import DefaultEventService
from writer.console_event_writer import ConsoleEventWriter


class ComposeFlow(Flow):
    def __init__(self, flow_list: list[Flow]):
        self.flow_list = flow_list

    def is_applicable(self, args: list[str]) -> bool:
        return any([flow.is_applicable(args) for flow in self.flow_list])

    def execute(self, args: list[str]):
        next(filter(lambda flow: flow.is_applicable(args), self.flow_list)).execute(args)


