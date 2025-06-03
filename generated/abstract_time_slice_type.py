from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_gmltype import AbstractGmltype
from generated.data_source import DataSource
from generated.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeSliceType(AbstractGmltype):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
