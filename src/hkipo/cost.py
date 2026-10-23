"""Hong Kong IPO entry-fee calculator.

Fee schedule (HKEX / SFC, as commonly applied by HK brokers for IPO
subscriptions paid in full at application):
- brokerage: 1% of application amount (broker-set; many charge 1%, some waive)
- SFC transaction levy: 0.0027%
- HKEX trading fee: 0.00565%
- FRC transaction levy: 0.00015%
Sources: HKEX IPO subscription fee disclosures; rates are parameters so a
broker waiver or a rate change is a one-line change, not a code change.
"""
from dataclasses import dataclass

SFC_LEVY = 0.000027
HKEX_FEE = 0.0000565
FRC_LEVY = 0.0000015

@dataclass(frozen=True)
class EntryCost:
    shares: int
    application_amount: float
    brokerage: float
    sfc_levy: float
    hkex_fee: float
    frc_levy: float
    @property
    def total_fees(self) -> float:
        return self.brokerage + self.sfc_levy + self.hkex_fee + self.frc_levy
    @property
    def total_cost(self) -> float:
        return self.application_amount + self.total_fees

def entry_cost(price: float, lot_size: int, lots: int = 1,
               brokerage_rate: float = 0.01) -> EntryCost:
    if price <= 0 or lot_size <= 0 or lots <= 0:
        raise ValueError("price, lot_size and lots must be positive")
    shares = lot_size * lots
    amount = price * shares
    return EntryCost(shares=shares, application_amount=round(amount, 2),
        brokerage=round(amount * brokerage_rate, 2),
        sfc_levy=round(amount * SFC_LEVY, 2),
        hkex_fee=round(amount * HKEX_FEE, 2),
        frc_levy=round(amount * FRC_LEVY, 2))
