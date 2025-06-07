from dataclasses import dataclass

from generated.md_aggregate_information_type import MdAggregateInformationType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdAggregateInformation(MdAggregateInformationType):
    class Meta:
        name = "MD_AggregateInformation"
        namespace = "http://www.isotc211.org/2005/gmd"
