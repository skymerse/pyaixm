from dataclasses import dataclass

from generated.fasdata_block_type import FasdataBlockType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FasdataBlock(FasdataBlockType):
    class Meta:
        name = "FASDataBlock"
        namespace = "http://www.aixm.aero/schema/5.1"
