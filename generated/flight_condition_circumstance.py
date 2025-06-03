from dataclasses import dataclass

from generated.flight_condition_circumstance_type import (
    FlightConditionCircumstanceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightConditionCircumstance(FlightConditionCircumstanceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
