from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_distance_indication_type import (
    CodeDistanceIndicationType,
)
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.distance_indication_time_slice_type_extension import (
    DistanceIndicationTimeSliceTypeExtension,
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
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DistanceIndicationTimeSliceType(AbstractAixmtimeSliceType):
    distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
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
    type_value: Optional[CodeDistanceIndicationType] = field(
        default=None,
        metadata={
            "name": "type",
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
    extension: Iterable[DistanceIndicationTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
