from dataclasses import dataclass

from pyaixm.generated.special_date_extension_type import (
    SpecialDateExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SpecialDateExtension(SpecialDateExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
