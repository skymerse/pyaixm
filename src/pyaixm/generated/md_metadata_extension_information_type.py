from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_object_type import AbstractObjectType
from generated.ci_online_resource_property_type import (
    CiOnlineResourcePropertyType,
)
from generated.md_extended_element_information_property_type import (
    MdExtendedElementInformationPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMetadataExtensionInformationType(AbstractObjectType):
    """
    Information describing metadata extensions.
    """

    class Meta:
        name = "MD_MetadataExtensionInformation_Type"

    extension_on_line_resource: Optional[CiOnlineResourcePropertyType] = field(
        default=None,
        metadata={
            "name": "extensionOnLineResource",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    extended_element_information: Iterable[
        MdExtendedElementInformationPropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "extendedElementInformation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
