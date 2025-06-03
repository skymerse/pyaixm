from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.flight_condition_circumstance import FlightConditionCircumstance

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightConditionCircumstancePropertyType(AbstractAixmpropertyType):
    flight_condition_circumstance: Optional[FlightConditionCircumstance] = (
        field(
            default=None,
            metadata={
                "name": "FlightConditionCircumstance",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
