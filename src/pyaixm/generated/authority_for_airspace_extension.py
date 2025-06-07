from dataclasses import dataclass

from pyaixm.generated.authority_for_airspace_extension_type import (
    AuthorityForAirspaceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AuthorityForAirspaceExtension(AuthorityForAirspaceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
