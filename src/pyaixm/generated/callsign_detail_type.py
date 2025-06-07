from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.callsign_detail_type_extension import (
    CallsignDetailTypeExtension,
)
from pyaixm.generated.code_language_type import CodeLanguageType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CallsignDetailType(AbstractAixmobjectType):
    call_sign: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    language: Optional[CodeLanguageType] = field(
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
    extension: Iterable[CallsignDetailTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
