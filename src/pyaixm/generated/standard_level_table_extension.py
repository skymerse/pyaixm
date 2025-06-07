from dataclasses import dataclass

from pyaixm.generated.standard_level_table_extension_type import (
    StandardLevelTableExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class StandardLevelTableExtension(StandardLevelTableExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
