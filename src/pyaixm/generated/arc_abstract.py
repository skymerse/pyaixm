from dataclasses import dataclass

from generated.arc_type_2 import ArcType2

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class ArcAbstract(ArcType2):
    class Meta:
        name = "arc"
        namespace = "http://www.w3.org/1999/xlink"
