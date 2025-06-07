from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.navigation_area_sector import NavigationAreaSector

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaSectorPropertyType(AbstractAixmpropertyType):
    navigation_area_sector: Optional[NavigationAreaSector] = field(
        default=None,
        metadata={
            "name": "NavigationAreaSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
