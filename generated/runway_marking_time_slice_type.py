from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_marking_condition_type import CodeMarkingConditionType
from generated.code_runway_section_type import CodeRunwaySectionType
from generated.code_yes_no_type import CodeYesNoType
from generated.marking_element_property_type import MarkingElementPropertyType
from generated.note_property_type import NotePropertyType
from generated.runway_marking_time_slice_type_extension import (
    RunwayMarkingTimeSliceTypeExtension,
)
from generated.runway_property_type import RunwayPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayMarkingTimeSliceType(AbstractAixmtimeSliceType):
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
    marking_location: Optional[CodeRunwaySectionType] = field(
        default=None,
        metadata={
            "name": "markingLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marked_runway: Optional[RunwayPropertyType] = field(
        default=None,
        metadata={
            "name": "markedRunway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[RunwayMarkingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
