from dataclasses import dataclass

from generated.taxiway_light_system_time_slice_type import (
    TaxiwayLightSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayLightSystemTimeSlice(TaxiwayLightSystemTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
