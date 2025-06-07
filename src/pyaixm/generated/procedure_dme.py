from dataclasses import dataclass

from generated.procedure_dmetype import ProcedureDmetype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureDme(ProcedureDmetype):
    class Meta:
        name = "ProcedureDME"
        namespace = "http://www.aixm.aero/schema/5.1"
