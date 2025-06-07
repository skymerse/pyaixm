from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.code_course_quality_ilstype import CodeCourseQualityIlstype
from generated.code_integrity_level_ilstype import CodeIntegrityLevelIlstype
from generated.code_navaid_designator_type import CodeNavaidDesignatorType
from generated.code_navaid_purpose_type import CodeNavaidPurposeType
from generated.code_navaid_service_type import CodeNavaidServiceType
from generated.code_signal_performance_ilstype import (
    CodeSignalPerformanceIlstype,
)
from generated.code_yes_no_type import CodeYesNoType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.navaid_component_property_type import (
    NavaidComponentPropertyType,
)
from generated.navaid_operational_status_property_type import (
    NavaidOperationalStatusPropertyType,
)
from generated.navaid_time_slice_type_extension import (
    NavaidTimeSliceTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from generated.text_name_type import TextNameType
from generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeNavaidServiceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator: Optional[CodeNavaidDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    flight_checked: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "flightChecked",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    purpose: Optional[CodeNavaidPurposeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    signal_performance: Optional[CodeSignalPerformanceIlstype] = field(
        default=None,
        metadata={
            "name": "signalPerformance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    course_quality: Optional[CodeCourseQualityIlstype] = field(
        default=None,
        metadata={
            "name": "courseQuality",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    integrity_level: Optional[CodeIntegrityLevelIlstype] = field(
        default=None,
        metadata={
            "name": "integrityLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    touch_down_lift_off: Iterable[TouchDownLiftOffPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "touchDownLiftOff",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    navaid_equipment: Iterable[NavaidComponentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "navaidEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    runway_direction: Iterable[RunwayDirectionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "runwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    served_airport: Iterable[AirportHeliportPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "servedAirport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[NavaidOperationalStatusPropertyType] = field(
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
    extension: Iterable[NavaidTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
