from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.authority_for_special_navigation_station import (
    AuthorityForSpecialNavigationStation,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForSpecialNavigationStationPropertyType(
    AbstractAixmpropertyType
):
    authority_for_special_navigation_station: Optional[
        AuthorityForSpecialNavigationStation
    ] = field(
        default=None,
        metadata={
            "name": "AuthorityForSpecialNavigationStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
