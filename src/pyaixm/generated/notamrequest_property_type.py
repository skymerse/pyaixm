from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.notamrequest import Notamrequest

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class NotamrequestPropertyType(AbstractAixmpropertyType):
    class Meta:
        name = "NOTAMRequestPropertyType"

    notamrequest: Optional[Notamrequest] = field(
        default=None,
        metadata={
            "name": "NOTAMRequest",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "required": True,
        },
    )
