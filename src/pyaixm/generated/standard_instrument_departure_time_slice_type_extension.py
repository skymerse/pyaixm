from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.procedure_extension_1 import ProcedureExtension1
from pyaixm.generated.procedure_extension_2 import ProcedureExtension2
from pyaixm.generated.standard_instrument_departure_extension import (
    StandardInstrumentDepartureExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentDepartureTimeSliceTypeExtension:
    class Meta:
        global_type = False

    standard_instrument_departure_extension: Optional[
        StandardInstrumentDepartureExtension
    ] = field(
        default=None,
        metadata={
            "name": "StandardInstrumentDepartureExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    procedure_extension: Optional[ProcedureExtension2] = field(
        default=None,
        metadata={
            "name": "ProcedureExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_procedure_extension: Optional[
        ProcedureExtension1
    ] = field(
        default=None,
        metadata={
            "name": "ProcedureExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
