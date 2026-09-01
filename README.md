# Flip 7 Strategy Simulator
## Overview
Python simulation comparing player strategies for the card game Flip 7, 
using statistical testing to evaluate performance against a baseline.
## Tools
Python (OOP), Pandas, Matplotlib, SciPy
## Methodology
- Built 5 simulation variants isolating different strategy mechanics 
  (baseline, flip 3, 2nd chance, EV, all combined)
- Ran 1,000+ games per strategy, logging results to CSV
- Analyzed win rates, average scores, and standard deviation with Pandas
- Visualized win rates and score margins with Matplotlib
- Tested statistical significance of each strategy vs. baseline using 
  SciPy chi-square tests
## Key Findings
Win rates
- Flip 3 strategy: Increased from 45.6% to 47.7% (+2.1 percentage points, p ≈ 0.370)
- 2nd chance strategy: Increased from 45.6% to 52.5% (+6.9 percentage points, p ≈ 0.00235)
- EV strategy: Increased from 45.6% to 59.2% (+13.6 percentage points, p ≈ 1.50 * 10^-9)
- Combined strategy: Increased from 45.6% to 66.1% (+20.5 percentage points, p ≈ 4.07 * 10^-20)
