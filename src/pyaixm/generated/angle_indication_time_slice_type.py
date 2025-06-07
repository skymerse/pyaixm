from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.angle_indication_time_slice_type_extension import (
    AngleIndicationTimeSliceTypeExtension,
)
from pyaixm.generated.code_bearing_type import CodeBearingType
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.code_direction_reference_type import (
    CodeDirectionReferenceType,
)
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.navaid_property_type import NavaidPropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.point_property_type_2 import PointPropertyType2
from pyaixm.generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)
from pyaixm.generated.val_bearing_type import ValBearingType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleIndicationTimeSliceType(AbstractAixmtimeSliceType):
    angle: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_type: Optional[CodeBearingType] = field(
        default=None,
        metadata={
            "name": "angleType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    indication_direction: Optional[CodeDirectionReferenceType] = field(
        default=None,
        metadata={
            "name": "indicationDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    true_angle: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "trueAngle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_reception_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "minimumReceptionAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    fix: Optional[DesignatedPointPropertyType] = field(
        default=None,
        metadata={
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
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[AngleIndicationTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
