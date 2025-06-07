from dataclasses import dataclass

from pyaixm.generated.abstract_usage_condition_type import (
    AbstractUsageConditionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractUsageCondition(AbstractUsageConditionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
