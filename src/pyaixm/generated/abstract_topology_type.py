from dataclasses import dataclass

from pyaixm.generated.abstract_gmltype import AbstractGmltype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTopologyType(AbstractGmltype):
    """This abstract type supplies the root or base type for all topological
    elements including primitives and complexes.

    It inherits AbstractGMLType and hence can be identified using the
    gml:id attribute.
    """
