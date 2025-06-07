from dataclasses import dataclass

from pyaixm.generated.ci_responsible_party_type import CiResponsiblePartyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiResponsibleParty(CiResponsiblePartyType):
    class Meta:
        name = "CI_ResponsibleParty"
        namespace = "http://www.isotc211.org/2005/gmd"
