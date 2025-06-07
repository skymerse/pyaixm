from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.definition_base_type import DefinitionBaseType
from pyaixm.generated.remarks import Remarks

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
