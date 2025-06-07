from dataclasses import dataclass

from pyaixm.generated.ci_contact_type import CiContactType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiContact(CiContactType):
    class Meta:
        name = "CI_Contact"
        namespace = "http://www.isotc211.org/2005/gmd"
