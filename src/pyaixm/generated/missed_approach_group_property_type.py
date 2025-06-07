from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.missed_approach_group import MissedApproachGroup

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MissedApproachGroupPropertyType(AbstractAixmpropertyType):
    missed_approach_group: Optional[MissedApproachGroup] = field(
        default=None,
        metadata={
            "name": "MissedApproachGroup",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
