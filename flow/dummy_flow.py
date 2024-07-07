from compose_flow import ComposeFlow
from flow.flow import Flow


class AlwaysTrueFlow(Flow):
    def is_applicable(self, args: list[str]) -> bool:
        return True

    def execute(self, args: list[str]):
        print("TRUE")


class AlwaysFalseFlow(Flow):
    def is_applicable(self, args: list[str]) -> bool:
        return False

    def execute(self, args: list[str]):
        print("FALSE")


flow_true = AlwaysTrueFlow()

flow_false = AlwaysFalseFlow()

compose_flow = ComposeFlow([flow_false, flow_false])
compose_flow1 = ComposeFlow([flow_false, flow_false, flow_true])
compose_flow.try_execute([])
compose_flow1.try_execute([])
