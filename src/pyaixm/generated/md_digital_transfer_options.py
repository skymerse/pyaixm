from dataclasses import dataclass

from pyaixm.generated.md_digital_transfer_options_type import (
    MdDigitalTransferOptionsType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDigitalTransferOptions(MdDigitalTransferOptionsType):
    class Meta:
        name = "MD_DigitalTransferOptions"
        namespace = "http://www.isotc211.org/2005/gmd"
