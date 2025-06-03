from dataclasses import dataclass

from generated.feature_property_type import AbstractFeatureCollectionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractFeatureCollection(AbstractFeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
