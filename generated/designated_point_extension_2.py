from dataclasses import dataclass

from generated.designated_point_extension_type_2 import (
    DesignatedPointExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class DesignatedPointExtension2(DesignatedPointExtensionType2):
    class Meta:
        name = "DesignatedPointExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
