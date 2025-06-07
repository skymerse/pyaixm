from dataclasses import dataclass

from pyaixm.generated.datum_property_type import DatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DatumRef(DatumPropertyType):
    class Meta:
        name = "datumRef"
        namespace = "http://www.opengis.net/gml/3.2"
