from dataclasses import dataclass

from pyaixm.generated.procedure_availability_type import (
    ProcedureAvailabilityType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureAvailability(ProcedureAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
