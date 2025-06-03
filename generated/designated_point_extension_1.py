from dataclasses import dataclass

from generated.designated_point_extension_type_1 import (
    DesignatedPointExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class DesignatedPointExtension1(DesignatedPointExtensionType1):
    class Meta:
        name = "DesignatedPointExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
