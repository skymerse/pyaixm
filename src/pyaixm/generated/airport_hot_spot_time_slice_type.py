from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.airport_hot_spot_time_slice_type_extension import (
    AirportHotSpotTimeSliceTypeExtension,
)
from generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.text_designator_type import TextDesignatorType
from generated.text_instruction_type import TextInstructionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHotSpotTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    area: Optional[ElevatedSurfacePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    affected_airport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "affectedAirport",
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
    extension: Iterable[AirportHotSpotTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
