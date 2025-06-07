from dataclasses import dataclass

from pyaixm.generated.generic_meta_data_type import GenericMetaDataType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GenericMetaData(GenericMetaDataType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
