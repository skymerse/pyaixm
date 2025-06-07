from dataclasses import dataclass

from pyaixm.generated.procedure_dmeextension_type import (
    ProcedureDmeextensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ProcedureDmeextension(ProcedureDmeextensionType):
    class Meta:
        name = "ProcedureDMEExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
