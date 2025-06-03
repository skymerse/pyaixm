from dataclasses import dataclass

from generated.taxiway_marking_time_slice_type import (
    TaxiwayMarkingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayMarkingTimeSlice(TaxiwayMarkingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
