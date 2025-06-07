from dataclasses import dataclass

from pyaixm.generated.search_rescue_service_extension_type import (
    SearchRescueServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SearchRescueServiceExtension(SearchRescueServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
