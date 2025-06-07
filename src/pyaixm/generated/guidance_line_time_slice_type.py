from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.aircraft_stand_property_type import (
    AircraftStandPropertyType,
)
from pyaixm.generated.apron_property_type import ApronPropertyType
from pyaixm.generated.code_direction_type import CodeDirectionType
from pyaixm.generated.code_guidance_line_type import CodeGuidanceLineType
from pyaixm.generated.elevated_curve_property_type import (
    ElevatedCurvePropertyType,
)
from pyaixm.generated.guidance_line_time_slice_type_extension import (
    GuidanceLineTimeSliceTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from pyaixm.generated.taxiway_property_type import TaxiwayPropertyType
from pyaixm.generated.text_name_type import TextNameType
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)
from pyaixm.generated.val_speed_type import ValSpeedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeGuidanceLineType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    max_speed: Optional[ValSpeedType] = field(
        default=None,
        metadata={
            "name": "maxSpeed",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    usage_direction: Optional[CodeDirectionType] = field(
        default=None,
        metadata={
            "name": "usageDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    connected_touch_down_lift_off: Iterable[TouchDownLiftOffPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "connectedTouchDownLiftOff",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    connected_runway_centreline_point: Iterable[
        RunwayCentrelinePointPropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "connectedRunwayCentrelinePoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    connected_apron: Iterable[ApronPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "connectedApron",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    connected_stand: Iterable[AircraftStandPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "connectedStand",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent: Optional[ElevatedCurvePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    connected_taxiway: Iterable[TaxiwayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "connectedTaxiway",
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
    extension: Iterable[GuidanceLineTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
