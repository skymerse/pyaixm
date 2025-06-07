from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.organisation_authority_association import (
    OrganisationAuthorityAssociation,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OrganisationAuthorityAssociationPropertyType(AbstractAixmpropertyType):
    organisation_authority_association: Optional[
        OrganisationAuthorityAssociation
    ] = field(
        default=None,
        metadata={
            "name": "OrganisationAuthorityAssociation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
