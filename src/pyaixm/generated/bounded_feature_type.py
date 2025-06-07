from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_feature_type import AbstractFeatureType
from pyaixm.generated.bounded_by import BoundedBy

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundedFeatureType(AbstractFeatureType):
    bounded_by: Optional[BoundedBy] = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
