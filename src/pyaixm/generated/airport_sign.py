from dataclasses import dataclass

from pyaixm.generated.airport_sign_type import AirportSignType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportSign(AirportSignType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
