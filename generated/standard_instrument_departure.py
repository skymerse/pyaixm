from dataclasses import dataclass

from generated.standard_instrument_departure_type import (
    StandardInstrumentDepartureType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentDeparture(StandardInstrumentDepartureType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
