# Flip 7 Strategy Simulator
Python simulation and statistical analysis of strategy performance in Flip 7.
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
- 2nd chance, EV-based decisions, and the combined strategy all significantly improved win rate over baseline (p < 0.0001)
- Flip-3 targeting alone showed no significant effect (p = 0.37)
