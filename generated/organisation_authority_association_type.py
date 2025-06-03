from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_organisation_hierarchy_type import (
    CodeOrganisationHierarchyType,
)
from generated.note_property_type import NotePropertyType
from generated.organisation_authority_association_type_extension import (
    OrganisationAuthorityAssociationTypeExtension,
)
from generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OrganisationAuthorityAssociationType(AbstractAixmobjectType):
    type_value: Optional[CodeOrganisationHierarchyType] = field(
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
    extension: Iterable[OrganisationAuthorityAssociationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
