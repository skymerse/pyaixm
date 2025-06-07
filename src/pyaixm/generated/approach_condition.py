from dataclasses import dataclass

from generated.approach_condition_type import ApproachConditionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachCondition(ApproachConditionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
