from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.surveillance_ground_station import (
    SurveillanceGroundStation,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurveillanceGroundStationPropertyType(AbstractAixmpropertyType):
    surveillance_ground_station: Optional[SurveillanceGroundStation] = field(
        default=None,
        metadata={
            "name": "SurveillanceGroundStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
