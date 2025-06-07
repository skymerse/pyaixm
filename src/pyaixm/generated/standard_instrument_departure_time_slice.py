from dataclasses import dataclass

from pyaixm.generated.standard_instrument_departure_time_slice_type import (
    StandardInstrumentDepartureTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentDepartureTimeSlice(
    StandardInstrumentDepartureTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
