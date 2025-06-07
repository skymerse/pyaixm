from dataclasses import dataclass

from pyaixm.generated.result_type import ResultType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ResultOf(ResultType):
    class Meta:
        name = "resultOf"
        namespace = "http://www.opengis.net/gml/3.2"
