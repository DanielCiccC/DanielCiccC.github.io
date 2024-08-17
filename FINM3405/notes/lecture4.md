# Lecture 4

> - Plain vanilla options - basic kinds of options
>   - there are more exotic options, complicated derivative securities also

## Introduction to options
Recall that there is two types of plain vanilla European options:
- Call option: Gives the holder the right but not the obligation to buy the underlying asset for the strike price K on the expiry date T.
- Put option: Gives the holder the right but not the obligation to sell the underlying asset for the strike price K on the expiry date T.

Also recall that an *American* option gives the holder these rights *at any point in time up to and including the expiry date* T.

> - also called strike price, or exercise price, or $k$
> - option premium or value, or price.
> - For options we call it options date (or maturity date)


The option writer is “at the mercy of” the buyer.
- We say that an option has asymmetric rights.

> - Assume no counterparty risk - we assume they are going to do it

## Notation

- We work on a given time interval $0 ≤ t ≤ T$ where:
  - Time $t = 0$ is the date we enter into a contract.
  - Time $T$ is the expiry date.
  - Time $t$ is some intermediate date $0 ≤ t ≤ T$.
- S t is the underlying asset’s price at time t.
  - We write $S = S_{0}$ to reduce notation.
- $r$ is the risk free rate.
- $K$ is the strike or exercise price (some authors use X).
- $C_{t}$ and $P_{t}$ are the call and put prices (premiums) at time $t$.
  - Again, we write $C = C_{0}$ and $P = P_{0}$.


Asymmetric rights: The holder (long position) has payoffs at expiry of
- call holder payoff = $\max {0, S_{T} − K},$
- put holder payoff = $\max {0, K − S_{T}}$

and the writer’s (short position) payoffs are the negative of these:
- call writer payoff= $− \max {0, S_{T} − K}$,
- put writer payoff= $− \max {0, K − S_{T}}$.

> thinking about payoffs only
> - Beauty of options for holders is never non-negative
>  - not going to incur a loss besides the premium they pay

## Option Payoffs and profits

### Call options
![alt text](assets\IMG48.PNG)

### Put options

![alt text](assets\IMG49.PNG)

> Options intrinsic value

At any time t, an option’s intrinsic or exercise value (IV) is
call $IV_{t} = max{0, S_{t} − K}$ and put $IV_{t} = max{0, K − S_{t}}$
(payoff if the option expired at time t). At time t an option is:
- In the money if it has positive intrinsic value:
  - $K < S_{t}$ for a call option.
  - $S_{t} < K$ for a put option.
- At the money if $S_{t} = K$ (intrinsic value is 0).
- Out of the money if its intrinsic value is 0 and $S_{t} ̸= K$:
  - $S_{t} < K$ for a call option.
  - $K < S_{t}$ for a put option.

> - in the money, positive payoff

The above motivates using the idea of no arbitrage to justify the taker having to pay the option price or premium to the writer:
- The holder’s payoff at expiry is nonnegative (positive or zero).
- If options required no upfront premium, then by definition this would be an arbitrage opportunity for the holder:
  - No upfront cashflow.
  - No risk of loss.
  - Chance of a positive payoff.

**Remark** Developing complex mathematical models that calculate the fair value of an option’s premium takes up a lot of space in the world of quant finance in both industry and academia.

> - Have a positive value at any point in time
> - Option holder, payoff is not negative you can never lose
>   - If the option costs nothing, you would enter into more and more
>   - Would be an arbitrage situation and would not hold
> Premium takes up a 

To calculate trading profits, the above payoff s need to be modified to incorporate the premium paid/received. The option taker’s profits are:
- call holder profit = $max {0, S T − K} − C$,
- put holder profit = $max {0, K − S T } − P$

and the writer’s (short position) profits are the negative of these:
- call writer profit = $C − max{0, S T − K}$,
- put writer profit = $P − max{0, K − S T }$.

> - profits, profit diagram
> - same as payoff diagram and including the premium

![alt text](assets\IMG50.PNG)


So the premium gives the writer a chance of a profit, but exposes them
to the risk of significant loss, unlimited in the case of call options:

- Calls and puts:
  - Holder: Loss is limited to the premium paid C or P.
  - Writer: Profit is limited to the premium received C or P.
- Call options:
  - Holder: Profit is unlimited and equal to $S_{T} − K − C$ for $S_{T} > K$.
  - Writer: Loss is unlimited and equal to $S_{T} − K − C$ for $S_{T} > K$.
- Put options:
  - Holder: Profit is potentially large and as much as $K − P$ for $S_{T} = 0$.
  - Writer: Loss is potentially large and as much as $K − P$ for $S_{T} = 0$.

Exchanges have margin mechanisms for short options positions.


Fundamental differences between futures/forwards and options:
- Obligations:
  - Futures/forwards: Both parties must transact.
  - Options: The taker/holder gets to choose.
- Payoff s:
  - Futures/forwards: Symmetric.
  - Options: Asymmetric (favour the taker/holder).
- The “price” or value:
  - Futures/forwards: The actual contract price $K_{t}$.
  - Options: The premium $C t or P_{t}$ (the strike price K is fixed).
- Upfront cashflow:
  - Futures/forwards: $K_{t}$ is set so they have 0 upfront value/cashflow.
  - Options: The taker pays premium $C_{t}$ or $P_{t}$ upfront to the writer.

> - Price of a futures or forwards, the actual price of the contract ($k$)
> - In contracts it is the price of the premium

## Options markets

We look at the main exchange traded options markets and contracts for:
- Equities:
  - Individual share and ETFs.
  - Share index.
- Currencies.
While doing this we don’t present basic speculation and hedging examples since these we devote a whole lecture to this in a few weeks time. We also cover interest rate derivatives later in the course.

## Commodity options

Note also that commodity options are not as actively traded as commodity futures so we’ll skip looking at commodity options:

![alt text](assets\IMG51.PNG)

> Nowhere near as popular

## Equity Options

Equity options are very popular and heavily traded products. Below gives volumes for all exchange traded derivatives (options and futures).

![alt text](assets\IMG52.PNG)

And out of the very large volume of equity derivatives trading worldwide from the previous slide, it’s mostly equity options trading:

> - Hedge on options, trading on exchanges

![alt text](assets\IMG53.PNG)

> It goes without saying that equity index options dwarf everything else.
>
> 