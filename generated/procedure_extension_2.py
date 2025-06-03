from dataclasses import dataclass

from generated.procedure_extension_type_2 import ProcedureExtensionType2

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ProcedureExtension2(ProcedureExtensionType2):
    class Meta:
        name = "ProcedureExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
