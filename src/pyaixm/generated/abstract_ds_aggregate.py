from dataclasses import dataclass

from pyaixm.generated.md_metadata_type import AbstractDsAggregateType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDsAggregate(AbstractDsAggregateType):
    class Meta:
        name = "AbstractDS_Aggregate"
        namespace = "http://www.isotc211.org/2005/gmd"
