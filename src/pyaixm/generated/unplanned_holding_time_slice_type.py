from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_approval_type import CodeApprovalType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.code_yes_no_type import CodeYesNoType
from generated.note_property_type import NotePropertyType
from generated.segment_point_property_type import SegmentPointPropertyType
from generated.unplanned_holding_time_slice_type_extension import (
    UnplannedHoldingTimeSliceTypeExtension,
)
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnplannedHoldingTimeSliceType(AbstractAixmtimeSliceType):
    unplanned_holding: Optional[CodeApprovalType] = field(
        default=None,
        metadata={
            "name": "unplannedHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    authorized_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "authorizedAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "altitudeReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    controlled_airspace: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "controlledAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    holding_point: Optional[SegmentPointPropertyType] = field(
        default=None,
        metadata={
            "name": "holdingPoint",
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
    extension: Iterable[UnplannedHoldingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
