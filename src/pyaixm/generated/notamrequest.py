from dataclasses import dataclass

from pyaixm.generated.notamrequest_type import NotamrequestType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class Notamrequest(NotamrequestType):
    class Meta:
        name = "NOTAMRequest"
        namespace = "urn:us.gov.dot.faa.aim.fns"
