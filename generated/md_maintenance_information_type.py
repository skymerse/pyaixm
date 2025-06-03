from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_object_type import AbstractObjectType
from generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from generated.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from generated.date_property_type import DatePropertyType
from generated.md_maintenance_frequency_code_property_type import (
    MdMaintenanceFrequencyCodePropertyType,
)
from generated.md_scope_code_property_type import MdScopeCodePropertyType
from generated.md_scope_description_property_type import (
    MdScopeDescriptionPropertyType,
)
from generated.tm_period_duration_property_type import (
    TmPeriodDurationPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceInformationType(AbstractObjectType):
    """
    Information about the scope and frequency of updating.
    """

    class Meta:
        name = "MD_MaintenanceInformation_Type"

    maintenance_and_update_frequency: Optional[
        MdMaintenanceFrequencyCodePropertyType
    ] = field(
        default=None,
        metadata={
            "name": "maintenanceAndUpdateFrequency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    date_of_next_update: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "name": "dateOfNextUpdate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    user_defined_maintenance_frequency: Optional[
        TmPeriodDurationPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "userDefinedMaintenanceFrequency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    update_scope: Iterable[MdScopeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScope",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    update_scope_description: Iterable[MdScopeDescriptionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScopeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    maintenance_note: Iterable[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    contact: Iterable[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
