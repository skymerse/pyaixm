from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_feature_type import AbstractFeatureType
from pyaixm.generated.data_source import DataSource
from pyaixm.generated.data_source_reference import DataSourceReference
from pyaixm.generated.history import History
from pyaixm.generated.track import Track
from pyaixm.generated.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureType(AbstractFeatureType):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    track: Optional[Track] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    data_source_reference: Optional[DataSourceReference] = field(
        default=None,
        metadata={
            "name": "dataSourceReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
