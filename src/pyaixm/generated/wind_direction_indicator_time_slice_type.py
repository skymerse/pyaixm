from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.code_status_operations_type import CodeStatusOperationsType
from generated.code_wind_direction_indicator_type import (
    CodeWindDirectionIndicatorType,
)
from generated.note_property_type import NotePropertyType
from generated.runway_property_type import RunwayPropertyType
from generated.wind_direction_indicator_time_slice_type_extension import (
    WindDirectionIndicatorTimeSliceTypeExtension,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class WindDirectionIndicatorTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeWindDirectionIndicatorType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    operational_status: Optional[CodeStatusOperationsType] = field(
        default=None,
        metadata={
            "name": "operationalStatus",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    associated_runway: Optional[RunwayPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedRunway",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    associated_airport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedAirport",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    extension: Iterable[WindDirectionIndicatorTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
