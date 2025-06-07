from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.departure_arrival_condition import DepartureArrivalCondition

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureArrivalConditionPropertyType(AbstractAixmpropertyType):
    departure_arrival_condition: Optional[DepartureArrivalCondition] = field(
        default=None,
        metadata={
            "name": "DepartureArrivalCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
