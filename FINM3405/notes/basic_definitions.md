# FINM3405 Revision

# Lecture 1 - Basic definitions

### Lecture 1
- 1. Basic definitions of:
    - 1.1 Futures and forwards.
    - 1.2 Options.
    - 1.3 Swaps
      - 1.3.1 interest rate swaps
      - 1.3.2 FX swaps
      - 1.3.3 currency swaps
      - 1.3.4 credit default swaps
- 2. Differences between futures and forwards.
- Basic payoff diagrams of futures/forwards and options. (1.1 - 1.3)
- 3. Central, foundational, fundamental building block concepts on which all of financial theory and practice are built:
  - 3.1. Law of finance and present value (later became risk-neutral pricing).
  - 3.2. No arbitrage and the law of one price.


### Derivative securities facilitate the management of risks
- The financial system performs its core function of transferring savings and investment funds to long-term investments in real assets.
- Businesses simply go about their usual day-to-day trading activities.

### Uses
- Trading, speculation and arbitrage.
  - Derivatives can be more efficient and cost effective means by which to speculate on movements in the underlying asset than trading the asset itself
- Risk management or hedging.
  -  Credit/default and counterparty risk.
  - Market risks including adverse movements in interest rates, exchange rates, commodity prices, equity/share prices, etc.
  - Government/political/sovereign risk, uncertainty and instability, including changing regulations, elections and military conflict.
- Market making.
  - Market makers, and dealers in OTC markets, perform this liquidity function by continuously providing bid and ask quotes in the market for other participants to trade at
- Regulators and other industry bodies and associations.

## 1.1 Futures and forwards

``Defn``

Futures and forwards are contracts obligating two parties to trade an agreed quantity of the underlying asset for an agreed contract price K on an agreed future date T (the maturity date).

The basic difference between futures and forward contracts is:
- Futures are standardised contracts traded on trading venues (exchange-traded).
- Forwards are negotiated between the parties in OTC markets.

At maturity T, the long party buys the underlying asset for $K$. If $S_{T} > K$ at maturity, then the long party has benefited by the amount $S_{T} − K$.

But if $S_{T} < K$ at maturity then the short party, who sells the underlying asset for K, has benefited by the amount $K − S_{T}$.
-  Hence, the payoffs to the long and short parties are:

long payoff = $S_{T} − K$ and short payoff= $K − S_{T}$.


![alt text](assets\IMG2.PNG)


## 1.2 Options

There are two basic types of option contracts, namely call and put options:

The *holder* of a European **call** option has the *right but not the obligation to buy* an agreed quantity of the underlying asset for an agreed strike price K on an agreed future date T (expiry).

The *holder* of a European **put** option has the *right but not the obligation to sell* an agreed quantity of the underlying asset for an agreed strike price K on an agreed future date T (expiry).

Note that an American option gives the holder these rights to *exercise an option at any point up and including the expiry date* T.


- The holder of an option is also called the taker, and is said to be **long**.
- The other party to the contract is called the writer and said to be **short.**

### Expiry - call
European **call holder’s payoff** at expiry is call holder payoff = ``max``${0, S_{T} − K}$. 

### Expiry - put
European **put holder’s payoff** at expiry is put holder payoff = max ${0, K − S_{T} }$.

## 1.3 Swaps

Swaps include:
- Interest rate swaps.
- Foreign exchange (FX) swaps.
- Currency swaps.
- Credit default swaps.

### 1.3.1 Interest Rate Swaps
A plain vanilla fixed-for-floating interest rate swap involves two parties swapping their existing loan payment obligations:

- One party swaps fixed-rate payments with floating-rate payments.
  - They have an existing fixed-rate loan but want to pay floating.
- The other swaps floating-rate payments with fixed-rate payments.
  - They have an existing floating-rate loan but want to pay fixed.


**Reasons**
- Interest rate swaps can help businesses manage interest rate risk
- Enable a business to borrow at terms most favourable to them and then swap their loan to their desired interest rate exposure

### 1.3.2 Foreign Exchange (FX) Swaps

A foreign exchange (FX) swap is an agreement to exchange one currency for another at an agreed rate on an agreed date and to re-exchange those two currencies at a later date at an agreed rate.

FX swaps are negotiated and arranged OTC.

### 1.3.3 Currency Swaps

A currency swap is an agreement between two parties to swap interest payments on a loan made in one currency for interest payments on a loan made in another currency.

### 1.3.4 Credit Default Swaps

A credit default swap is effectively an insurance contract between two parties in which one party purchases protection for a defined period of time from another party against losses from the occurrence of some credit event, usually default of a third party called the reference entity.

- The buyer pays the seller regular premiums, and in return receives a payout from the seller if the reference entity defaults.
  - Hence, credit default swaps help businesses manage credit risk, but they’re also used for speculation and arbitrage.
- They are negotiated and arranged OTC.

# 3. Foundational Concepts

## 3.1. Law of finance (Present Value)

The value of an asset is the present value of its expected future cashflows.

## 3.2. No arbitrage and the law of one price

- A very common approach or technique used in derivative security valuation is to construct a portfolio of more basic securities (such as stocks, bank accounts, simple forwards and futures, etc) which replicates the derivative’s future cashflow structure or payoff.

- Securities or portfolios with the same future cashflow structure or payoff must have the same price

**No Arbitrage**

An arbitrage opportunity can be defined in various equivalent ways, and the following two alternative definitions will suffice for this course:
1. An arbitrage opportunity is a scenario that has no initial, upfront cashflow or exchange of money, no risk of future loss (negative cashflow), but a chance of a future profit (positive cashflow).
  - Keep investing at 0 cost with the possibility of a future profit.
2. Alternatively, an arbitrage opportunity is a scenario of two different portfolios or financial securities having the same future cashflow structure or payoff, but different prices.
  - Long the cheap and short the expensive security/portfolio. 

Neither of these scenarios can last long in efficient financial markets.