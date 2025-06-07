from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.definition_ref import DefinitionRef
from pyaixm.generated.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionProxyType(DefinitionType):
    definition_ref: Optional[DefinitionRef] = field(
        default=None,
        metadata={
            "name": "definitionRef",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
