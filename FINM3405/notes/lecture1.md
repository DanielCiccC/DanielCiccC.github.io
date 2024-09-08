# Lecture 1 - Introduction to derivative markets


## Derivatives
- main instruments that are traded
- sophisticated and complex

### Derivative securities facilitate the management of risks that arise when:
- The financial system performs its core function of transferring savings and investment funds to long-term investments in real assets.
- Businesses simply go about their usual day-to-day trading activities.

![alt text](assets\IMG8.PNG)

> - Transfers money through the economy
> - Make investments in real assets in the economy
> - Has a large impact on what products and services are sold in the economy
> - Banks funnel money into businesses that produce economic growth - if they produce value and consumers purchase from them
>
> **In the process of the main function of the financial system:**
> - Apple has to pay wages in Chinese yuan - products/services exposed to risks, exchange rate risks, interest rate risk
>
> Derivative securities can offload risk to other players, whose job is to manage those risks
> - reallocation of risks through the economy

### Vanilla derivatives and payoffs

A derivative security is a contract between two or more counter-parties specifying one or more future transactions that are dependent on (are “derived” from) other underlying assets. 

- **Futures and forwards**: Contracts obligating the parties to trade the underlying asset for an agreed price on a future date.
- **Options**: Contracts giving one party the right but not the obligation to trade the underlying asset for an agreed price in the future.
- **Swaps**: Contracts involving the exchange or “swapping” of future cashflow obligations or risk exposures between the parties.

> Some sort of contract at trade in financial markets (counterparties)
> - payoff depends on some kind of underlying assets - underlying events
> - events can even be weather, or similar to betting events

![alt text](assets\IMG1.PNG)

> forward commitments
> - each side of the party that they have to honor
>
> contingent claims
> - whether there is some sort of claim in the contract is contingent on the outcome of the event


- Derivative securities can be negotiated directly between parties OTC, or standardised contracts traded on trading venues:
- Traditional exchanges, multilateral trading facilities (MTF) in Europe, and alternative trading systems (ATS) in the US.
- Underlying assets include physical assets, financial securities or instruments, financial market indices or other variables, currencies, commodities, energy, other derivatives, etc.
- The underlying assets can be physically deliverable in the contract, or the derivative security can be cash settled with no physical delivery of the underlying asset ever taking place.

We now give a brief description of the above basic classes of derivatives:
- futures/forwards, options and swaps.

> OTC:
> - Individual financial institutions negotiating directly with very little regulation
> - no centralised trading facility
>
> Can be physically delivered:
> - e.g. buy 20 tonnes of wheat

## Futures and forwards

``Defn``

Futures and forwards are contracts obligating two parties to trade
an agreed quantity of the underlying asset for an agreed contract
price K on an agreed future date T (the maturity date).

The basic difference between futures and forward contracts is:
- Futures are standardised contracts traded on trading venues.
- Forwards are negotiated between the parties in OTC markets.

The party agreeing to *buy* the underlying asset is said to be taking a **long**
position. The party agreeing to *sell* the underlying is said to be **short**.

> - futures, trading on exchanges
> - forward contract, negotiated directly between OTC markets

At maturity T, the long party buys the underlying asset for $K$. If $S_{T} > K$ at maturity, then the long party has benefited by the amount $S_{T} − K$.

But if $S_{T} < K$ at maturity then the short party, who sells the underlying asset for K, has benefi ted by the amount $K − S_{T}$.
-  Hence, the payoffs to the long and short parties are:

long payoff = $S_{T} − K$ and short payoff= $K − S_{T}$ .
We plot these payoff s graphically as follows:


$S_{T}$ : spot price at time T
$K$: Contract price

![alt text](assets\IMG2.PNG)

## Options

There’s two basic types of option contracts, namely call and put options:

The *holder* of a European **call** option has the *right but not the obligation to buy* an agreed quantity of the underlying asset for an agreed strike price K on an agreed future date T (expiry).

The *holder* of a European **put** option has the *right but not the obligation to sell* an agreed quantity of the underlying asset for an agreed strike price K on an agreed future date T (expiry).

Note that an American option gives the holder these rights to exercise an option at any point up and including the expiry date T.


- The holder of an option is also called the taker, and is said to be **long**.
- The other party to the contract is called the writer and said to be **short.**

The writer has “no rights” and is “at the mercy” of the holder if the holder decides to exercise the option at expiry (European options)

or anytime up to and including expiry (American options):
- Call option: The writer must sell the underlying asset if the taker exercises their right to buy it.
- Put option: The writer must buy the underlying asset if the taker exercises their right to sell it.

> write or sell an option: choose whether the option gets sold or not.

### Expiry - call

At expiry $T$, the call option holder has the right but not the obligation to buy the underlying asset for $K$. If $S_{T} > K$ at expiry, then the holder has benefited by the amount $S_{T} − K$ and will exercise the option. But since the holder has no obligation to exercise the option, if $S_{T} < K$ at expiry, then the holder doesn’t exercise it and simply lets it expire worthless.

