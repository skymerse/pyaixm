from dataclasses import dataclass

from pyaixm.generated.runway_blast_pad_extension_type import (
    RunwayBlastPadExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayBlastPadExtension(RunwayBlastPadExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
