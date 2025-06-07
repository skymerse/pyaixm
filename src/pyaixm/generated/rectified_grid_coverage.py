from dataclasses import dataclass

from pyaixm.generated.discrete_coverage_type import DiscreteCoverageType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RectifiedGridCoverage(DiscreteCoverageType):
    """The gml:RectifiedGridCoverage is a discrete point coverage based on a
    rectified grid.

    It is similar to the grid coverage except that the points of the
    grid are geometrically referenced. The rectified grid coverage has a
    domain that is a gml:RectifiedGrid geometry.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
