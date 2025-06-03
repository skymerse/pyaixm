from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_holding_category_type import CodeHoldingCategoryType
from generated.code_status_operations_type import CodeStatusOperationsType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.guidance_line_property_type import GuidanceLinePropertyType
from generated.note_property_type import NotePropertyType
from generated.runway_property_type import RunwayPropertyType
from generated.taxi_holding_position_time_slice_type_extension import (
    TaxiHoldingPositionTimeSliceTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionTimeSliceType(AbstractAixmtimeSliceType):
    landing_category: Optional[CodeHoldingCategoryType] = field(
        default=None,
        metadata={
            "name": "landingCategory",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    status: Optional[CodeStatusOperationsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    associated_guidance_line: Optional[GuidanceLinePropertyType] = field(
        default=None,
        metadata={
            "name": "associatedGuidanceLine",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    protected_runway: Iterable[RunwayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "protectedRunway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ElevatedPointPropertyType] = field(
        default=None,
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
    extension: Iterable[TaxiHoldingPositionTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
