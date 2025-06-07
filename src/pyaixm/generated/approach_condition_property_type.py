from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.approach_condition import ApproachCondition

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachConditionPropertyType(AbstractAixmpropertyType):
    approach_condition: Optional[ApproachCondition] = field(
        default=None,
        metadata={
            "name": "ApproachCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
