from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Event:
    name: str
    start_datetime: datetime
    duration: timedelta
    id: int = field(default=None)

    def __getattr__(self, item):
        return self.get(item)

    @property
    def end_datetime(self):
        return self.start_datetime + self.duration