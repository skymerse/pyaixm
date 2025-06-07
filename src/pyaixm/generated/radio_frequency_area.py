from dataclasses import dataclass

from pyaixm.generated.radio_frequency_area_type import RadioFrequencyAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioFrequencyArea(RadioFrequencyAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
