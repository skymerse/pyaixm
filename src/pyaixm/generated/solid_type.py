from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_solid_type import AbstractSolidType
from generated.shell_property_type import ShellPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidType(AbstractSolidType):
    exterior: Optional[ShellPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interior: Iterable[ShellPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
