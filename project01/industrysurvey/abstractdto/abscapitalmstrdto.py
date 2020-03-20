from dataclasses import dataclass, fields, asdict, astuple

@dataclass
class AbsCapitalMasterDTO:
    CustomerCd: str
    CustomerCapital: float
