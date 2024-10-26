# Lecture 13
# Course Overview and Revision


### Lecture 1
- Basic defi nitions of:
    - Futures and forwards.
    - Options.
    - Swaps, including interest rate, currency and credit default.
- Differences between futures and forwards.
- Basic payoff diagrams of futures/forwards and options.
- Central, foundational, fundamental building block concepts on which
all of financial theory and practice are built:
  - Law of finance and present value (later became risk-neutral pricing).
  - No arbitrage and the law of one price.

> - forwards are OTC
> - futures have a precise mechanism
> - Need to know basic definitions and characteristics
> - profit/payoff diagrams, particularly in options
>   - include/adjust for the premium
> - Assume a risk neutral probability distribution
>   - No arbitrage argument
>   - LOOP - two portfolios (if one in the future) should maintain the same price


### Lec 2-3 Futures & forwards
- Definitions, differences and payoff diagrams of futures and forwards.
- Margin mechanism and leverage eff ect for futures.
- How to calculate the value of a futures/forward contract.
- The following for the main classes of futures and forwards in terms of the underlying asset, namely commodities, equities, currencies and interest rates (FRA and BAB futures):
  - Main contracts and their specifications.
  - Perfect hedging examples.
  - Basic examples of speculating on the price of the underlying asset.
- Contract pricing via the cost of carry approach.
- Basis risk and optimal hedging.


> - Leverage effect
> - Calculate the value of a futures contract at a particular time
>   - always have 0 value upfront, as the price change, your position may move in/out of your favour
> - Contract specifications - remember to look for the multiplier
>   - Contract multiplier will be given
> - futures and forward pricing, definitions
>   - optimal hedging examples
>   - Little quantitative calculations


### Lec 4-8 Options
- Definitions and concepts, including parties (taker, writer), vanilla types (puts & calls, European & American), asymmetric payoffs.
- Moneyness (ITM, ATM, OTM).
- Payoff s vs profits (including the premium).
- Main contracts and markets, contract specifications.
- Pricing bounds and put-call-parity.
- American call premium = European call premium when no dividends.
- Time value and intrinsic value.

> - Quite a decent proportion of the final exam on options
> - Taker, writer, buyer, seller
>   - Basic types, American puts and calls
> - Have a lot of quick little conceptual questions
> - Specifications of the contracts will be given
> - Pricing bounds - little calculation questions
>   - most are logical/common sense
> - Put/call parity formula (derive through an arbitrage argument, REMEMBER IT)
>   - Pricing bounds - premiums should be the same


- European option premiums/prices via the Black-Scholes model:
  - On non-dividend paying assets.
  - For dividend/income paying assets.
  - For currencies (simply viewed as dividend paying assets).
- Black-Scholes assumption of geometric Brownian motion and consequent log-normal distribution of the underlying asset’s price, or normal distribution of the asset’s returns.
- Simulating geometric Brownian motion in preparation for the Monte Carlo approach to derivative security pricing.
- Heuristic (non-rigorous) discussion of risk-neutral pricing.
- Heuristic (hand-waving) interpretation of the factors affecting option prices, and quantification of this via the Black-Scholes model Greeks.

> - know what each of the parameters mean
> - Work out the Z value from the table
> - distributions of the underlying assets returns
>   - prices are log-normally distributed
>   - Assumptions of the distributions of the returns in the black scholes model
>     - Are they normally distribution?
>     - Left skewness, fat tails etc.
> - Geometric Brownian motion
>   - Might simulate some paths
>   - might give us data of asset price paths, calculate price paths in an exam
>   - What is the price of an ATM call/put option e.g.
>   - European arithmetic average/final price
> - Haven't been given call/put options for lookback, 
>   - Maybe one or two of the list in the example tutorial
>
> The greeks
> - If market volatility goes up e.g., simple questions like that
> - Not the complicated ones, might ask to be calculated.

- Using delta ∆ and gamma Γ to predict small changes in option prices due to small changes in the price of the underlying asset (in preparation for delta and delta-gamma hedging).
- More detailed discussion of theta θ and associated concept of time
decay, and how it relates to moneyness.
- Basic ideas and examples of static delta hedging, static delta-gamma
hedging, and dynamic delta hedging.
- Implied volatility and the volatility smile and term structure, and
related VIX index enabling volatility to be directly traded.
- Trading strategies and their payoff and profit/loss diagrams.

> - Delta/gamma hedging questions
> - not realistic to ask questions on dynamic delta hedging
> - Basic questions may be asked
> - Implied volatility
>   - volatility smile - what does it mean? VIX index
>
> Trading strategies
> - on a bull spread e.g., what is the payoff?
> - Simple stuff around the basics, basic strategies
> - Know what a bear spread, etc

Options continued:
- Binomial and Monte Carlo numerical option pricing methods:
  - The need for numerical methods:
  - Price more complex derivative securities.
  - More complex pricing methods than the Black-Scholes model, in particular because returns are not normally distributed.
