import argparse
from .cost import entry_cost
from .calendar import load_calendar, open_for_subscription

def main() -> None:
    p = argparse.ArgumentParser(prog="hkipo", description="HK IPO research toolkit")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cost", help="true entry cost per lot")
    c.add_argument("--price", type=float, required=True)
    c.add_argument("--lot-size", type=int, required=True)
    c.add_argument("--lots", type=int, default=1)
    c.add_argument("--brokerage-rate", type=float, default=0.01)
    cal = sub.add_parser("calendar", help="list IPOs open on a date")
    cal.add_argument("--file", required=True)
    cal.add_argument("--on", required=True, help="ISO date yyyy-mm-dd")
    a = p.parse_args()
    if a.cmd == "cost":
        r = entry_cost(a.price, a.lot_size, a.lots, a.brokerage_rate)
        print(f"Shares: {r.shares}  Application: HK${r.application_amount:,.2f}  "
              f"Fees: HK${r.total_fees:,.2f}  Total entry: HK${r.total_cost:,.2f}")
    else:
        for i in open_for_subscription(load_calendar(a.file), a.on):
            print(f"{i.code} {i.name} — closes {i.close_date}, lists {i.listing_date}, "
                  f"HK${i.price_low}-{i.price_high}, lot {i.lot_size}")
if __name__ == "__main__":
    main()
