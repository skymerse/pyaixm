from dataclasses import dataclass

from generated.runway_blast_pad_type import RunwayBlastPadType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayBlastPad(RunwayBlastPadType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
