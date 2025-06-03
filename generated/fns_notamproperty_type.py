from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.fns_notam import FnsNotam

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class FnsNotampropertyType(AbstractAixmpropertyType):
    class Meta:
        name = "FNS_NOTAMPropertyType"

    fns_notam: Optional[FnsNotam] = field(
        default=None,
        metadata={
            "name": "FNS_NOTAM",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "required": True,
        },
    )
