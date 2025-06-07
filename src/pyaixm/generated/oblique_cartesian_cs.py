from dataclasses import dataclass

from pyaixm.generated.oblique_cartesian_cstype import ObliqueCartesianCstype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ObliqueCartesianCs(ObliqueCartesianCstype):
    class Meta:
        name = "ObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"
