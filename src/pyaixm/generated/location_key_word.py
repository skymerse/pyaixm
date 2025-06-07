from dataclasses import dataclass

from generated.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LocationKeyWord(CodeType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
