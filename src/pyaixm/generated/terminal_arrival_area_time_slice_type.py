from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_taatype import CodeTaatype
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.instrument_approach_procedure_property_type import (
    InstrumentApproachProcedurePropertyType,
)
from pyaixm.generated.navaid_property_type import NavaidPropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.point_property_type_2 import PointPropertyType2
from pyaixm.generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from pyaixm.generated.surface_property_type_2 import SurfacePropertyType2
from pyaixm.generated.terminal_arrival_area_sector_property_type import (
    TerminalArrivalAreaSectorPropertyType,
)
from pyaixm.generated.terminal_arrival_area_time_slice_type_extension import (
    TerminalArrivalAreaTimeSliceTypeExtension,
)
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalAreaTimeSliceType(AbstractAixmtimeSliceType):
    arrival_area_type: Optional[CodeTaatype] = field(
        default=None,
        metadata={
            "name": "arrivalAreaType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outer_buffer_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "outerBufferWidth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lateral_buffer_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "lateralBufferWidth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    if_fix_designated_point: Optional[DesignatedPointPropertyType] = field(
        default=None,
        metadata={
            "name": "IF_fixDesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    if_navaid_system: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "IF_navaidSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    if_aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "IF_aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    if_runway_point: Optional[RunwayCentrelinePointPropertyType] = field(
        default=None,
        metadata={
            "name": "IF_runwayPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    if_airport_reference_point: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "IF_airportReferencePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    if_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "name": "IF_position",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    iaf_fix_designated_point: Optional[DesignatedPointPropertyType] = field(
        default=None,
        metadata={
            "name": "IAF_fixDesignatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    iaf_navaid_system: Optional[NavaidPropertyType] = field(
        default=None,
        metadata={
            "name": "IAF_navaidSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    iaf_aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "IAF_aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    iaf_runway_point: Optional[RunwayCentrelinePointPropertyType] = field(
        default=None,
        metadata={
            "name": "IAF_runwayPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    iaf_airport_reference_point: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "IAF_airportReferencePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    iaf_position: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "name": "IAF_position",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    buffer: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    sector: Iterable[TerminalArrivalAreaSectorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    approach_rnav: Optional[InstrumentApproachProcedurePropertyType] = field(
        default=None,
        metadata={
            "name": "approachRNAV",
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
    extension: Iterable[TerminalArrivalAreaTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
