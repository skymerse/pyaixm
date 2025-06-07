from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.approach_altitude_table_property_type import (
    ApproachAltitudeTablePropertyType,
)
from pyaixm.generated.approach_distance_table_property_type import (
    ApproachDistanceTablePropertyType,
)
from pyaixm.generated.approach_timing_table_property_type import (
    ApproachTimingTablePropertyType,
)
from pyaixm.generated.final_profile_type_extension import (
    FinalProfileTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FinalProfileType(AbstractAixmobjectType):
    altitude: Iterable[ApproachAltitudeTablePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    distance: Iterable[ApproachDistanceTablePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    timing: Iterable[ApproachTimingTablePropertyType] = field(
        default_factory=list,
        metadata={
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
    extension: Iterable[FinalProfileTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
