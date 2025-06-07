from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_vertical_structure_type import (
    CodeVerticalStructureType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.ground_light_system_property_type import (
    GroundLightSystemPropertyType,
)
from pyaixm.generated.marker_beacon_property_type import (
    MarkerBeaconPropertyType,
)
from pyaixm.generated.navaid_equipment_property_type import (
    NavaidEquipmentPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from pyaixm.generated.passenger_service_property_type import (
    PassengerServicePropertyType,
)
from pyaixm.generated.service_property_type import ServicePropertyType
from pyaixm.generated.special_navigation_station_property_type import (
    SpecialNavigationStationPropertyType,
)
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.unit_property_type import UnitPropertyType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.vertical_structure_lighting_status_property_type import (
    VerticalStructureLightingStatusPropertyType,
)
from pyaixm.generated.vertical_structure_part_property_type import (
    VerticalStructurePartPropertyType,
)
from pyaixm.generated.vertical_structure_time_slice_type_extension import (
    VerticalStructureTimeSliceTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructureTimeSliceType(AbstractAixmtimeSliceType):
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeVerticalStructureType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lighted: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marking_icaostandard: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "markingICAOStandard",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    group: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    radius: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lighting_icaostandard: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "lightingICAOStandard",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    synchronised_lighting: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "synchronisedLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marker: Optional[MarkerBeaconPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    part: Iterable[VerticalStructurePartPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    hosted_passenger_service: Iterable[PassengerServicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hostedPassengerService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    supported_ground_light: Iterable[GroundLightSystemPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "supportedGroundLight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    hosted_navaid_equipment: Iterable[NavaidEquipmentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hostedNavaidEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    hosted_special_nav_station: Iterable[
        SpecialNavigationStationPropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "hostedSpecialNavStation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    hosted_unit: Iterable[UnitPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hostedUnit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    hosted_organisation: Iterable[OrganisationAuthorityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hostedOrganisation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    supported_service: Iterable[ServicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "supportedService",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lighting_availability: Iterable[
        VerticalStructureLightingStatusPropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "lightingAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[VerticalStructureTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
