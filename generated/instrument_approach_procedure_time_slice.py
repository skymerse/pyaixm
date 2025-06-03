from dataclasses import dataclass

from generated.instrument_approach_procedure_time_slice_type import (
    InstrumentApproachProcedureTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InstrumentApproachProcedureTimeSlice(
    InstrumentApproachProcedureTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
