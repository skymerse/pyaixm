from dataclasses import dataclass

from generated.standard_level_sector_extension_type import (
    StandardLevelSectorExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class StandardLevelSectorExtension(StandardLevelSectorExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
