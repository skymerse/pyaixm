from dataclasses import dataclass

from generated.search_rescue_service_type import SearchRescueServiceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SearchRescueService(SearchRescueServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
