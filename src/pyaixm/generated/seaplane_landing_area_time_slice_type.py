from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from generated.floating_dock_site_property_type import (
    FloatingDockSitePropertyType,
)
from generated.manoeuvring_area_availability_property_type import (
    ManoeuvringAreaAvailabilityPropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.seaplane_landing_area_time_slice_type_extension import (
    SeaplaneLandingAreaTimeSliceTypeExtension,
)
from generated.seaplane_ramp_site_property_type import (
    SeaplaneRampSitePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneLandingAreaTimeSliceType(AbstractAixmtimeSliceType):
    ramp_site: Iterable[SeaplaneRampSitePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "rampSite",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    dock_site: Iterable[FloatingDockSitePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dockSite",
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
    extension: Iterable[SeaplaneLandingAreaTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
