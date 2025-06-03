from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_marking_condition_type import CodeMarkingConditionType
from generated.code_yes_no_type import CodeYesNoType
from generated.marking_element_property_type import MarkingElementPropertyType
from generated.note_property_type import NotePropertyType
from generated.taxi_holding_position_marking_time_slice_type_extension import (
    TaxiHoldingPositionMarkingTimeSliceTypeExtension,
)
from generated.taxi_holding_position_property_type import (
    TaxiHoldingPositionPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionMarkingTimeSliceType(AbstractAixmtimeSliceType):
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
    marked_taxi_hold: Optional[TaxiHoldingPositionPropertyType] = field(
        default=None,
        metadata={
            "name": "markedTaxiHold",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TaxiHoldingPositionMarkingTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
