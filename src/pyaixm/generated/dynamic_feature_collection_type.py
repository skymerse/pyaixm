from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.abstract_feature_member_type import (
    AbstractFeatureMemberType,
)
from pyaixm.generated.actuate_type import ActuateType
from pyaixm.generated.dynamic_feature import DynamicFeature
from pyaixm.generated.dynamic_feature_type import DynamicFeatureType
from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.show_type import ShowType
from pyaixm.generated.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureCollectionType(DynamicFeatureType):
    dynamic_members: Optional["DynamicMembers"] = field(
        default=None,
        metadata={
            "name": "dynamicMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class DynamicFeatureCollection(DynamicFeatureCollectionType):
    """A gml:DynamicFeatureCollection is a feature collection that has a
    gml:validTime property (i.e. is a snapshot of the feature collection) or which
    has a gml:history property that contains one or more gml:AbstractTimeSlices
    each of which contain values of the time varying properties of the feature
    collection.

    Note that the gml:DynamicFeatureCollection may be one of the following:
    1.      A feature collection which consists of static feature members (members do not change in time) but which has properties of the collection object as a whole that do change in time .
    2.      A feature collection which consists of dynamic feature members (the members are gml:DynamicFeatures) but which also has properties of the collection as a whole that vary in time.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureMemberType(AbstractFeatureMemberType):
    dynamic_feature_collection: Iterable[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature: Iterable[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class DynamicMembers(DynamicFeatureMemberType):
    class Meta:
        name = "dynamicMembers"
        namespace = "http://www.opengis.net/gml/3.2"
