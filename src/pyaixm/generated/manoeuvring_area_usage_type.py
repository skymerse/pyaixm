from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_usage_condition_type import AbstractUsageConditionType
from generated.code_operation_manoeuvring_area_type import (
    CodeOperationManoeuvringAreaType,
)
from generated.code_usage_limitation_type import CodeUsageLimitationType
from generated.condition_combination_property_type import (
    ConditionCombinationPropertyType,
)
from generated.contact_information_property_type import (
    ContactInformationPropertyType,
)
from generated.manoeuvring_area_usage_type_extension import (
    ManoeuvringAreaUsageTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.val_duration_type import ValDurationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ManoeuvringAreaUsageType(AbstractUsageConditionType):
    type_value: Optional[CodeUsageLimitationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    prior_permission: Optional[ValDurationType] = field(
        default=None,
        metadata={
            "name": "priorPermission",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    contact: Iterable[ContactInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    selection: Optional[ConditionCombinationPropertyType] = field(
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
    operation: Optional[CodeOperationManoeuvringAreaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[ManoeuvringAreaUsageTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
