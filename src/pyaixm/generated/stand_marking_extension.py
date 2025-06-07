from dataclasses import dataclass

from pyaixm.generated.stand_marking_extension_type import (
    StandMarkingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class StandMarkingExtension(StandMarkingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
