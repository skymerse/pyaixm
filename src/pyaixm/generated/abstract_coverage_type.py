from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_feature_type import AbstractFeatureType
from generated.domain_set import DomainSet
from generated.grid_domain import GridDomain
from generated.multi_curve_domain import MultiCurveDomain
from generated.multi_point_domain import MultiPointDomain
from generated.multi_solid_domain import MultiSolidDomain
from generated.multi_surface_domain import MultiSurfaceDomain
from generated.range_set import RangeSet
from generated.rectified_grid_domain import RectifiedGridDomain

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoverageType(AbstractFeatureType):
    """The base type for coverages is gml:AbstractCoverageType.

    The basic elements of a coverage can be seen in this content model: the coverage contains gml:domainSet and gml:rangeSet properties. The gml:domainSet property describes the domain of the coverage and the gml:rangeSet property describes the range of the coverage.
    """

    rectified_grid_domain: Optional[RectifiedGridDomain] = field(
        default=None,
        metadata={
            "name": "rectifiedGridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_domain: Optional[GridDomain] = field(
        default=None,
        metadata={
            "name": "gridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid_domain: Optional[MultiSolidDomain] = field(
        default=None,
        metadata={
            "name": "multiSolidDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface_domain: Optional[MultiSurfaceDomain] = field(
        default=None,
        metadata={
            "name": "multiSurfaceDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve_domain: Optional[MultiCurveDomain] = field(
        default=None,
        metadata={
            "name": "multiCurveDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point_domain: Optional[MultiPointDomain] = field(
        default=None,
        metadata={
            "name": "multiPointDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    domain_set: Optional[DomainSet] = field(
        default=None,
        metadata={
            "name": "domainSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    range_set: Optional[RangeSet] = field(
        default=None,
        metadata={
            "name": "rangeSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
