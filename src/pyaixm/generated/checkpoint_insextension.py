from dataclasses import dataclass

from generated.checkpoint_insextension_type import CheckpointInsextensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class CheckpointInsextension(CheckpointInsextensionType):
    class Meta:
        name = "CheckpointINSExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
