from enum import Enum

class DecoderModes(Enum):
    AND_OR = "AND"
    OR_AND = "OR"

class LogicGateTypes(Enum):
    AND = "Logic AND"
    OR = "Logic OR"
    NOT = "Logic NOT"
    XOR = "Logic XOR"
    NOR = "Logic NOR"
    NAND = "Logic NAND"
