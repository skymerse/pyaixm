from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airspace_property_type import AirspacePropertyType
from generated.code_flight_rule_type import CodeFlightRuleType
from generated.code_north_reference_type import CodeNorthReferenceType
from generated.note_property_type import NotePropertyType
from generated.standard_level_column_property_type import (
    StandardLevelColumnPropertyType,
)
from generated.standard_level_sector_time_slice_type_extension import (
    StandardLevelSectorTimeSliceTypeExtension,
)
from generated.val_bearing_type import ValBearingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelSectorTimeSliceType(AbstractAixmtimeSliceType):
    flight_rule: Optional[CodeFlightRuleType] = field(
        default=None,
        metadata={
            "name": "flightRule",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    from_track: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "fromTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    to_track: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "toTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_type: Optional[CodeNorthReferenceType] = field(
        default=None,
        metadata={
            "name": "angleType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    applicable_airspace: Iterable[AirspacePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "applicableAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    applicable_level_column: Optional[StandardLevelColumnPropertyType] = field(
        default=None,
        metadata={
            "name": "applicableLevelColumn",
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
    extension: Iterable[StandardLevelSectorTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
