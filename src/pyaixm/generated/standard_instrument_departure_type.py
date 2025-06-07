from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_procedure_type import AbstractProcedureType
from pyaixm.generated.standard_instrument_departure_time_slice_property_type import (
    StandardInstrumentDepartureTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentDepartureType(AbstractProcedureType):
    time_slice: Iterable[StandardInstrumentDepartureTimeSlicePropertyType] = (
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
