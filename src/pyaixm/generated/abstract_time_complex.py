from dataclasses import dataclass

from pyaixm.generated.abstract_time_complex_type import AbstractTimeComplexType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeComplex(AbstractTimeComplexType):
    """
    Gml:AbstractTimeComplex is an aggregation of temporal primitives and acts as
    the head of a substitution group for temporal complexes.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
