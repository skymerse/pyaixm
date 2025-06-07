from dataclasses import dataclass

from pyaixm.generated.distance_indication_extension_type import (
    DistanceIndicationExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class DistanceIndicationExtension(DistanceIndicationExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
