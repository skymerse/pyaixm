from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.notamresponse import Notamresponse

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class NotamresponsePropertyType(AbstractAixmpropertyType):
    class Meta:
        name = "NOTAMResponsePropertyType"

    notamresponse: Optional[Notamresponse] = field(
        default=None,
        metadata={
            "name": "NOTAMResponse",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "required": True,
        },
    )
