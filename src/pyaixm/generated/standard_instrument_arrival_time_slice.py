from dataclasses import dataclass

from pyaixm.generated.standard_instrument_arrival_time_slice_type import (
    StandardInstrumentArrivalTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentArrivalTimeSlice(
    StandardInstrumentArrivalTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
