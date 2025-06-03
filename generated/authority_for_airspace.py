from dataclasses import dataclass

from generated.authority_for_airspace_type import AuthorityForAirspaceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForAirspace(AuthorityForAirspaceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
