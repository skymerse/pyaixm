from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.navaid_component import NavaidComponent

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidComponentPropertyType(AbstractAixmpropertyType):
    navaid_component: Optional[NavaidComponent] = field(
        default=None,
        metadata={
            "name": "NavaidComponent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
