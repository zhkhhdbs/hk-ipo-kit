# Changelog
## 0.0.2 — 2026-10-22
- Real dataset: `data/oct_2026_ipos.csv` with two verified October 2026
  listings — ESWIN Computing (1256) and Transsion Holdings (2636) —
  replacing reliance on the illustrative sample for real use.
- Validation tests: the entry-fee calculator now reproduces the published
  maximum entry fees exactly — Transsion HK$3,919.13/lot and Slender West
  Lake (6157) HK$5,121.14/lot. 6 tests pass.
- Known gap: Slender West Lake (6157) postponed its offering on 20 Oct 2026
  after subscriptions closed (refunds from 23 Oct) — the calendar schema
  has no `status` field yet, so postponed deals cannot be represented.
  Adding `status` is the top item for v0.0.3.

## 0.0.1 — 2026-10-22
- Scaffold: entry-fee calculator (brokerage + SFC/HKEX/FRC levies), calendar
  CSV loader/filter, CLI (`cost`, `calendar`), tests, CI workflow.
