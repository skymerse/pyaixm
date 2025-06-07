from dataclasses import dataclass

from pyaixm.generated.direction_finder_extension_type import (
    DirectionFinderExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class DirectionFinderExtension(DirectionFinderExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
