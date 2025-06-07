from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_response_status_type import CodeResponseStatusType
from generated.fns_notamproperty_type import FnsNotampropertyType
from generated.notamresponse_type_extension import NotamresponseTypeExtension

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class NotamresponseType(AbstractAixmobjectType):
    class Meta:
        name = "NOTAMResponseType"

    status: Optional[CodeResponseStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    has_notam: Iterable[FnsNotampropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hasNOTAM",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    extension: Iterable[NotamresponseTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
