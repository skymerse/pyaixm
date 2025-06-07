from dataclasses import dataclass

from pyaixm.generated.apron_marking_extension_type_1 import (
    ApronMarkingExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ApronMarkingExtension1(ApronMarkingExtensionType1):
    class Meta:
        name = "ApronMarkingExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
