from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.notamtranslation import Notamtranslation

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NotamtranslationPropertyType(AbstractAixmpropertyType):
    class Meta:
        name = "NOTAMTranslationPropertyType"

    notamtranslation: Optional[Notamtranslation] = field(
        default=None,
        metadata={
            "name": "NOTAMTranslation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "required": True,
        },
    )
