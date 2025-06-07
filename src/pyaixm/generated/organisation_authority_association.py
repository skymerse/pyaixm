from dataclasses import dataclass

from pyaixm.generated.organisation_authority_association_type import (
    OrganisationAuthorityAssociationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OrganisationAuthorityAssociation(OrganisationAuthorityAssociationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
