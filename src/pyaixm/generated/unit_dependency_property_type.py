from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.unit_dependency import UnitDependency

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitDependencyPropertyType(AbstractAixmpropertyType):
    unit_dependency: Optional[UnitDependency] = field(
        default=None,
        metadata={
            "name": "UnitDependency",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
