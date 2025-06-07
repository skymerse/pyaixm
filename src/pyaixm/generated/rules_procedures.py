from dataclasses import dataclass

from pyaixm.generated.rules_procedures_type import RulesProceduresType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RulesProcedures(RulesProceduresType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
