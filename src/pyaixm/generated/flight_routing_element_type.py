from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.aerial_refuelling_property_type import (
    AerialRefuellingPropertyType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.airspace_property_type import AirspacePropertyType
from pyaixm.generated.code_comparison_type import CodeComparisonType
from pyaixm.generated.code_speed_reference_type import CodeSpeedReferenceType
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.direct_flight_segment_property_type import (
    DirectFlightSegmentPropertyType,
)
from pyaixm.generated.flight_restriction_level_property_type import (
    FlightRestrictionLevelPropertyType,
)
from pyaixm.generated.flight_routing_element_type_extension import (
    FlightRoutingElementTypeExtension,
)
from pyaixm.generated.navaid_property_type import NavaidPropertyType
from pyaixm.generated.no_sequence_type import NoSequenceType
from pyaixm.generated.note_property_type import NotePropertyType
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
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)
from pyaixm.generated.val_speed_type import ValSpeedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRoutingElementType(AbstractAixmobjectType):
    order_number: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "orderNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed: Optional[ValSpeedType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed_reference: Optional[CodeSpeedReferenceType] = field(
        default=None,
        metadata={
            "name": "speedReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed_criteria: Optional[CodeComparisonType] = field(
        default=None,
        metadata={
            "name": "speedCriteria",
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
    element_standard_instrument_arrival_element: Optional[
        StandardInstrumentArrivalPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "element_standardInstrumentArrivalElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element_airspace_element: Optional[AirspacePropertyType] = field(
        default=None,
        metadata={
            "name": "element_airspaceElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_element_fix_designated_point: Optional[
        DesignatedPointPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "pointElement_fixDesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_element_navaid_system: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "pointElement_navaidSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_element_aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "pointElement_aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_element_runway_point: Optional[RunwayCentrelinePointPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "pointElement_runwayPoint",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    point_element_airport_reference_point: Optional[
        AirportHeliportPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "pointElement_airportReferencePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_element_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "name": "pointElement_position",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element_direct_flight_element: Optional[
        DirectFlightSegmentPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "element_directFlightElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element_standard_instrument_departure_element: Optional[
        StandardInstrumentDeparturePropertyType
    ] = field(
        default=None,
        metadata={
            "name": "element_standardInstrumentDepartureElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element_route_portion_element: Optional[RoutePortionPropertyType] = field(
        default=None,
        metadata={
            "name": "element_routePortionElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element_airport_heliport_element: Optional[AirportHeliportPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "element_airportHeliportElement",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    element_aerial_refuelling_element: Optional[
        AerialRefuellingPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "element_aerialRefuellingElement",
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
    extension: Iterable[FlightRoutingElementTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
