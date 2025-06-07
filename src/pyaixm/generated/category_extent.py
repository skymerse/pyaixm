from dataclasses import dataclass

from generated.category_extent_type import CategoryExtentType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CategoryExtent(CategoryExtentType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
