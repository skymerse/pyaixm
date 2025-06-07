from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.md_digital_transfer_options_property_type import (
    MdDigitalTransferOptionsPropertyType,
)
from pyaixm.generated.md_distributor_type import (
    MdDistributorPropertyType,
    MdFormatPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributionType(AbstractObjectType):
    """
    Information about the distributor of and options for obtaining the dataset.
    """

    class Meta:
        name = "MD_Distribution_Type"

    distribution_format: Iterable[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributionFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    distributor: Iterable[MdDistributorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    transfer_options: Iterable[MdDigitalTransferOptionsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transferOptions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
