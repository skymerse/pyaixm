from dataclasses import dataclass, field
from typing import Optional

from generated.coverage_mapping_rule import CoverageMappingRule
from generated.grid_function import GridFunction
from generated.mapping_rule import MappingRule

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoverageFunctionType:
    mapping_rule: Optional[MappingRule] = field(
        default=None,
        metadata={
            "name": "MappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coverage_mapping_rule: Optional[CoverageMappingRule] = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_function: Optional[GridFunction] = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
