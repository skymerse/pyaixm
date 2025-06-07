from dataclasses import dataclass

from pyaixm.generated.event_extension_type import EventExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE"


@dataclass
class EventExtension(EventExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE"
