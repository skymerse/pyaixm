from dataclasses import dataclass

from generated.departure_arrival_condition_type import (
    DepartureArrivalConditionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureArrivalCondition(DepartureArrivalConditionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
