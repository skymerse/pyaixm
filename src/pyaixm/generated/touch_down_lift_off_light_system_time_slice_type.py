from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_colour_type import CodeColourType
from pyaixm.generated.code_light_intensity_type import CodeLightIntensityType
from pyaixm.generated.code_tlofsection_type import CodeTlofsectionType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.ground_lighting_availability_property_type import (
    GroundLightingAvailabilityPropertyType,
)
from pyaixm.generated.light_element_property_type import (
    LightElementPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.touch_down_lift_off_light_system_time_slice_type_extension import (
    TouchDownLiftOffLightSystemTimeSliceTypeExtension,
)
from pyaixm.generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffLightSystemTimeSliceType(AbstractAixmtimeSliceType):
    emergency_lighting: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "emergencyLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    intensity_level: Optional[CodeLightIntensityType] = field(
        default=None,
        metadata={
            "name": "intensityLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    colour: Optional[CodeColourType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element: Iterable[LightElementPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[GroundLightingAvailabilityPropertyType] = field(
        default_factory=list,
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
    position: Optional[CodeTlofsectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lighted_touch_down_lift_off: Optional[TouchDownLiftOffPropertyType] = (
        field(
            default=None,
            metadata={
                "name": "lightedTouchDownLiftOff",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    extension: Iterable[TouchDownLiftOffLightSystemTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
