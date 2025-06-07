from dataclasses import dataclass

from generated.marking_extension_type import MarkingExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class MarkingExtension(MarkingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
