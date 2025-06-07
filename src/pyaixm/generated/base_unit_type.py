from dataclasses import dataclass, field
from typing import Optional

from generated.reference_type import ReferenceType
from generated.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseUnitType(UnitDefinitionType):
    units_system: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "unitsSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
