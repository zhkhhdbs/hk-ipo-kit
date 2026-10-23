"""Load and filter a clean HK IPO calendar dataset (CSV)."""
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Ipo:
    name: str; code: str; open_date: str; close_date: str
    listing_date: str; price_low: float; price_high: float; lot_size: int

def load_calendar(path: str | Path) -> list[Ipo]:
    with open(path, newline="", encoding="utf-8") as f:
        return [Ipo(name=r["name"], code=r["code"], open_date=r["open_date"],
            close_date=r["close_date"], listing_date=r["listing_date"],
            price_low=float(r["price_low"]), price_high=float(r["price_high"]),
            lot_size=int(r["lot_size"])) for r in csv.DictReader(f)]

def open_for_subscription(ipos: list[Ipo], on_date: str) -> list[Ipo]:
    """IPOs whose subscription window includes on_date (ISO yyyy-mm-dd)."""
    return [i for i in ipos if i.open_date <= on_date <= i.close_date]
