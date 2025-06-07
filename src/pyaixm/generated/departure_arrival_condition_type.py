from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from pyaixm.generated.code_vertical_reference_type import (
    CodeVerticalReferenceType,
)
from pyaixm.generated.departure_arrival_condition_type_extension import (
    DepartureArrivalConditionTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureArrivalConditionType(AbstractAixmobjectType):
    minimum_enroute_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "minimumEnrouteAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_crossing_at_end: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "minimumCrossingAtEnd",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_crossing_at_end_reference: Optional[CodeVerticalReferenceType] = (
        field(
            default=None,
            metadata={
                "name": "minimumCrossingAtEndReference",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    maximum_crossing_at_end: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "maximumCrossingAtEnd",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    maximum_crossing_at_end_reference: Optional[CodeVerticalReferenceType] = (
        field(
            default=None,
            metadata={
                "name": "maximumCrossingAtEndReference",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    engine_type: Optional[AircraftCharacteristicPropertyType] = field(
        default=None,
        metadata={
            "name": "engineType",
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
    extension: Iterable[DepartureArrivalConditionTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
