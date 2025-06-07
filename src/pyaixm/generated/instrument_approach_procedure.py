from dataclasses import dataclass

from pyaixm.generated.instrument_approach_procedure_type import (
    InstrumentApproachProcedureType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InstrumentApproachProcedure(InstrumentApproachProcedureType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
