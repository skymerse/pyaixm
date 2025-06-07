from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from pyaixm.generated.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from pyaixm.generated.md_aggregate_information_property_type import (
    MdAggregateInformationPropertyType,
)
from pyaixm.generated.md_browse_graphic_property_type import (
    MdBrowseGraphicPropertyType,
)
from pyaixm.generated.md_constraints_property_type import (
    MdConstraintsPropertyType,
)
from pyaixm.generated.md_distributor_type import MdFormatPropertyType
from pyaixm.generated.md_identifier_type import CiCitationPropertyType
from pyaixm.generated.md_keywords_property_type import MdKeywordsPropertyType
from pyaixm.generated.md_maintenance_information_property_type import (
    MdMaintenanceInformationPropertyType,
)
from pyaixm.generated.md_progress_code_property_type import (
    MdProgressCodePropertyType,
)
from pyaixm.generated.md_usage_property_type import MdUsagePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdIdentificationType(AbstractObjectType):
    """
    Basic information about data.
    """

    class Meta:
        name = "AbstractMD_Identification_Type"

    citation: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    abstract: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    purpose: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    credit: Iterable[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    status: Iterable[MdProgressCodePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    point_of_contact: Iterable[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "pointOfContact",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_maintenance: Iterable[MdMaintenanceInformationPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "resourceMaintenance",
                "type": "Element",
                "namespace": "http://www.isotc211.org/2005/gmd",
            },
        )
    )
    graphic_overview: Iterable[MdBrowseGraphicPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "graphicOverview",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_format: Iterable[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    descriptive_keywords: Iterable[MdKeywordsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "descriptiveKeywords",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_specific_usage: Iterable[MdUsagePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceSpecificUsage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_constraints: Iterable[MdConstraintsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    aggregation_info: Iterable[MdAggregateInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "aggregationInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
