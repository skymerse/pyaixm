from dataclasses import dataclass

from pyaixm.generated.instrument_approach_procedure_extension_type_2 import (
    InstrumentApproachProcedureExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class InstrumentApproachProcedureExtension2(
    InstrumentApproachProcedureExtensionType2
):
    class Meta:
        name = "InstrumentApproachProcedureExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
