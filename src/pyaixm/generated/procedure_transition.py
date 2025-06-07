from dataclasses import dataclass

from pyaixm.generated.procedure_transition_type import ProcedureTransitionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureTransition(ProcedureTransitionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
