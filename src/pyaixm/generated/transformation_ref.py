from dataclasses import dataclass

from generated.transformation_property_type import TransformationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TransformationRef(TransformationPropertyType):
    class Meta:
        name = "transformationRef"
        namespace = "http://www.opengis.net/gml/3.2"
