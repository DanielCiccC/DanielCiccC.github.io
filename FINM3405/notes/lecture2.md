# Lecture 2 Futures and forwards - Examples and basic concepts

Futures and forwards are contracts between two parties to trade an agreed quantity $m$ of an asset for an agreed contract or forward price $K$ on an agreed future delivery or maturity date $T$.

- Written over all kinds of assets including shares, ETFs, indices, commodities, interest rates, currencies, energy, weather events, etc.
- Traded all over the world, with forward contracts traded in OTC markets and futures contracts traded on organised exchanges.
- Many uses including speculation and trading, risk management or hedging, arbitrage trading and price discovery, structured and synthetic product construction, portfolio exposure modification, etc.


> contract price or forward price
> - delivery date of the asset
> - written on other derivatives
> - forwards are traded (arranged) OTC
> - futures are traded on organised exchanges
>   - nowadays
>
> Get a sense of underlying assets from futures market trading
> - shares are based on the futures market trading price
> - futures used for construction and synthetic products


### Futures and Forwards
The payoffs at maturity from 1 contract (over 1 asset) are:

![alt text](assets\IMG10.PNG)

long payoff = $S_{T} − K$ and short payoff = $K − S_{T}$ .

> buying assets for K
> - spot price is higher, can sell at the spot price for higher and make a profit

### Example

I agree to buy $m = 1,000$ Alibaba ADRs (traded on NYSE under the ticker BABA) off you in 3 months for $K = \$76.50$ per ADR.

|Spot Price | 
| --- |
| ![alt text](assets\IMG11.PNG)

If the Alibaba’s share (well, ADR) spot price in 3 months is say:
- $S_{T} = \$80$, then I’m happy since I’m buying BABA off you for only K = \$76.50 and I can sell it spot for \$80.
- My payoff is ($S_{T} − K) × m = \$3,500$ (your loss).
- $S_{T} = \$70$, then I’m regretting our agreement since I could
have paid \$70 spot. You’re happy with getting K = \$76.50.
- My payoff is $(S_{T} − K) × m = −\$6, 500$ (your gain).

In the 2nd scenario, you hope that I fulfil my obligations and still buy it off you, and this introduces the idea of counterparty risk.

> Counterparty risk is a big thing
> - hoping that the losing party is going to pay

The payoff diagram for my long forward position with you is:

![alt text](assets\IMG12.PNG)

### Futures and Forwards

The basic difference between futures and forward contracts is:
- Futures are traded on exchanges (and other trading venues).
- Forwards are negotiated directly between market participants OTC.

This has a number of implications, including:
- Contract standardisation.
- Centralised counterparty.
- Counterparty risk.
- Trading liquidity and ability to close out positions.
- Holding to maturity vs closing out early.
- Margin mechanism and daily settlement: See below.

![alt text](assets\IMG13.PNG)

> - normally doing it with a major bank
>   - OTC can be very non-standard
>   - quants trade here, more potential for arbitrage
> - futures, trading with the clearinghouse
>   - obligations are with the clearinghouse - like the intermediary
>   - more standardised

![alt text](assets\IMG14.PNG)

![alt text](assets\IMG15.PNG)

These differences would seem to entail separate treatments of forwards and futures, but we can show that they can be viewed as equivalent under simplifying assumptions such as frictionless financial markets, constant or deterministic (nonrandom) interest rates, etc.

- So we treat them identically in these notes.

> - unrestricted borrowing holdings, no fees, etc we can treat them basically the same

### Notation
We use the following notation and terminology throughout these notes:

- We work on a hypothetical time interval $[0, T]$.
  - Time $t = 0$ is a contract’s initiation date.
  - Time $T$ is a contract’s maturity or delivery date.
  - Time $t$ is some intermediate date: $0 ≤ t ≤ T$.
- $S_{t}$ is the underlying asset’s spot price at time $t$.
- $K_{t}$ is the contract price at time $t$.
  - We write $S = S_{0}$ and $K = K_{0}$ to reduce notation.
- $m$ is the contract multiplier.
- $F_{t} = K_{t} \times m$ is the notional or face value of 1 contract.
- $h$ is the number of contracts we enter into.

Note that it’s very important to be clear about exactly what $K_{t}$ is.

