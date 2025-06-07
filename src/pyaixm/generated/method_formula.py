from dataclasses import dataclass

from generated.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MethodFormula(CodeType):
    class Meta:
        name = "methodFormula"
        namespace = "http://www.opengis.net/gml/3.2"
