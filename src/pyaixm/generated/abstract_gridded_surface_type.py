from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_gridded_surface_type_rows_row import (
    AbstractGriddedSurfaceTypeRowsRow,
)
from pyaixm.generated.abstract_parametric_curve_surface_type import (
    AbstractParametricCurveSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    row: Iterable[AbstractGriddedSurfaceTypeRowsRow] = field(
        default_factory=list,
        metadata={
            "wrapper": "rows",
            "name": "Row",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    rows_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "rows",
            "type": "Attribute",
        },
    )
    columns: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
