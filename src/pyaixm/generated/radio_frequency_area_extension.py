from dataclasses import dataclass

from pyaixm.generated.radio_frequency_area_extension_type import (
    RadioFrequencyAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RadioFrequencyAreaExtension(RadioFrequencyAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
