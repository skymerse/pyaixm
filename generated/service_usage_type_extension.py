from dataclasses import dataclass, field

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ServiceUsageTypeExtension:
    class Meta:
        global_type = False

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
