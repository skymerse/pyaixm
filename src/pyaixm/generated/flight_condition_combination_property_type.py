from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)
from pyaixm.generated.aerial_refuelling_property_type import (
    AerialRefuellingPropertyType,
)
from pyaixm.generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.airspace_border_crossing_property_type import (
    AirspaceBorderCrossingPropertyType,
)
from pyaixm.generated.airspace_property_type import AirspacePropertyType
from pyaixm.generated.code_flow_condition_operation_type import (
    CodeFlowConditionOperationType,
)
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.direct_flight_property_type import (
    DirectFlightPropertyType,
)
from pyaixm.generated.flight_characteristic_property_type import (
    FlightCharacteristicPropertyType,
)
from pyaixm.generated.flight_condition_circumstance_property_type import (
    FlightConditionCircumstancePropertyType,
)
from pyaixm.generated.flight_condition_combination_type_extension import (
    FlightConditionCombinationTypeExtension,
)
from pyaixm.generated.flight_condition_element_type_extension import (
    FlightConditionElementTypeExtension,
)
from pyaixm.generated.flight_restriction_level_property_type import (
    FlightRestrictionLevelPropertyType,
)
from pyaixm.generated.meteorology_property_type import MeteorologyPropertyType
from pyaixm.generated.navaid_property_type import NavaidPropertyType
from pyaixm.generated.no_sequence_type import NoSequenceType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from pyaixm.generated.point_property_type_2 import PointPropertyType2
from pyaixm.generated.route_portion_property_type import (
    RoutePortionPropertyType,
)
from pyaixm.generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from pyaixm.generated.standard_instrument_arrival_property_type import (
    StandardInstrumentArrivalPropertyType,
)
from pyaixm.generated.standard_instrument_departure_property_type import (
    StandardInstrumentDeparturePropertyType,
)
from pyaixm.generated.timesheet_property_type import TimesheetPropertyType
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightConditionCombinationPropertyType(AbstractAixmpropertyType):
    flight_condition_combination: Optional["FlightConditionCombination"] = (
        field(
            default=None,
            metadata={
                "name": "FlightConditionCombination",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )


@dataclass
class FlightConditionElementType(AbstractAixmobjectType):
    index: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_airport_heliport_condition: Optional[
        AirportHeliportPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_airportHeliportCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_standard_instrument_departure_condition: Optional[
        StandardInstrumentDeparturePropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_standardInstrumentDepartureCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_route_portion_condition: Optional[
        RoutePortionPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_routePortionCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_organisation_condition: Optional[
        OrganisationAuthorityPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_organisationCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    significant_point_condition_fix_designated_point: Optional[
        DesignatedPointPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "significantPointCondition_fixDesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    significant_point_condition_navaid_system: Optional[NavaidPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "significantPointCondition_navaidSystem",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    significant_point_condition_aiming_point: Optional[
        TouchDownLiftOffPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "significantPointCondition_aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    significant_point_condition_runway_point: Optional[
        RunwayCentrelinePointPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "significantPointCondition_runwayPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    significant_point_condition_airport_reference_point: Optional[
        AirportHeliportPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "significantPointCondition_airportReferencePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    significant_point_condition_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "name": "significantPointCondition_position",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_direct_flight_condition: Optional[
        DirectFlightPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_directFlightCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_aircraft: Optional[AircraftCharacteristicPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "flightCondition_aircraft",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    flight_condition_border_crossing_condition: Optional[
        AirspaceBorderCrossingPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_borderCrossingCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_airspace_condition: Optional[AirspacePropertyType] = (
        field(
            default=None,
            metadata={
                "name": "flightCondition_airspaceCondition",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    flight_condition_flight: Optional[FlightCharacteristicPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "flightCondition_flight",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    flight_condition_standard_instrument_arrival_condition: Optional[
        StandardInstrumentArrivalPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_standardInstrumentArrivalCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_operand: Optional[
        FlightConditionCombinationPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_operand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_weather: Optional[MeteorologyPropertyType] = field(
        default=None,
        metadata={
            "name": "flightCondition_weather",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_condition_aerial_refuelling_condition: Optional[
        AerialRefuellingPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "flightCondition_aerialRefuellingCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    operational_condition: Optional[
        FlightConditionCircumstancePropertyType
    ] = field(
        default=None,
        metadata={
            "name": "operationalCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_level: Iterable[FlightRestrictionLevelPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "flightLevel",
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
    extension: Iterable[FlightConditionElementTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )


@dataclass
class FlightConditionElement(FlightConditionElementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightConditionElementPropertyType(AbstractAixmpropertyType):
    flight_condition_element: Optional[FlightConditionElement] = field(
        default=None,
        metadata={
            "name": "FlightConditionElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )


@dataclass
class FlightConditionCombinationType(AbstractPropertiesWithScheduleType):
    time_interval: Iterable[TimesheetPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeInterval",
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
    special_date_authority: Iterable[OrganisationAuthorityPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "specialDateAuthority",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    logical_operator: Optional[CodeFlowConditionOperationType] = field(
        default=None,
        metadata={
            "name": "logicalOperator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element: Iterable[FlightConditionElementPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[FlightConditionCombinationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )


@dataclass
class FlightConditionCombination(FlightConditionCombinationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
