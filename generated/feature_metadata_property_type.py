from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_metadata_property_type import (
    AbstractMetadataPropertyType,
)
from generated.md_metadata_type import MdMetadata

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FeatureMetadataPropertyType(AbstractMetadataPropertyType):
    md_metadata: Optional[MdMetadata] = field(
        default=None,
        metadata={
            "name": "MD_Metadata",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
