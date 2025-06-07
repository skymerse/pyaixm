from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_marking_condition_type import CodeMarkingConditionType
from generated.code_tlofsection_type import CodeTlofsectionType
from generated.code_yes_no_type import CodeYesNoType
from generated.marking_element_property_type import MarkingElementPropertyType
from generated.note_property_type import NotePropertyType
from generated.touch_down_lift_off_marking_time_slice_type_extension import (
    TouchDownLiftOffMarkingTimeSliceTypeExtension,
)
from generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffMarkingTimeSliceType(AbstractAixmtimeSliceType):
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
    marking_location: Optional[CodeTlofsectionType] = field(
        default=None,
        metadata={
            "name": "markingLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marked_touch_down_lift_off: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "markedTouchDownLiftOff",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TouchDownLiftOffMarkingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
