from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.special_navigation_station_status import (
    SpecialNavigationStationStatus,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationStationStatusPropertyType(AbstractAixmpropertyType):
    special_navigation_station_status: Optional[
        SpecialNavigationStationStatus
    ] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationStationStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
