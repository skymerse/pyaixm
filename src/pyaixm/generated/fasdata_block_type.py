from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.fasdata_block_type_extension import (
    FasdataBlockTypeExtension,
)
from pyaixm.generated.no_sequence_type import NoSequenceType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_alarm_limit_type import ValAlarmLimitType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_hex_type import ValHexType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FasdataBlockType(AbstractAixmobjectType):
    class Meta:
        name = "FASDataBlockType"

    horizontal_alarm_limit: Optional[ValAlarmLimitType] = field(
        default=None,
        metadata={
            "name": "horizontalAlarmLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_alarm_limit: Optional[ValAlarmLimitType] = field(
        default=None,
        metadata={
            "name": "verticalAlarmLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    threshold_course_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "thresholdCourseWidth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    length_offset: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "lengthOffset",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    crcremainder: Optional[ValHexType] = field(
        default=None,
        metadata={
            "name": "CRCRemainder",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    operation_type: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "operationType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    service_provider_sbas: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "serviceProviderSBAS",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    approach_performance_designator: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "approachPerformanceDesignator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    route_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "routeIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "pattern": r"[A-Z]*",
        },
    )
    reference_path_data_selector: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "referencePathDataSelector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    reference_path_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "referencePathIdentifier",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "pattern": r"([A-Z]|\d)*",
        },
    )
    code_icao: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeICAO",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "pattern": r"([A-Z]|\d)*",
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
    extension: Iterable[FasdataBlockTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
