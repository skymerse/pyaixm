from dataclasses import dataclass, field
from typing import Any

from pyaixm.generated.abstract_gmltype import AbstractGmltype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmobjectType(AbstractGmltype):
    """Base type for AIXM complex types that are NOT features.

    For example, City, ContactInformation, AirspaceVolume, etc. It
    derives from AbstractGMLType so that AIXM objects are recognised as
    GML objects, thus ensuring that GML-aware applications recognise
    them properly. Retains only the mandatory gml:id attribute.
    """

    class Meta:
        name = "AbstractAIXMObjectType"

    meta_data_property: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description_reference: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    identifier: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    opengis_net_gml_3_2_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
