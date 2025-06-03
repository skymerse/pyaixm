from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_level_series_type import CodeLevelSeriesType
from generated.code_rvsmtype import CodeRvsmtype
from generated.note_property_type import NotePropertyType
from generated.standard_level_column_time_slice_type_extension import (
    StandardLevelColumnTimeSliceTypeExtension,
)
from generated.standard_level_property_type import StandardLevelPropertyType
from generated.standard_level_table_property_type import (
    StandardLevelTablePropertyType,
)
from generated.uom_distance_vertical_type_value import (
    UomDistanceVerticalTypeValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelColumnTimeSliceType(AbstractAixmtimeSliceType):
    series: Optional[CodeLevelSeriesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    unit_of_measurement: Optional[Union[str, UomDistanceVerticalTypeValue]] = (
        field(
            default=None,
            metadata={
                "name": "unitOfMeasurement",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "pattern": r"OTHER(:(\w|_){1,58})?",
            },
        )
    )
    separation: Optional[CodeRvsmtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    level: Iterable[StandardLevelPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    level_table: Optional[StandardLevelTablePropertyType] = field(
        default=None,
        metadata={
            "name": "levelTable",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[StandardLevelColumnTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
