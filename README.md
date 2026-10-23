# hk-ipo-kit

A small, MIT-licensed Python toolkit for **Hong Kong IPO research** — the two
things retail subscribers and students currently assemble by hand from broker
notices and exchange filings:

1. **True entry cost per lot** — offer price × lot size is *not* what you pay.
   `hkipo cost` adds the 1% brokerage and the SFC / HKEX / FRC levies.
2. **A clean subscription calendar** — one CSV row per IPO (open/close,
   listing date, price range, lot size), loadable in Python or Excel.

中文簡介：計算香港新股每手真實入場費（連佣金及徵費），並提供可直接用於
分析的 IPO 日曆 CSV 資料集。

## Install (once published / from a clone)
```bash
pip install hk-ipo-kit        # planned for v0.1.0
# from source:
pip install -e .
```

## Examples
```bash
hkipo cost --price 10 --lot-size 500
# Shares: 500  Application: HK$5,000.00  Fees: HK$50.42  Total entry: HK$5,050.42

hkipo calendar --file data/sample_ipos.csv --on 2026-10-22
```
```python
from hkipo import entry_cost
entry_cost(price=12.0, lot_size=100, lots=2, brokerage_rate=0.0)  # broker waives brokerage
```

## Status
v0.0.2. `data/oct_2026_ipos.csv` now holds **real, verified October 2026
listings** (ESWIN Computing 1256; Transsion Holdings 2636), and the
calculator reproduces both deals' published maximum entry fees to the cent
(see tests). `data/sample_ipos.csv` remains **illustrative only**.
Known gap: the calendar has no `status` field, so a postponed deal —
e.g. Slender West Lake (6157), postponed 20 Oct 2026 after subscriptions
closed — cannot yet be represented; that is the v0.0.3 item.
Out of scope: prospectus PDF parsing, grey-market prices, and any order
placement (this is a research tool, not investment advice).

## Contributing / Licence
Issues and PRs welcome — see CONTRIBUTING.md. MIT licence — see LICENSE.
