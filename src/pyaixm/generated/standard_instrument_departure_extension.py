from dataclasses import dataclass

from pyaixm.generated.standard_instrument_departure_extension_type import (
    StandardInstrumentDepartureExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class StandardInstrumentDepartureExtension(
    StandardInstrumentDepartureExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
