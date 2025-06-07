from dataclasses import dataclass

from pyaixm.generated.localizer_type import LocalizerType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Localizer(LocalizerType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
