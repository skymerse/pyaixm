from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.holding_pattern_duration_type_extension import (
    HoldingPatternDurationTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_duration_type import ValDurationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternDurationType(AbstractAixmobjectType):
    duration: Optional[ValDurationType] = field(
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
    extension: Iterable[HoldingPatternDurationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
