from dataclasses import dataclass

from pyaixm.generated.taxiway_element_time_slice_type import (
    TaxiwayElementTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayElementTimeSlice(TaxiwayElementTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
