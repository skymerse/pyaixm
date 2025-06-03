from dataclasses import dataclass, field
from typing import Optional

from generated.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeReferenceSystemType(DefinitionType):
    domain_of_validity: Optional[str] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
