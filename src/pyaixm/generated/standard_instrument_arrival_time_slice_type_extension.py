from dataclasses import dataclass, field
from typing import Optional

from generated.procedure_extension_1 import ProcedureExtension1
from generated.procedure_extension_2 import ProcedureExtension2
from generated.standard_instrument_arrival_extension import (
    StandardInstrumentArrivalExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentArrivalTimeSliceTypeExtension:
    class Meta:
        global_type = False

    standard_instrument_arrival_extension: Optional[
        StandardInstrumentArrivalExtension
    ] = field(
        default=None,
        metadata={
            "name": "StandardInstrumentArrivalExtension",
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
