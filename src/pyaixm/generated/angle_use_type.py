from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.angle_indication_property_type import (
    AngleIndicationPropertyType,
)
from pyaixm.generated.angle_use_type_extension import AngleUseTypeExtension
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleUseType(AbstractAixmobjectType):
    along_course_guidance: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "alongCourseGuidance",
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
    the_angle_indication: Optional[AngleIndicationPropertyType] = field(
        default=None,
        metadata={
            "name": "theAngleIndication",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[AngleUseTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
