from dataclasses import dataclass

from pyaixm.generated.glidepath_extension_type import GlidepathExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class GlidepathExtension(GlidepathExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
