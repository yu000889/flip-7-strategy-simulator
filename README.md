# Flip 7 Strategy Simulator
## Overview
Flip 7 is a push-your-luck card game where players choose whether to
continue drawing cards or stop and keep their current score. This project
uses Python simulation to investigate how different decision-making
strategies affect player scores and win rates.

## Tools
Python (OOP), Pandas, Matplotlib, SciPy

## Strategies
The simulation compares a baseline strategy with four strategies that
individually or collectively introduce different decision-making mechanics.
- **Baseline:** Uses the standard decision-making strategy without any of the experimental mechanics.
- **Flip 3:** Uses information from the Flip 3 mechanic to make more informed decisions about whether to continue drawing.
- **2nd Chance:** Uses the 2nd Chance mechanic to reduce the risk of losing a round when a duplicate card is drawn.
- **EV:** Uses expected value calculations to determine whether continuing to draw is likely to improve the player's expected score.
- **Combined:** Combines the Flip 3, 2nd Chance, and EV mechanics into a single strategy.

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
- EV strategy: Increased from 45.6% to 59.2% (+13.6 percentage points, p ≈ 1.50e-9)
- Combined strategy: Increased from 45.6% to 66.1% (+20.5 percentage points, p ≈ 4.07e-20)

Overall, the EV-based strategy produced a substantial improvement in win rate, while combining all strategy mechanics produced the largest improvement.
