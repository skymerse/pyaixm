from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.checkpoint_instime_slice_type_extension import (
    CheckpointInstimeSliceTypeExtension,
)
from generated.code_altitude_use_type import CodeAltitudeUseType
from generated.code_checkpoint_category_type import CodeCheckpointCategoryType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.note_property_type import NotePropertyType
from generated.val_bearing_type import ValBearingType
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointInstimeSliceType(AbstractAixmtimeSliceType):
    class Meta:
        name = "CheckpointINSTimeSliceType"

    category: Optional[CodeCheckpointCategoryType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "upperLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "upperLimitReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "lowerLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "lowerLimitReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_interpretation: Optional[CodeAltitudeUseType] = field(
        default=None,
        metadata={
            "name": "altitudeInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    position: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    airport_heliport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "airportHeliport",
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
    extension: Iterable[CheckpointInstimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
