from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.instrument_approach_procedure_extension_1 import (
    InstrumentApproachProcedureExtension1,
)
from pyaixm.generated.instrument_approach_procedure_extension_2 import (
    InstrumentApproachProcedureExtension2,
)
from pyaixm.generated.procedure_extension_1 import ProcedureExtension1
from pyaixm.generated.procedure_extension_2 import ProcedureExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InstrumentApproachProcedureTimeSliceTypeExtension:
    class Meta:
        global_type = False

    instrument_approach_procedure_extension: Optional[
        InstrumentApproachProcedureExtension2
    ] = field(
        default=None,
        metadata={
            "name": "InstrumentApproachProcedureExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_instrument_approach_procedure_extension: Optional[
        InstrumentApproachProcedureExtension1
    ] = field(
        default=None,
        metadata={
            "name": "InstrumentApproachProcedureExtension",
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
