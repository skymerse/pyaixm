from dataclasses import dataclass

from pyaixm.generated.road_extension_type import RoadExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RoadExtension(RoadExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
