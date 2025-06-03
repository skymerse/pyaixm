from dataclasses import dataclass, field
from typing import Optional

from generated.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MappingRuleType:
    rule_definition: Optional[str] = field(
        default=None,
        metadata={
            "name": "ruleDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rule_reference: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "ruleReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
