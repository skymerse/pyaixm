from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_segment_point_type import (
    AbstractSegmentPointType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_atcreporting_type import CodeAtcreportingType
from pyaixm.generated.code_free_flight_type import CodeFreeFlightType
from pyaixm.generated.code_military_route_point_type import (
    CodeMilitaryRoutePointType,
)
from pyaixm.generated.code_rvsmpoint_role_type import CodeRvsmpointRoleType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.en_route_segment_point_type_extension import (
    EnRouteSegmentPointTypeExtension,
)
from pyaixm.generated.navaid_property_type import NavaidPropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.point_property_type_2 import PointPropertyType2
from pyaixm.generated.point_reference_property_type import (
    PointReferencePropertyType,
)
from pyaixm.generated.radio_frequency_area_property_type import (
    RadioFrequencyAreaPropertyType,
)
from pyaixm.generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EnRouteSegmentPointType(AbstractSegmentPointType):
    reporting_atc: Optional[CodeAtcreportingType] = field(
        default=None,
        metadata={
            "name": "reportingATC",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    fly_over: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "flyOver",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    waypoint: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    radar_guidance: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "radarGuidance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    facility_makeup: Iterable[PointReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "facilityMakeup",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_choice_fix_designated_point: Optional[
        DesignatedPointPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "pointChoice_fixDesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_choice_navaid_system: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "pointChoice_navaidSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_choice_aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "pointChoice_aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_choice_runway_point: Optional[RunwayCentrelinePointPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "pointChoice_runwayPoint",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    point_choice_airport_reference_point: Optional[
        AirportHeliportPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "pointChoice_airportReferencePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point_choice_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "name": "pointChoice_position",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extended_service_volume: Optional[RadioFrequencyAreaPropertyType] = field(
        default=None,
        metadata={
            "name": "extendedServiceVolume",
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
    role_free_flight: Optional[CodeFreeFlightType] = field(
        default=None,
        metadata={
            "name": "roleFreeFlight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    role_rvsm: Optional[CodeRvsmpointRoleType] = field(
        default=None,
        metadata={
            "name": "roleRVSM",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    turn_radius: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "turnRadius",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    role_military_training: Optional[CodeMilitaryRoutePointType] = field(
        default=None,
        metadata={
            "name": "roleMilitaryTraining",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[EnRouteSegmentPointTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
