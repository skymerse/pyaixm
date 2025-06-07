from dataclasses import dataclass

from generated.standard_level_column_extension_type import (
    StandardLevelColumnExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class StandardLevelColumnExtension(StandardLevelColumnExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
