from dataclasses import dataclass

from pyaixm.generated.instrument_approach_procedure_extension_type_1 import (
    InstrumentApproachProcedureExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class InstrumentApproachProcedureExtension1(
    InstrumentApproachProcedureExtensionType1
):
    class Meta:
        name = "InstrumentApproachProcedureExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
