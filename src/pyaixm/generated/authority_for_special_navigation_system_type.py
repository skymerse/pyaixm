from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.authority_for_special_navigation_system_type_extension import (
    AuthorityForSpecialNavigationSystemTypeExtension,
)
from pyaixm.generated.code_authority_role_type import CodeAuthorityRoleType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForSpecialNavigationSystemType(AbstractAixmobjectType):
    type_value: Optional[CodeAuthorityRoleType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    the_organisation_authority: Optional[OrganisationAuthorityPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "theOrganisationAuthority",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    extension: Iterable[AuthorityForSpecialNavigationSystemTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
