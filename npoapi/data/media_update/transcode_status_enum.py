from enum import Enum

__NAMESPACE__ = "urn:vpro:media:update:2009"


class TranscodeStatusEnum(Enum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    TERMINATED = "TERMINATED"
    PAUSED = "PAUSED"
