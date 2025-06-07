from dataclasses import dataclass

from generated.procedure_extension_type_1 import ProcedureExtensionType1

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ProcedureExtension1(ProcedureExtensionType1):
    class Meta:
        name = "ProcedureExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
