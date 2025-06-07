from dataclasses import dataclass

from generated.indirect_entry_type import IndirectEntryType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class IndirectEntry(IndirectEntryType):
    class Meta:
        name = "indirectEntry"
        namespace = "http://www.opengis.net/gml/3.2"
