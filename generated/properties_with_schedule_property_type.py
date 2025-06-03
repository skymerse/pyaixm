from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.airport_heliport_availability import AirportHeliportAvailability
from generated.airport_heliport_responsibility_organisation import (
    AirportHeliportResponsibilityOrganisation,
)
from generated.airspace_activation import AirspaceActivation
from generated.airspace_layer_class import AirspaceLayerClass
from generated.altimeter_source_status import AltimeterSourceStatus
from generated.apron_area_availability import ApronAreaAvailability
from generated.circling_restriction import CirclingRestriction
from generated.condition_combination_property_type import ConditionCombination
from generated.flight_condition_combination_property_type import (
    FlightConditionCombination,
)
from generated.ground_lighting_availability import GroundLightingAvailability
from generated.light_element_status import LightElementStatus
from generated.manoeuvring_area_availability import ManoeuvringAreaAvailability
from generated.navaid_equipment_monitoring import NavaidEquipmentMonitoring
from generated.navaid_operational_status import NavaidOperationalStatus
from generated.online_contact import OnlineContact
from generated.postal_address import PostalAddress
from generated.procedure_availability import ProcedureAvailability
from generated.radio_communication_operational_status import (
    RadioCommunicationOperationalStatus,
)
from generated.route_availability import RouteAvailability
from generated.runway_declared_distance_value import (
    RunwayDeclaredDistanceValue,
)
from generated.service_operational_status import ServiceOperationalStatus
from generated.special_navigation_station_status import (
    SpecialNavigationStationStatus,
)
from generated.telephone_contact import TelephoneContact
from generated.unit_availability import UnitAvailability
from generated.vertical_structure_lighting_status import (
    VerticalStructureLightingStatus,
)
from generated.vertical_structure_part import VerticalStructurePart
from generated.workarea_activity import WorkareaActivity

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PropertiesWithSchedulePropertyType(AbstractAixmpropertyType):
    route_availability: Optional[RouteAvailability] = field(
        default=None,
        metadata={
            "name": "RouteAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    flight_condition_combination: Optional[FlightConditionCombination] = field(
        default=None,
        metadata={
            "name": "FlightConditionCombination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    procedure_availability: Optional[ProcedureAvailability] = field(
        default=None,
        metadata={
            "name": "ProcedureAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    circling_restriction: Optional[CirclingRestriction] = field(
        default=None,
        metadata={
            "name": "CirclingRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vertical_structure_lighting_status: Optional[
        VerticalStructureLightingStatus
    ] = field(
        default=None,
        metadata={
            "name": "VerticalStructureLightingStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    vertical_structure_part: Optional[VerticalStructurePart] = field(
        default=None,
        metadata={
            "name": "VerticalStructurePart",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    unit_availability: Optional[UnitAvailability] = field(
        default=None,
        metadata={
            "name": "UnitAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    special_navigation_station_status: Optional[
        SpecialNavigationStationStatus
    ] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationStationStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navaid_equipment_monitoring: Optional[NavaidEquipmentMonitoring] = field(
        default=None,
        metadata={
            "name": "NavaidEquipmentMonitoring",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    navaid_operational_status: Optional[NavaidOperationalStatus] = field(
        default=None,
        metadata={
            "name": "NavaidOperationalStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    radio_communication_operational_status: Optional[
        RadioCommunicationOperationalStatus
    ] = field(
        default=None,
        metadata={
            "name": "RadioCommunicationOperationalStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    service_operational_status: Optional[ServiceOperationalStatus] = field(
        default=None,
        metadata={
            "name": "ServiceOperationalStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    light_element_status: Optional[LightElementStatus] = field(
        default=None,
        metadata={
            "name": "LightElementStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    telephone_contact: Optional[TelephoneContact] = field(
        default=None,
        metadata={
            "name": "TelephoneContact",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    online_contact: Optional[OnlineContact] = field(
        default=None,
        metadata={
            "name": "OnlineContact",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace_layer_class: Optional[AirspaceLayerClass] = field(
        default=None,
        metadata={
            "name": "AirspaceLayerClass",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airspace_activation: Optional[AirspaceActivation] = field(
        default=None,
        metadata={
            "name": "AirspaceActivation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_availability: Optional[AirportHeliportAvailability] = (
        field(
            default=None,
            metadata={
                "name": "AirportHeliportAvailability",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    condition_combination: Optional[ConditionCombination] = field(
        default=None,
        metadata={
            "name": "ConditionCombination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    workarea_activity: Optional[WorkareaActivity] = field(
        default=None,
        metadata={
            "name": "WorkareaActivity",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    altimeter_source_status: Optional[AltimeterSourceStatus] = field(
        default=None,
        metadata={
            "name": "AltimeterSourceStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    airport_heliport_responsibility_organisation: Optional[
        AirportHeliportResponsibilityOrganisation
    ] = field(
        default=None,
        metadata={
            "name": "AirportHeliportResponsibilityOrganisation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    ground_lighting_availability: Optional[GroundLightingAvailability] = field(
        default=None,
        metadata={
            "name": "GroundLightingAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    apron_area_availability: Optional[ApronAreaAvailability] = field(
        default=None,
        metadata={
            "name": "ApronAreaAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    manoeuvring_area_availability: Optional[ManoeuvringAreaAvailability] = (
        field(
            default=None,
            metadata={
                "name": "ManoeuvringAreaAvailability",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
    runway_declared_distance_value: Optional[RunwayDeclaredDistanceValue] = (
        field(
            default=None,
            metadata={
                "name": "RunwayDeclaredDistanceValue",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
