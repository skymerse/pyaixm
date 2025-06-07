from dataclasses import dataclass

from pyaixm.generated.seaplane_landing_area_extension_type import (
    SeaplaneLandingAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SeaplaneLandingAreaExtension(SeaplaneLandingAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
