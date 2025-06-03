from dataclasses import dataclass

from generated.abstract_surface_contamination_type import (
    AbstractSurfaceContaminationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractSurfaceContamination(AbstractSurfaceContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
