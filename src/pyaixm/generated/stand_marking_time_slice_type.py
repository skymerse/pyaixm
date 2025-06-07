from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.aircraft_stand_property_type import (
    AircraftStandPropertyType,
)
from pyaixm.generated.code_marking_condition_type import (
    CodeMarkingConditionType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.marking_element_property_type import (
    MarkingElementPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.stand_marking_time_slice_type_extension import (
    StandMarkingTimeSliceTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandMarkingTimeSliceType(AbstractAixmtimeSliceType):
    marking_icaostandard: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "markingICAOStandard",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    condition: Optional[CodeMarkingConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element: Iterable[MarkingElementPropertyType] = field(
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
    marked_stand: Optional[AircraftStandPropertyType] = field(
        default=None,
        metadata={
            "name": "markedStand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[StandMarkingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