- 1-period binomial model for European option price and delta.
- Multi-period binomial model for European option price and delta.
- More rigorous introduction of risk-neutral pricing via binomial model.
- Monte Carlo pricing of European options.
  - Simple method that simulates only final asset price.
  - More general method that simulates entire asset price paths in preparation for Monte Carlo pricing of path dependent options.

> - representative in the practise exam
>   - All the i
>   - Will be given the values in the tree - will not be asked to build one
>   - Calculate their delta's
>   - choosers option IMPORTANT (given a tree)
> - Binomial risk-neutral probability
>   - work through the tree, use the risk-neutral approach to calculate the binomial prices in the tree
> - chooser options and other options with the binomial model
> - five asset price paths with a few dates - MAKE SURE YOU CAN DO THIS
>   - Will be given the tree or the asset price paths

### Lec 9 CDS
- Basic definitions and concepts for credit default swaps.
- More precise description of mechanics, including notions of:
- Analogy with insurance contracts.
- Parties: protection buyer and seller.
- Reference entity, assets and events.
- Payout, including physical vs cash delivery.
- Recovery rate and loss given default.
- CDS coupon or spread or premium.
- Single name vs multi name, basket, CDS indices.
- Idea that CDS spreads refl ect credit risk perceptions, and relation
between breakeven CDS spread and reference entity’s risk premium.
- Survival and default probabilities.

> - CDS calculations
>   - Table with dates, given survival prob, and default prob
>     - Breakeven CDS spread
>     - Upfront exchange of money
> - CDS spread increases
>   - Speculate in credit risk perceptions
>   - conceptual understanding of CDS - be prepared and understand them


- CDS pricing:
  - Calculating the breakeven CDS spread.
  - Or calculating the upfront cashflow given a fi xed CDS spread.
- Speculating and hedging with CDS.
- Idea that CDS opened up credit risk as “just another” asset class that can be directly traded, like VIX indices did for volatility.

> - Numerical options, credit rate swaps and credit default swaps

### Lec 10 Interest rate swaps
- Floating rate notes (FRN) definition, concepts and pricing in preparation for fi xed-for-fl oating interest rate swap pricing.
- Fixed-for-floating interest rate swap definitions and concepts.
- Calculating the net cashflows on each coupon or interest date.
- The idea that a position in a fixed-for-floating interest rate swap can be replicated via positions in a FRN and a fixed coupon bond.
- Interest rate swap pricing: calculating the fi xed rate.
- Hedging and speculating with interest rate swaps.

> - interest rate swaps question - representative of what is in the final exam

### Lec 12 VaR and ES
- Basic concepts relating to risk, including:
  - Types: market, default, liquidity, operational.
  - Portfolio expected return and standard deviation (volatility).
- Concepts related to the normal distribution in preparation for
calculating value at risk (VaR) and expected shortfall (ES).
- The need for simple, single measures of market risk like VaR and ES.
- VaR and ES definitions, basic concepts, and differences.
- Potential shortcoming of VaR and consequent need for ES.
- Calculating VaR and ES via 2 methods:
  - Parametric approach assuming normally distributed returns.
  - Nonparametric approach directly using historical data.
- Parametric portfolio VaR, worst case VaR, diversification benefits.

> - What is risk, calculate the portfolio
> - Worst case VAR, benefits of diversification
> - Proficient of normal distribution
> - VaR
> - Know how to use normal distribution
> - Why do we need VaR
>   - simple measures of risk
>   - Basic definitions and what they are
> - expected definition of VaR and expected shortfall?
>
> Parametric and non-parametric
>  - Calculate a parametric approach for a portfolio
> - non-parametric is not possible
> - no VaR formulas - need to remember these
> - confidence interval to the left of it
> - no portfolio VaR formula


<iframe frameborder="0" style="width:100%;height:102px;" src="https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=recap.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22AJVX2dEOV6ciYNKZwofG%22%3EjZJNb4QgEIZ%2FDccmKqnpuXbbXtoePHgmMiu0IC5i1f76Qh38yGaTnoBnPnlnCC309GJZJ94MB0WyhE%2BEPpEsS5P7xB%2BBzAvJ83QBjZUcnTZQyh%2BIkUgHyaE%2FODpjlJPdEdambaF2B8asNePR7WzUsWrHGrgCZc3UNa0kd2KhD%2FFbgb%2BCbESsnCZo0Sw6I%2BgF42bcIXoitLDGuOWmpwJUEC%2FqssQ937CujVlo3X8C4ALnjyyvms9LldeT1V%2Fvwx1m%2BWZqwA%2F3RoMTsm2wazdHKawZWg4hW0Lo4yikg7JjdbCOfvieCaeVf6X%2BinnBOphuNpyuMvj9gVDYzt4FA2iOyuHq0LgT4zaINKordkOIcQxn36ypN3n8BRWKz20Sf7bdPtPTLw%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E"></iframe>