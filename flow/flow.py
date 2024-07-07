from abc import ABC, abstractmethod


class Flow(ABC):
    @abstractmethod
    def is_applicable(self, args: list[str]) -> bool:
        raise NotImplementedError

    @abstractmethod
    def execute(self, args: list[str]):
        raise NotImplementedError

    def try_execute(self, args: list[str]):
        if self.is_applicable(args):
            self.execute(args)