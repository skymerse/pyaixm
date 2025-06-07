from dataclasses import dataclass

from generated.rules_procedures_extension_type import (
    RulesProceduresExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RulesProceduresExtension(RulesProceduresExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
