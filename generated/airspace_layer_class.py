from dataclasses import dataclass

from generated.airspace_layer_class_type import AirspaceLayerClassType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceLayerClass(AirspaceLayerClassType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
