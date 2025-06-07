from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_procedure_type import AbstractProcedureType
from pyaixm.generated.standard_instrument_arrival_time_slice_property_type import (
    StandardInstrumentArrivalTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentArrivalType(AbstractProcedureType):
    time_slice: Iterable[StandardInstrumentArrivalTimeSlicePropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "timeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "min_occurs": 1,
            },
        )
    )
