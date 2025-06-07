from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmfeature_base_type import (
    AbstractAixmfeatureBaseType,
)
from pyaixm.generated.feature_metadata_property_type import (
    FeatureMetadataPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmfeatureType(AbstractAixmfeatureBaseType):
    """
    Adds the FeatureMetadata, which is common to all AIXM features.
    """

    class Meta:
        name = "AbstractAIXMFeatureType"

    feature_metadata: Optional[FeatureMetadataPropertyType] = field(
        default=None,
        metadata={
            "name": "featureMetadata",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
