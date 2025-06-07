from dataclasses import dataclass

from pyaixm.generated.pt_locale_container_type import PtLocaleContainerType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocaleContainer(PtLocaleContainerType):
    class Meta:
        name = "PT_LocaleContainer"
        namespace = "http://www.isotc211.org/2005/gmd"
