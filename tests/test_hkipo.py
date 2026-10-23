import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from hkipo import entry_cost, load_calendar, open_for_subscription

def test_entry_cost_one_lot():
    r = entry_cost(price=10.0, lot_size=500)
    assert r.shares == 500 and r.application_amount == 5000.0
    assert r.brokerage == 50.0
    assert abs(r.total_cost - (5000.0 + r.total_fees)) < 0.01
    assert 50.0 < r.total_fees < 51.0  # 1% brokerage + ~0.0085% levies/fees

def test_entry_cost_zero_brokerage_waiver():
    r = entry_cost(price=12.0, lot_size=100, lots=2, brokerage_rate=0.0)    assert r.brokerage == 0.0 and r.application_amount == 2400.0def test_entry_cost_rejects_nonpositive():
    try:
        entry_cost(price=0, lot_size=100); assert False
    except ValueError: pass

def test_calendar_filter():
    rows = load_calendar(Path(__file__).parent.parent / "data" / "sample_ipos.csv")
    assert len(open_for_subscription(rows, "2026-10-22")) == 1
    assert len(open_for_subscription(rows, "2026-10-24")) == 0

def test_oct2026_real_dataset():
    rows = load_calendar(Path(__file__).parent.parent / "data" / "oct_2026_ipos.csv")
    assert {r.code for r in rows} == {"1256", "2636"}
    on_oct1 = open_for_subscription(rows, "2026-10-01")
    assert [r.code for r in on_oct1] == ["1256"]  # ESWIN only
    on_oct10 = open_for_subscription(rows, "2026-10-10")
    assert [r.code for r in on_oct10] == ["2636"]  # Transsion only

def test_entry_cost_matches_published_max_entry_fees():
    # Transsion (2636): published maximum entry fee HK$3,919.13 per lot
    # (offer price high HK$38.80 x 100 shares, incl. 1% brokerage + levies)
    assert entry_cost(price=38.80, lot_size=100).total_cost == 3919.13
    # Slender West Lake (6157): published maximum payment HK$5,121.14 per lot
    # (offer price high HK$5.07 x 1,000 shares) — offering later postponed
    assert entry_cost(price=5.07, lot_size=1000).total_cost == 5121.14
