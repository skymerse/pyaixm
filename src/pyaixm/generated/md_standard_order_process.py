from dataclasses import dataclass

from pyaixm.generated.md_standard_order_process_type import (
    MdStandardOrderProcessType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdStandardOrderProcess(MdStandardOrderProcessType):
    class Meta:
        name = "MD_StandardOrderProcess"
        namespace = "http://www.isotc211.org/2005/gmd"
