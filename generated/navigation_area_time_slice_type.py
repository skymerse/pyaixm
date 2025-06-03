from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.code_navigation_area_type import CodeNavigationAreaType
from generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from generated.navaid_property_type import NavaidPropertyType
from generated.navigation_area_sector_property_type import (
    NavigationAreaSectorPropertyType,
)
from generated.navigation_area_time_slice_type_extension import (
    NavigationAreaTimeSliceTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.point_property_type_2 import PointPropertyType2
from generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from generated.standard_instrument_departure_property_type import (
    StandardInstrumentDeparturePropertyType,
)
from generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaTimeSliceType(AbstractAixmtimeSliceType):
    navigation_area_type: Optional[CodeNavigationAreaType] = field(
        default=None,
        metadata={
            "name": "navigationAreaType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_ceiling: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "minimumCeiling",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_visibility: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "minimumVisibility",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    departure: Optional[StandardInstrumentDeparturePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    sector: Iterable[NavigationAreaSectorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    centre_point_fix_designated_point: Optional[
        DesignatedPointPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "centrePoint_fixDesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    centre_point_navaid_system: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "centrePoint_navaidSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    centre_point_aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "centrePoint_aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    centre_point_runway_point: Optional[RunwayCentrelinePointPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "centrePoint_runwayPoint",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    centre_point_airport_reference_point: Optional[
        AirportHeliportPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "centrePoint_airportReferencePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    centre_point_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "name": "centrePoint_position",
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
    extension: Iterable[NavigationAreaTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
