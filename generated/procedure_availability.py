from dataclasses import dataclass

from generated.procedure_availability_type import ProcedureAvailabilityType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureAvailability(ProcedureAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
