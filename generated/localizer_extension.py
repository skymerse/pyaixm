from dataclasses import dataclass

from generated.localizer_extension_type import LocalizerExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class LocalizerExtension(LocalizerExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
