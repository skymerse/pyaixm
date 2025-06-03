from dataclasses import dataclass, field
from typing import Optional

from generated.definition_base_type import DefinitionBaseType
from generated.remarks import Remarks

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionType(DefinitionBaseType):
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
