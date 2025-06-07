from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_flight_restriction_designator_type import (
    CodeFlightRestrictionDesignatorType,
)
from pyaixm.generated.code_flight_restriction_type import (
    CodeFlightRestrictionType,
)
from pyaixm.generated.flight_condition_combination_property_type import (
    FlightConditionCombinationPropertyType,
)
from pyaixm.generated.flight_restriction_route_property_type import (
    FlightRestrictionRoutePropertyType,
)
from pyaixm.generated.flight_restriction_time_slice_type_extension import (
    FlightRestrictionTimeSliceTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.text_instruction_type import TextInstructionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[CodeFlightRestrictionDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeFlightRestrictionType] = field(
        default=None,
        metadata={
            "name": "type",
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
    flight: Optional[FlightConditionCombinationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    regulated_route: Iterable[FlightRestrictionRoutePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "regulatedRoute",
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
    extension: Iterable[FlightRestrictionTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
