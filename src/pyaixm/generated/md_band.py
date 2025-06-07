from dataclasses import dataclass

from generated.md_band_type import MdBandType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBand(MdBandType):
    class Meta:
        name = "MD_Band"
        namespace = "http://www.isotc211.org/2005/gmd"
