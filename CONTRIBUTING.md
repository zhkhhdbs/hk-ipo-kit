# Contributing
File an issue for a data error, a missing IPO row, or a feature request.
PRs: keep modules small, add a test for any fee/calendar logic change, and
never commit real broker account data. Fee rates live as named constants in
`src/hkipo/cost.py` — cite the HKEX/SFC source in the PR if you change one.
