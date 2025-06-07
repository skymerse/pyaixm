from dataclasses import dataclass

from pyaixm.generated.standard_level_sector_type import StandardLevelSectorType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelSector(StandardLevelSectorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
