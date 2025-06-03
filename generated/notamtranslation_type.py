from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_language_type import CodeLanguageType
from generated.code_notamtranslation_type import CodeNotamtranslationType
from generated.notamtranslation_type_extension import (
    NotamtranslationTypeExtension,
)
from generated.text_notamtype import TextNotamtype
from generated.xhtmltype import Xhtmltype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NotamtranslationType(AbstractAixmobjectType):
    class Meta:
        name = "NOTAMTranslationType"

    type_value: Optional[CodeNotamtranslationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    language: Optional[CodeLanguageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    simple_text: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "simpleText",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    formatted_text: Optional[Xhtmltype] = field(
        default=None,
        metadata={
            "name": "formattedText",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    extension: Iterable[NotamtranslationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
