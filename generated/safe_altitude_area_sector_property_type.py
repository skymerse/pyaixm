from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.safe_altitude_area_sector import SafeAltitudeAreaSector

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SafeAltitudeAreaSectorPropertyType(AbstractAixmpropertyType):
    safe_altitude_area_sector: Optional[SafeAltitudeAreaSector] = field(
        default=None,
        metadata={
            "name": "SafeAltitudeAreaSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
