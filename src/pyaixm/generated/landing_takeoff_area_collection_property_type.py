from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.landing_takeoff_area_collection import (
    LandingTakeoffAreaCollection,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LandingTakeoffAreaCollectionPropertyType(AbstractAixmpropertyType):
    landing_takeoff_area_collection: Optional[LandingTakeoffAreaCollection] = (
        field(
            default=None,
            metadata={
                "name": "LandingTakeoffAreaCollection",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
