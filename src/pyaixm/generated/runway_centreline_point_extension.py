from dataclasses import dataclass

from pyaixm.generated.runway_centreline_point_extension_type import (
    RunwayCentrelinePointExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayCentrelinePointExtension(RunwayCentrelinePointExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
