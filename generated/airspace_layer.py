from dataclasses import dataclass

from generated.airspace_layer_type import AirspaceLayerType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceLayer(AirspaceLayerType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
