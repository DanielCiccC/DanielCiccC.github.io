# Tutorial 12

### 1
- VaR estimates the maximum loss expected (with a given confidence interval, usually 95% or 99%) over a set period under normal market condition
- ES provides an average of the losses that exceeed the VaR at a certain confidence level.
  - Provides a fuller picture of the tail risk

### 2

Financial market returns often exhibit fat tails meaning that extreme events (large losses/gains) happen more frequently than predicted by a normal distribution
- A normal distribution understates the likelihood of extreme market movements, thus underestimating VaR and ES

To improve the accuracy, we could take a non-parametric approach, e.g. historical simulation could be used to calculate VaR and ES based on actual historical returns.

This method makes no assumptions about the underlying return distribution, making it more accurate during periods of market stress/high volatility.

### 3
