from dataclasses import dataclass

from pyaixm.generated.abstract_curve_type import AbstractCurveType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCurve(AbstractCurveType):
    """
    The AbstractCurve element is the abstract head of the substitution group for
    all (continuous) curve elements.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
