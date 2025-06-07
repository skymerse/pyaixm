from dataclasses import dataclass

from pyaixm.generated.checkpoint_vorextension_type import (
    CheckpointVorextensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class CheckpointVorextension(CheckpointVorextensionType):
    class Meta:
        name = "CheckpointVORExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
