from dataclasses import dataclass

from generated.abstract_ground_light_system_type import (
    AbstractGroundLightSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractGroundLightSystem(AbstractGroundLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
