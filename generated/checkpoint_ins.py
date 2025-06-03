from dataclasses import dataclass

from generated.checkpoint_instype import CheckpointInstype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointIns(CheckpointInstype):
    class Meta:
        name = "CheckpointINS"
        namespace = "http://www.aixm.aero/schema/5.1"
