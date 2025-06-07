from dataclasses import dataclass

from pyaixm.generated.organisation_authority_type import (
    OrganisationAuthorityType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OrganisationAuthority(OrganisationAuthorityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
