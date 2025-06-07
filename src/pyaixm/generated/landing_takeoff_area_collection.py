from dataclasses import dataclass

from generated.landing_takeoff_area_collection_type import (
    LandingTakeoffAreaCollectionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LandingTakeoffAreaCollection(LandingTakeoffAreaCollectionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
