# Flip 7 Strategy Simulator
Python simulation and statistical analysis of strategy performance in Flip 7.
## Overview
This project simulates 5 versions of Flip 7 — a baseline with no special logic, and four variants that each add one specific strategy mechanic (flip-3 targeting, 2nd chance usage, EV-based decisions, and all combined). Each version played 1,000 games against baseline to see which mechanics actually help win.
## Tools Used
Python (pandas, matplotlib, scipy)
## Key Findings
- 2nd chance, EV-based decisions, and the combined strategy all significantly improved win rate over baseline (p < 0.0001)
- Flip-3 targeting alone showed no significant effect (p = 0.37)
