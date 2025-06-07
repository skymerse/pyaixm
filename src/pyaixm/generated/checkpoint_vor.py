from dataclasses import dataclass

from pyaixm.generated.checkpoint_vortype import CheckpointVortype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointVor(CheckpointVortype):
    class Meta:
        name = "CheckpointVOR"
        namespace = "http://www.aixm.aero/schema/5.1"
