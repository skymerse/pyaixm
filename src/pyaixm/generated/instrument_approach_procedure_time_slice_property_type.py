from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.instrument_approach_procedure_time_slice import (
    InstrumentApproachProcedureTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InstrumentApproachProcedureTimeSlicePropertyType:
    instrument_approach_procedure_time_slice: Optional[
        InstrumentApproachProcedureTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "InstrumentApproachProcedureTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
