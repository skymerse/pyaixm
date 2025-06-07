from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_notamrequest_action_base_type import (
    CodeNotamrequestActionBaseType,
)
from pyaixm.generated.code_notamscenario_type_value import (
    CodeNotamscenarioTypeValue,
)
from pyaixm.generated.fns_notamproperty_type import FnsNotampropertyType
from pyaixm.generated.notamrequest_type_extension import (
    NotamrequestTypeExtension,
)
from pyaixm.generated.text_phone_type import TextPhoneType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class NotamrequestType(AbstractAixmobjectType):
    class Meta:
        name = "NOTAMRequestType"

    scenario_type: Optional[Union[str, CodeNotamscenarioTypeValue]] = field(
        default=None,
        metadata={
            "name": "scenarioType",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "pattern": r"OTHER(:(\w|_){1,58})?",
        },
    )
    request_action: Optional[CodeNotamrequestActionBaseType] = field(
        default=None,
        metadata={
            "name": "requestAction",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    originator_first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "originatorFirstName",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    originator_last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "originatorLastName",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    originator_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "originatorEmail",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    originator_phone: Optional[TextPhoneType] = field(
        default=None,
        metadata={
            "name": "originatorPhone",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    originator_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "originatorRemark",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    fns_notam: Optional[FnsNotampropertyType] = field(
        default=None,
        metadata={
            "name": "FNS_NOTAM",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    extension: Iterable[NotamrequestTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
