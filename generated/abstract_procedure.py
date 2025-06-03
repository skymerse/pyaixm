from dataclasses import dataclass

from generated.abstract_procedure_type import AbstractProcedureType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractProcedure(AbstractProcedureType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
