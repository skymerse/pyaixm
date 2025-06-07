from dataclasses import dataclass

from pyaixm.generated.standard_instrument_arrival_extension_type import (
    StandardInstrumentArrivalExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class StandardInstrumentArrivalExtension(
    StandardInstrumentArrivalExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
