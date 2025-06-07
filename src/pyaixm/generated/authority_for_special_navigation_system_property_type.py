from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.authority_for_special_navigation_system import (
    AuthorityForSpecialNavigationSystem,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForSpecialNavigationSystemPropertyType(
    AbstractAixmpropertyType
):
    authority_for_special_navigation_system: Optional[
        AuthorityForSpecialNavigationSystem
    ] = field(
        default=None,
        metadata={
            "name": "AuthorityForSpecialNavigationSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
