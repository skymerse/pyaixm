from dataclasses import dataclass

from pyaixm.generated.procedure_dmetime_slice_type import (
    ProcedureDmetimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureDmetimeSlice(ProcedureDmetimeSliceType):
    class Meta:
        name = "ProcedureDMETimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
