from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.airspace_property_type import AirspacePropertyType
from pyaixm.generated.code_airspace_point_position_type import (
    CodeAirspacePointPositionType,
)
from pyaixm.generated.code_airspace_point_role_type import (
    CodeAirspacePointRoleType,
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
from pyaixm.generated.significant_point_in_airspace_time_slice_type_extension import (
    SignificantPointInAirspaceTimeSliceTypeExtension,
)
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SignificantPointInAirspaceTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeAirspacePointRoleType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    relative_location: Optional[CodeAirspacePointPositionType] = field(
        default=None,
        metadata={
            "name": "relativeLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    containing_airspace: Optional[AirspacePropertyType] = field(
        default=None,
        metadata={
            "name": "containingAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location_fix_designated_point: Optional[DesignatedPointPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "location_fixDesignatedPoint",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    location_navaid_system: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "location_navaidSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location_aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "location_aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location_runway_point: Optional[RunwayCentrelinePointPropertyType] = field(
        default=None,
        metadata={
            "name": "location_runwayPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location_airport_reference_point: Optional[AirportHeliportPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "location_airportReferencePoint",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    location_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
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
    extension: Iterable[SignificantPointInAirspaceTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
