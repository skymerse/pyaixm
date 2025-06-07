from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.landing_takeoff_area_collection_type_extension import (
    LandingTakeoffAreaCollectionTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LandingTakeoffAreaCollectionType(AbstractAixmobjectType):
    runway: Iterable[RunwayDirectionPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    tlof: Iterable[TouchDownLiftOffPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "TLOF",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[LandingTakeoffAreaCollectionTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
