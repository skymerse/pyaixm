from dataclasses import dataclass

from generated.checkpoint_vortype import CheckpointVortype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointVor(CheckpointVortype):
    class Meta:
        name = "CheckpointVOR"
        namespace = "http://www.aixm.aero/schema/5.1"
