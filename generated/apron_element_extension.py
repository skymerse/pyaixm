from dataclasses import dataclass

from generated.apron_element_extension_type import ApronElementExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ApronElementExtension(ApronElementExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
