from dataclasses import dataclass, field
from typing import Optional

from generated.definition_proxy import DefinitionProxy

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class IndirectEntryType:
    definition_proxy: Optional[DefinitionProxy] = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
