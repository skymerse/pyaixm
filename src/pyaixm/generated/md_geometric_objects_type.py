from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.integer_property_type import IntegerPropertyType
from pyaixm.generated.md_geometric_object_type_code_property_type import (
    MdGeometricObjectTypeCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeometricObjectsType(AbstractObjectType):
    class Meta:
        name = "MD_GeometricObjects_Type"

    geometric_object_type: Optional[MdGeometricObjectTypeCodePropertyType] = (
        field(
            default=None,
            metadata={
                "name": "geometricObjectType",
                "type": "Element",
                "namespace": "http://www.isotc211.org/2005/gmd",
                "required": True,
            },
        )
    )
    geometric_object_count: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "geometricObjectCount",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