- Hence, the European **call holder’s payoff** at expiry is call holder payoff = ``max``${0, S_{T} − K}$. 

The call writer’s payoff is the negative of this.

![alt text](assets\IMG3.PNG)

### Expiry - put

At expiry $T$, the put option holder has the right but not the obligation to sell the underlying asset for $K$. If $S_{T} < K$ at expiry, then the holder has benefited by the amount $K − S_{T}$ and will exercise the option. But since the holder has no obligation to exercise the option, if $S_{T} > K$ at expiry, then the holder doesn’t exercise it and simply lets it expire worthless.

- Hence, the European **put holder’s payoff** at expiry is put holder payoff = max ${0, K − S_{T} }$.

The put writer’s payoff is the negative of this.

## Swaps

Swaps come in “all shapes and sizes” and in this course we focus on:
- Interest rate swaps.
- Foreign exchange (FX) swaps.
- Currency swaps.
- Credit default swaps.
- Possibly some others, time permitting.

### Interest rate swaps
A plain vanilla fixed-for-floating interest rate swap involves two parties swapping their existing loan payment obligations:

- One party swaps fixed-rate payments with floating-rate payments.
  - They have an existing fixed-rate loan but want to pay floating.
- The other swaps floating-rate payments with fixed-rate payments.
  - They have an existing floating-rate loan but want to pay fixed.

Hence, interest rate swaps can help businesses manage interest rate risk. Also, they enable a business to borrow at terms most favourable to them and then swap their loan to their desired interest rate exposure, thus helping the business to reduce borrowing costs.

> fixed a floating rate loan for a fixed rate loan
> - biggest financial market on the planet
> - also OTC
>   - can manage interest rate risk
>   - saves them from re-negotiating a loan

The mechanics of a fixed-for-floating swap can be described as follows:

- The parties continue to pay off their original loans as per normal.
- On each loan payment date:
- The parties calculate their new desired and contracted loan payments, as negotiated and agreed between them in the swap.
- One party exchanges a net amount to the other so that this exchange combined with their original loan payment results in them achieving their overall desired loan payment exposure as agreed in the swap.

Note that interest rate swaps are overwhelmingly traded OTC.

### FX swaps

A foreign exchange (FX) swap is an agreement to exchange one currency for another at an agreed rate on an agreed date and to re-exchange those two currencies at a later date at an agreed rate.

- They are typically used for exchange rate risk management. So in a FX swap you simultaneously agree to two transactions, namely an initial transaction and then a reversing transaction at a later date.
- The initial transaction can be spot or on a future date.
- If it’s spot then they’re typically called a spot-forward FX swap. 
 
  
FX swaps are negotiated and arranged OTC.

> - Very popular also

### Currency swaps

A currency swap is an agreement between two parties to swap interest payments on a loan made in one currency for interest payments on a loan made in another currency.

- Hence, each party has an existing loan in their respective currency, but now wants to make their loan payments in the other’s currency. A currency swap may also involve the parties exchanging the loan principal, which is then exchanged back at the swap’s maturity date.
- This is effectively a FX swap feature added to the currency swap. 

Again, only a net amount is transferred on each loan payment date:


The mechanics of a currency swap can be described as follows:

- The parties continue to pay off their original loans in their original currencies as per normal.
- On each loan payment date:
  - The parties calculate their new loan payments in their desired currencies, as agreed in the currency swap.
  - One party exchanges a net amount to the other which combined with their original loan payment results in them achieving their overall desired loan payment exposure in their desired currency.

> Swap their loan repayment obligations
> - Might involve swapping the initial loan amount
> - don't want to make the payment and loan in another currency, swap the loan altogether
> - both countries meet at loan payment dates
>
> E.g. country in australia
> - Want to borrow money in australia (easier) and then diversify and swap for a Chinese loan
 
Not only can currency swaps contain a FX swap feature, but they can also contain a fixed-for-floating interest rate swap feature:
- One party has borrowed at a fixed rate in one currency but now wants to now pay their loan at a floating rate in the other currency!
- The other has borrowed at a floating rate in their currency but now wants to pay off their loan at a fixed rate in the other currency!
This is termed a fixed-for-floating currency swap , and I think you get the idea of what fixed-for-fixed or floating-for-floating currency swaps are.

## Credit default swaps

A credit default swap is effectively an insurance contract between two parties in which one party purchases protection for a defined period of time from another party against losses from the occurrence of some credit event, usually default of a third party called the reference entity.
- The buyer pays the seller regular premiums, and in return receives a payout from the seller if the reference entity defaults.
  - Hence, credit default swaps help businesses manage credit risk, but they’re also used for speculation and arbitrage.
- They are negotiated and arranged OTC.

> default on loan, 
> - manage counterparty risk with credit default swaps


### Relative market sizes

![alt text](assets\IMG4.PNG)

> exchange relative to OTC


![alt text](assets\IMG5.PNG)

