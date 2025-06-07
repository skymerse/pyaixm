from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_helicopter_performance_type import (
    CodeHelicopterPerformanceType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.manoeuvring_area_availability_property_type import (
    ManoeuvringAreaAvailabilityPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.runway_property_type import RunwayPropertyType
from pyaixm.generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from pyaixm.generated.text_designator_type import TextDesignatorType
from pyaixm.generated.touch_down_lift_off_contamination_property_type import (
    TouchDownLiftOffContaminationPropertyType,
)
from pyaixm.generated.touch_down_lift_off_time_slice_type_extension import (
    TouchDownLiftOffTimeSliceTypeExtension,
)
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_slope_type import ValSlopeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    slope: Optional[ValSlopeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    helicopter_class: Optional[CodeHelicopterPerformanceType] = field(
        default=None,
        metadata={
            "name": "helicopterClass",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    abandoned: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aiming_point: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "name": "aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent: Optional[ElevatedSurfacePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surface_properties: Optional[SurfaceCharacteristicsPropertyType] = field(
        default=None,
        metadata={
            "name": "surfaceProperties",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    associated_airport_heliport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedAirportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    approach_take_off_area: Optional[RunwayPropertyType] = field(
        default=None,
        metadata={
            "name": "approachTakeOffArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    contaminant: Iterable[TouchDownLiftOffContaminationPropertyType] = field(
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
    availability: Iterable[ManoeuvringAreaAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TouchDownLiftOffTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