- $K_{t}$ is the contract price when initiating a contract at time $t$.
  - Long position at time $t$: Agree buy the asset for $K_{t}$ at maturity $T$.
  - Short position at time $t$: Agree sell the asset for $K_{t}$ at maturity $T$.

The futures prices quoted on exchanges, or the forward price negotiated between parties OTC, is the contract price $K_{t}$.

> What is the future price you are trading?
> - the contract price $K$

$K_{t}$ varies over time and is the price you trade futures for. Suppose you:
- Go long $h$ contracts at time $t = 0$ for $K$.
- Close out your position at time $t > 0$ by shorting $h$ contracts for $K_{t}$.
- The contract prices K and $K_{t}$ will almost certainly be different!
- You have locked in a payout of $h(K_{t} − K)m$ at the delivery date T. 

Futures trading involves entering into and out of futures contracts over time at different contract prices $K_{t}$ up to the delivery date $T$.
- Traders typically trade the contract with the closest delivery date, and then roll over into the contract with the next delivery date. The margin mechanism governs your trading profits/losses over time:

> decided to buy $h \times m$ in your opening position
> - locking in different prices
> - People typically only trade the futures contract that has the closest maturity date
>   - not exposed to as much basis risk
>   - close out your position as it is nearly due for delivery

### Margin mechanism
The futures margin mechanism can be described as follows:
- You post an initial margin into your margin account, which is a percent of the contract price K (per contract).
- Your position is marked to market on a daily basis, with daily gains (losses) credited to (debited from) your margin account.
- There is a maintenance margin, usually less than the initial margin.
- If your margin account falls below the maintenance margin, you get a margin call to top your account back up to the initial margin.
- If you don’t pay it, the exchange closes out your position and your broker will likely “unfriend” you...
- When closing out your position before maturity, your position is immediately marked-to-market using your closing-out price.

> - futures exchange requires a margin mechanism
>   - have to post an initial margin (safety buffer) have money to honor your trade
>   - between 4-6%
>   - daily basis, marked to market at COB
>   - earned a profit, get put into a futures account

![alt text](assets\IMG16.PNG)

### Remark
- The above process is often called daily settlement.
- There may be intraday settlement and margin calls.
- You’re free to use the excess funds in your margin account over and above the maintenance margin.
- Daily settlement is the main way exchanges protect themselves against counterparty risk:
- The maintenance margin is typically less than the maximum allowable daily fluctuation or variation in the contract price.
- If the daily variation limit is hit, a circuit breaker or trading halt occurs and all margin accounts are marked-to-market.

> - only if large moves in the market

![alt text](assets\IMG17.PNG)

> - they won't do anything unless there is money in the margin account
> - far less counterparty risk


### Leverage Effect

Leverage effect: Your profit/loss as a percent of the initial margin.
- The danger with futures is you post only the initial margin upfront:
- Long position: You don’t post the full amount K upfront.
- Short position: You don’t need to own the underlying asset.

![alt text](assets\IMG18.PNG)


> Don't actually have to post the contract:
> - only post the initial margin
> - have a massive exposure

![alt text](assets\IMG19.PNG)

Contract value
Another important concept is the value of a futures/forward position at a
given point in time t that was entered into at time $t = 0$. Suppose you:

- Go long h contracts at time $t = 0$ for K.
- Close your position at time t by shorting h contracts for $K_{t}$.

The cashflow $h(K_{t} − K)m$ locked in at the delivery date is risk free. With
$r$ the risk-free rate, the value at time t of a *long* position is

$$V^{long}_{t} = e^{-r(T-t)}\cdot h(K_{t}-K)\cdot m$$

The value of a short position is thus $V^{short}_{t} = e^{-r(T-t)}\cdot h(K- K_{t})\cdot m$

> - priced so that they initially have 0 value
>   - no initial exchange of cash flows

### Examples, hedging, speculating
We now cover pricing, speculating and “perfect” hedging with futures contracts over the following general classes of underlying assets:
1. Commodities.
2. Equities:
  - Individual shares and ETFs.
  - Share indices.
3. Currencies.
4. Simple money market interest rates:
  - FRA.
  - BAB futures.

> - main classes of futures and forwards

