from dataclasses import dataclass

from generated.value_array_property_type import ValuePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ValueProperty(ValuePropertyType):
    """Property that refers to, or contains, a Value.

    Convenience element for general use.
    """

    class Meta:
        name = "valueProperty"
        namespace = "http://www.opengis.net/gml/3.2"
