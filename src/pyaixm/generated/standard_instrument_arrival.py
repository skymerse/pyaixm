from dataclasses import dataclass

from pyaixm.generated.standard_instrument_arrival_type import (
    StandardInstrumentArrivalType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentArrival(StandardInstrumentArrivalType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
