from dataclasses import dataclass

from generated.sector_design_type import SectorDesignType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SectorDesign(SectorDesignType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
