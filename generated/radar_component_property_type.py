from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.radar_component import RadarComponent

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarComponentPropertyType(AbstractAixmpropertyType):
    radar_component: Optional[RadarComponent] = field(
        default=None,
        metadata={
            "name": "RadarComponent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
