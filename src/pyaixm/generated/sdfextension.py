from dataclasses import dataclass

from pyaixm.generated.sdfextension_type import SdfextensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Sdfextension(SdfextensionType):
    class Meta:
        name = "SDFExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
