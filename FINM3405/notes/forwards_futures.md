# FINM3405 Revision

# Lecture 2-3 Futures & forwards

- 1. Definitions
  - 1.1. differences 
  - 1.2. payoff diagrams
- 2. Margin mechanism and leverage effect for futures.
- 3. Calculate the value of a futures/forward contract.
- The following for the main classes of futures and forwards in terms of the underlying asset, namely commodities, equities, currencies and interest rates (FRA and BAB futures):
  - Main contracts and their specifications.
  - Perfect hedging examples.
  - Basic examples of speculating on the price of the underlying asset.
- Contract pricing via the cost of carry approach.
- Basis risk and optimal hedging.

---
### Aside: Notation
- Hypothetical time interval $[0, T]$.
  - Time $t = 0$ is a contract’s initiation date.
  - Time $T$ is a contract’s maturity or delivery date.
  - Time $t$ is some intermediate date: $0 ≤ t ≤ T$.
- $S_{t}$ is the underlying asset’s spot price at time $t$.
- $K_{t}$ is the contract price at time $t$.
  - We write $S = S_{0}$ and $K = K_{0}$ to reduce notation.
- $m$ is the contract multiplier.
- $F_{t} = K_{t} \times m$ is the notional or face value of 1 contract.
- $h$ is the number of contracts we enter into.
- $K_{t}$ is the contract price when initiating a contract at time $t$.
  - Long position at time $t$: Agree buy the asset for $K_{t}$ at maturity $T$.
  - Short position at time $t$: Agree sell the asset for $K_{t}$ at maturity $T$.
---

## 1. Definitions

- Futures and forwards are contracts between two parties to trade an agreed quantity $m$ of an asset for an agreed contract or forward price $K$ on an agreed future delivery or maturity date $T$.

### 1.1 Differences
The basic difference between futures and forward contracts is:
- Futures are traded on exchanges (and other trading venues).
- Forwards are negotiated directly between market participants OTC.

This has a number of implications, including:
- Contract standardisation.
- Centralised counterparty.
- Counterparty risk.
- Trading liquidity and ability to close out positions.
- Holding to maturity vs closing out early.
- Margin mechanism and daily settlement (futures only)

### 1.2. Payoff Diagrams
The payoffs at maturity from 1 contract (over 1 asset) are:

![alt text](assets\IMG10.PNG)

long payoff = $S_{T} − K$ and short payoff = $K − S_{T}$

## 2. Margin Mechanism & Leverage Effect

The futures margin mechanism can be described as follows:
- You post an initial margin into your margin account, which is a percent of the contract price $K$ (per contract).
- Your position is marked to market on a daily basis, with daily gains (losses) credited to (debited from) your margin account.
- There is a maintenance margin, usually less than the initial margin.
- If your margin account falls below the maintenance margin, you get a margin call to top your account back up to the **initial margin**.
- If you don’t pay it, the exchange closes out your position
- When closing out your position before maturity, your position is immediately marked-to-market using your closing-out price.

![alt text](assets\IMG16.PNG)

**Leverage Effect**

Leverage effect: Your profit/loss as a percent of the initial margin.
- The danger with futures is you post only the initial margin upfront:
- Long position: You don’t post the full amount $K$ upfront.
- Short position: You don’t need to own the underlying asset.

---
(example in Onenote)

--- 

## 3. Calculate the value of a futures/forward contract

- Go long $h$ contracts at time $t = 0$ for $K$.
- Close your position at time $t$ by shorting $h$ contracts for $K_{t}$.

The cashflow $h(K_{t} − K)m$ locked in at the delivery date is risk free. With
$r$ the risk-free rate, the value at time t of a *long* position is

$$V^{long}_{t} = e^{-r(T-t)}\cdot h(K_{t}-K)\cdot m$$

The value of a short position is thus 
$$V^{short}_{t} = e^{-r(T-t)}\cdot h(K- K_{t})\cdot m$$

- NOTE: discounted at risk free rate $r$

