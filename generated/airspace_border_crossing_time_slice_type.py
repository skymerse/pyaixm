from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airspace_border_crossing_time_slice_type_extension import (
    AirspaceBorderCrossingTimeSliceTypeExtension,
)
from generated.airspace_property_type import AirspacePropertyType
from generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceBorderCrossingTimeSliceType(AbstractAixmtimeSliceType):
    exited_airspace: Optional[AirspacePropertyType] = field(
        default=None,
        metadata={
            "name": "exitedAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    entered_airspace: Optional[AirspacePropertyType] = field(
        default=None,
        metadata={
            "name": "enteredAirspace",
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
    extension: Iterable[AirspaceBorderCrossingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
