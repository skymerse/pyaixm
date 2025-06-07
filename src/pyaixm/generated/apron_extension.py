from dataclasses import dataclass

from generated.apron_extension_type import ApronExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ApronExtension(ApronExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