### Commodity futures
Commodity futures are contracts to trade an agreed quantity m
(and grade/quality) of a commodity for the contract or forward
price K at the maturity or delivery date T.


Futures are written on all kinds of commodities:
- Metals: Gold, silver, copper, aluminium, platinum, nickel, tin, etc.
- Energy and environment: Gas, oil, coal, electricity, carbon, etc.
- Agriculture and food: Beef, pork, milk, wheat, rice, corn, soy, sugar,
cocoa, coff ee, orange juice, wood, fertiliser, etc.

Many commodity futures are physically settled (but of course can be
closed out prior to maturity). Some trading volume statistics:

> - most commodity future contracts are physically settled
>   - don't close out, have to physically trade to collect commodity

### Commodity futures “perfect hedging”
To use futures to hedge an exposure to the underlying asset:
- Go long to hedge against prices going up.
- Go short to hedge against prices going down.

### Example
You want to buy 20 metric tons of soda ash in September in China, and don’t want to risk soda ash prices going up.
- To lock in a purchase contract price of K = 2, 023 CNY/ton (≈ $420/ton) you go long h = 1 September futures contract.
- On the 10 th trading day of September, you buy 20 tons of soda ash for $h × K × m = 40$, 460 CNY (about \$8, 371).

> lock in the price (either buying or selling) with a futures contract
> - using a contract to lock in a certain price, so you are not exposed to price fluctuations in the future

### **Remark** We call this “perfect hedging” since:
- The underlying asset in the contract is exactly the asset exposure we want to hedge.
- The number of units in the underlying asset we want to hedge is covered by an integer number of contracts.
- And our hedge date is exactly the contract delivery date. But things are rarely this “neat” in reality so next week we cover the notion of optimal hedging.

### Commodity futures speculating

To use futures to *speculate* on the direction of the underlying asset:
- Go *long* if you expect prices to go up.
- Go *short* if you expect prices to go down.
Suppose you go long h contracts at time $t = 0$ at K, and then closed it
out at time $t > 0$ by shorting h contracts at $K_{t}$. Your payoff at time t is

**Long Position payoff**
long position payoff = $h(K_{t} − K)m$

**Short Position payoff**

short position payoff = $h(K - K_{t})m$

### Equity futures

- Share and ETF futures are contracts to trade a quantity m of shares in a company or ETF for the contract price K at maturity T.
- Share index futures are contracts to trade a “share market index” for the contract price K (in units of the index) at maturity T.
  - The notional or face value of a share index futures contract is calculated as F = K × m, where m is the multiplier.

Individual share and ETF futures are typically physically settled but share index futures are usually cash settled (not possible to “trade a whole share index”, but ETF futures eff ectively enable this). Market statistics:

> a little bit more strange, organising to buy/sell a share market index
> - not a monetary value, value of the index
>   - multiplier m
>   - contract value is the dollar value of S&P500 e.g.
> - physically settled

### Example

You manage an ETF that tracks the S&P 500 Index but also
allows you to use futures contracts to hedge against market falls.
You’re worried that the index is in bubble territory.

![alt text](assets\IMG20.PNG)

You hold equivalently 5,000 units in the index, at a value of
$ 28,169,550. You short h = 100 December E-mini S&P500
contracts for a total exposure of h × K × m = $28, 740, 000.

Suppose the index falls 20% by December to S T = 4, 507.

In December, your ETF’s value fell to $ 22,535,000. Your futures
cash payout is h(K − S T )m = $6, 205, 000. Hence, your fi nal
position is $28, 740, 000. This is more than your original ETF
value of $ 28,169,550, and is due to the basis:

- Initially, S = 5, 633.91 and K = 5, 748.
- The initial basis is B = K − S = 114.09.
- At maturity K T = S T = 4, 507.
- The fi nal basis is B T = K T − S T = 0.

> - optimal hedging - minimise the basis risk


### Equity futures speculating

The above example shows what happens if you shorted h = 100
December E-mini S&P500 contracts and the S&P 500 did fall, in
line with your expectations. Your profi t is $ 6,205,000. But:
- If you were long, hoping for the index to keep going up like it
has been, you would have lost this amount. Leverage:
- The initial margin is ≈ 5% so ≈ $1, 437, 000.
- The loss wrt a long position’s total exposure is ≈ 22%, with
the extra 2% over the index fall due to the basis.
- Wiped out your initial margin 3 times over if you were long.

