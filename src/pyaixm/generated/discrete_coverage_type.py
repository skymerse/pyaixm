from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_coverage_type import AbstractCoverageType
from pyaixm.generated.coverage_function import CoverageFunction

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DiscreteCoverageType(AbstractCoverageType):
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
