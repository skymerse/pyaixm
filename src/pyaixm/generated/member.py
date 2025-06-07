from dataclasses import dataclass

from pyaixm.generated.association_role_type import AssociationRoleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Member(AssociationRoleType):
    class Meta:
        name = "member"
        namespace = "http://www.opengis.net/gml/3.2"