### FX futures
Foreign exchange (FX) futures are contracts to exchange an agreed
quantity of m units in one currency A for another currency B for the
contract price (forward exchange rate) K A:B at maturity T.

Our *quoting convention* for exchange rates is 1 unit of currency A
exchanges for K A:B units of currency B. We then have that 1 unit
of currency B exchanges for K B:A = 1/K A:B units of currency A.

The following market statistics show that there’s quite a lot of FX futures
(and options) trading volume on the NSE of India:

> - careful what we mean by an exchange rate

### Remark - FX futures
One way to think about these FX futures quoting conventions is
that the foreign currency is being viewed as the “underlying
asset”. Thus the futures price K USD:INR is telling us how much
Indian Rupee it “costs” to buy 1 unit of the underlying asset.

### Example - perfect hedging
You’re an exporter from India who sells in the USA, receiving USD payment. You’ll be receiving $ 1,000,000 in September and want to lock in the USD:INR exchange rate to get Indian Rupee.
- Short h = 1, 000 26-Sep-2024 USDINR futures for a forward exchange rate of K USD:INR = 83.7925.
- One contract is for m = $1, 000 so on 26-Sep-2024 you get F = K USD:INR × m = 83, 792.5 INR per contract, so h × F = 83, 792, 500 INR in total.

> - In the national stock exchange in INdia

### FX futures speculating Example
In the above example you took a short futures position, which is
what you’d do if you believed the USD will depreciate against the
Rupee. Suppose that it did and to S T,USD:INR = 80. Your profi t is

h(K USD:INR − S T,USD:INR )m = 3, 792, 500 INR.

If you were long then this would be a loss.

### Interest rate contracts

We now present two simple interest rate contracts:
- Forward rate agreements (FRA), which are OTC interest rate forward contracts over some global reference rate.
- 90 Day Bank Accepted Bill (BAB) Futures, which are an Australian ASX traded futures equivalent of a FRA over the BBSW rate.

> yield curve, interest rate quoted over the next six months
> - work out what the implied forward rate over a period
>   - lock in interest rate over that period
>   - must have the same final price
> - forward rate agreements, lock in implied interest rate

## Forward Rate Agreements (FRA)

A forward rate agreement (FRA) is a OTC traded forward contract over a reference interest rate such as SOFR or EURIBOR.

In an FRA the parties agree to fix an interest rate $k$ over an agreed
notional value F for an agreed time period $T$ starting on the FRA’s
agreed maturity date $T_{1}$ and ending on $T_{2} = T_{1} + T$.

FRA fix a simple interest rate k to begin at maturity $T_{1}$ for borrowing or
lending over the time period $[T_{1}, T_{2}]$ of length T, but are cash settled, so
no actual borrowing or lending takes place at time $T_{1}$ .
- A FRA’s payoff at maturity $T_{1}$ depends on the difference $k − r$,
where $r$ is the spot reference rate at time $T_{1}$ for the period $[T_{1}, T_{2}]$.

> - fix an interest rate, a loan or investment over a given period
>   - loan or investment, starts on the maturity
> Get to the maturity date at the enf of the year
>  - go long, hypothetical investment over that period
>    - organising at maturity date, the interest rate you would receive
>
> Payoff
> - interest rate you agree to, versus the spot reference rate (the spot rate at a future time t)


Pricing an FRA involves calculating the agreed upon rate k, which we call the fixed rate , and we cover this next week. Using this terminology:
- Being long an FRA involves locking in k as a lending or investment rate, and this party is called the fi xed rate receiver.
  - Think of this as agreeing to lend or invest F at maturity, time T 1 , and thus to receive the investment proceeds F(1 + kT) at time T 2 .
- Being short an FRA involves locking in k as a borrowing or funding rate, and this party is called the fi xed rate payer.
  - Think of this as agreeing to borrow F at maturity, time T 1 , and thus to pay off the loan amount of F(1 + kT) at time T 2 .

> - long party - fixed rate receiver
>   - earn interest on an investment