from dataclasses import dataclass

from generated.procedure_transition_leg_type import ProcedureTransitionLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureTransitionLeg(ProcedureTransitionLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
