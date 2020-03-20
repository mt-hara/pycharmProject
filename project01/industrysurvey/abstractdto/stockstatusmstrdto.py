from dataclasses import dataclass, fields, asdict, astuple

@dataclass
class AbsStockStatusMasterDTO:
    CustomerCd: str
    stockListingStatus: str
    MainStockholder_1: str
    MainStockholder_2: str
    MainStockholder_3: str
    MainStockholder_4: str
    MainStockholder_5: str
    ratioSH_1: float
    ratioSH_2: float
    ratioSH_3: float
    ratioSH_4: float
    ratioSH_5: float