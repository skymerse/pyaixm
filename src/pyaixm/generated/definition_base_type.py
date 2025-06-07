from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_gmltype import AbstractGmltype
from generated.identifier import Identifier

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionBaseType(AbstractGmltype):
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
