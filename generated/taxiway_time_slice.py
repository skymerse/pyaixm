from dataclasses import dataclass

from generated.taxiway_time_slice_type import TaxiwayTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayTimeSlice(TaxiwayTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
