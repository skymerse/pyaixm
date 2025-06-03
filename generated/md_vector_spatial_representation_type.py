from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_md_spatial_representation_type import (
    AbstractMdSpatialRepresentationType,
)
from generated.md_geometric_objects_property_type import (
    MdGeometricObjectsPropertyType,
)
from generated.md_topology_level_code_property_type import (
    MdTopologyLevelCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdVectorSpatialRepresentationType(AbstractMdSpatialRepresentationType):
    """
    Information about the vector spatial objects in the dataset.
    """

    class Meta:
        name = "MD_VectorSpatialRepresentation_Type"

    topology_level: Optional[MdTopologyLevelCodePropertyType] = field(
        default=None,
        metadata={
            "name": "topologyLevel",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    geometric_objects: Iterable[MdGeometricObjectsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "geometricObjects",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