> Figure: Notional value outstanding of exchange vs OTC FX plus interest rate
derivatives (source: BIS).
> - OTC markets have amounts open to maturity
> - exchange markets are closed fart more frequently

### Breakdown data

- see slides

### Exchanges

![alt text](assets\IMG6.PNG)

> This growth is particularly due to the National Stock Exchange of India.

### OTC markets

![alt text](assets\IMG7.PNG)

From all these graphs we can draw the following conclusions:
- Interest rate and FX forwards and swaps dominate OTC markets.
- Share and share index options dominate exchange-traded markets.

We focus on these in FINM3405 Derivatives and Risk Management.

## Uses and market participants

Derivative securities have a number of different uses, and in general
financial markets have a lot of “moving parts” with different players and
participants all all doing different things:
- Trading, speculation and arbitrage.
- Risk management or hedging.
- Market making.
- Regulators and other industry bodies and associations.

### Traders and speculation
We saw above the different payoffs depending on the movement in the underlying asset from taking long and short positions in futures and options. Derivatives can be more efficient and cost effective means by which to speculate on movements in the underlying asset than trading the asset itself. Of course there’s a huge variety of trading strategies that various market participants employ to make a profit by trading derivatives. Derivatives also introduce other variables and factors that can be speculated on, over and above the movement in the underlying asset, including time, volatility, interest rates, credit conditions and spreads, market liquidity, weather, political events, you name it! Then you have the whole world of quant/algo/HFT/arbitrage/automated/etc trading, which nowadays is often very machine learning and AI driven.

> give you exposure to underlying asset, time to expire, underlying security, interest rates, credit spreads

### Risk management and hedging
This course focuses on introducing derivative securities in the context of
risk management. As mentioned at the start of this lecture, businesses,
governments, financial institutions, etc, are naturally exposed to a variety
of financial risks just by going about their usual daily business, including:

- Credit/default and counterparty risk.
- Market risks including adverse movements in interest rates, exchange rates, commodity prices, equity/share prices, etc.
- Government/political/sovereign risk, uncertainty and instability, including changing regulations, elections and military conflict.

In this course we present a number of basic techniques to manage some
of these financial risks using the derivative securities we cover.

### Market makers
Trading venues have contracts with companies called **market makers** to
provide liquidity in markets. Market makers, and dealers in OTC markets,
perform this liquidity function by continuously providing bid and ask
quotes in the market for other participants to trade at, thereby taking
one side of the transaction. Market makers typically earn a profit from
the bid-ask spread they quote, but they also engage in speculation and
proprietary trading, particular algo/automated/computerised. Some large
market makers include Susquehanna, Optiver, Jane Street, Citadel, DRW,
IG Markets, IMC, Flow Traders, etc; working for them is very lucrative

> - provide bid and offer quotes in the market
> - trade options in the market, e.g.

### Present value: Law of finance

Law of finance: The value of an asset is the present value of its
expected future cashflows.

There is really no other concept more important than present value.
When we value derivative securities, we spend quite a bit of time
constructing their future cashflows or payoffs and discounting them back
to the present in order to calculate their price. Note that for some
derivatives such as options, this involves some subtleties and
mathematical complexities, and the law of finance becomes what is
known as the risk-neutral approach to derivative security pricing.

### Arbitrage: Law of one price

The other central technique used and assumption typically relied upon to
price derivative securities is that of no arbitrage. A very common
approach or technique used in derivative security valuation is to construct
a portfolio of more basic securities (such as stocks, bank accounts, simple
forwards and futures, etc) which replicates the derivative’s future
cashflow structure or payoff. The assumption of no arbitrage leads to the:
Law of one price: Securities or portfolios with the same future
cashflow structure or payoff must have the same price.
If the law of one price is violated, then an arbitrage opportunity exists in
financial markets, which is assumed to be immediately exploited and
traded away. But what do we precisely mean by the concept of arbitrage?

> If you can set up two different portfolios that have the exact same payoff in the future, they must have the same price now or else as an arbitrage opportunity.

An arbitrage opportunity can be defined in various equivalent ways, and
the following two alternative definitions will suffice for this course:
1. An arbitrage opportunity is a scenario that has no initial, upfront
cashflow or exchange of money, no risk of future loss (negative
cashflow), but a chance of a future profit (positive cashflow).
  - Keep investing at 0 cost with the possibility of a future profit.
2. Alternatively, an arbitrage opportunity is a scenario of two different
portfolios or financial securities having the same future cashflow
structure or payoff, but different prices.
  - Long the cheap and short the expensive security/portfolio.
Neither of these scenarios can last long in efficient financial markets.

> current cashflows, 
> The other idea of arbitrage and arbitrage is a situation in which you have no upfront upfront payment.
> You have no risk or loss of loss in the future, but you have a chance of a positive gain of making a profit.
> That's an arbitrage, too. So I know in finance that you would you would have heard the definition definition of an arbitrage of trading simultaneously to different securities for a different price and immediately getting a profit.
