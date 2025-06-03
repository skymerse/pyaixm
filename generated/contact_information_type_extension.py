from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ContactInformationTypeExtension:
    class Meta:
        global_type = False

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
