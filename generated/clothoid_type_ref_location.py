from dataclasses import dataclass, field
from typing import Optional

from generated.affine_placement import AffinePlacement

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ClothoidTypeRefLocation:
    class Meta:
        global_type = False

    affine_placement: Optional[AffinePlacement] = field(
        default=None,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
