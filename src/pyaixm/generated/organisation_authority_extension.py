from dataclasses import dataclass

from generated.organisation_authority_extension_type import (
    OrganisationAuthorityExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class OrganisationAuthorityExtension(OrganisationAuthorityExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
