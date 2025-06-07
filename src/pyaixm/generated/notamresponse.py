from dataclasses import dataclass

from pyaixm.generated.notamresponse_type import NotamresponseType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class Notamresponse(NotamresponseType):
    class Meta:
        name = "NOTAMResponse"
        namespace = "urn:us.gov.dot.faa.aim.fns"
