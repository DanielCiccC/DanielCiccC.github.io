# Lecture 5 - Hedging Transaction Exposure

Risks firms face include:
- Interest Rate risk
- Relative Price Risk
- Political/Geopolitical Risk
- Exchange rate risk – “is the variance of domestic-currency value of an asset, liability, or operating income that is attributable to unanticipated changes in exchange rates.” (Adler and Dumas, 1983)

> **Relative price risk**
> Price the goods that they sell
> 
> price of inputs are changing, can have impact on profitability
> - E.g. airlines and jet fuel
> **Political/geopolitical risk**
> - When political parties change, can bring uncertainty to operations
> - geopolitical - e.g. middle east, seizing ships going through the red sea


### Types of Foreign Exchange Exposure
- Unexpected changes in exchange rates may affect a firm’s cash flows and market value 
  - either through its effect on existing contracts -> **Transaction Exposure** 
  - or through its impact on the future operating cash flows of the firm -> **Operating Exposure** (aka Economic Exposure)
- Exchange rate changes may have an impact on accounting values
  - This is called Accounting Exposure or **Translation Exposure** 

> Unanticipated changes in the exchange rate has on the cash flows
> - in the international market, have cash flows in the future need to be forecasted in the future
>   - changes in the future cash flows can ultimately affect the project's value
> - not covering translation exposure

### Transaction Exposure
- Transaction exposure measures gains or losses that arise from the settlement of existing financial obligations (e.g., account receivables, account payables) whose terms are stated in a foreign currency.
- A classic example of transaction exposure is a firm that has signed a contract to ship goods overseas at a fixed foreign currency price.

> Enter into agreement to ship goods, on delivery have to convert to AUD
> - concerns about downside risk

#### Example
Suppose an Australian firm sells merchandise on open account to Belgian buyer for:

- €1,800,000, payment to be made in 60 days. 
- S0 = $0.9000/€
- The Australian seller expects to exchange the €1,800,000 for $1,620,000 when payment is received
- *Transaction exposure arises because of the risk that the Australian seller will receive something other than $1,620,000.*
- If the euro weakens to $0.8500/€, then the firm will receive $1,530,000
- If the euro strengthens to $0.9600/€, then it will receive $1,728,000

### Sources of Transaction Exposure
- Transaction exposure arises from:
  - Purchasing or selling on credit goods or services whose prices are stated in foreign currencies; 
  - Borrowing or lending funds when repayment is to be made in a foreign currency; 
  - Being a party to an unperformed foreign exchange forward contract; 
  - Otherwise acquiring assets or incurring liabilities denominated in foreign currencies.

> - Australia issues a bond in the American debt market
>   - payments made in US dollars

### Transaction Exposure

![alt text](assets\IMG100.PNG)

Net Exposure by currency and date = Total Inflows – Total Outflows 

> Total exposure - net the inflows and the outflows
> - receivables - payables

### Measuring Exposure: Value-at-Risk
- Aim: To estimate the potential loss in value due to adverse exchange rate movements over a defined horizon with a specific confidence level.
  - Regulators use Value-at-Risk (VaR) to compute capital requirements for financial institutions (e.g., Basel II) 
  - Typical confidence level is 99% or 95% focusing on the 1% or 5% worst case scenario.
- Blue Bossa Records has €10m receivable. The current spot rate is \$1.20/€ in 30 days. What is its VaR?
  - Need to specify reference probability and horizon
  - Need an estimate of the distribution, e.g., Normal distribution with μ = 0 and σ = 6% per month

> Banks - specify what the value of the risk is
> - 'how much can I lose with x%' over a certain horizon
>   - use confidence interval - 95% chance etc.


### Measuring Exposure: Value-at-Risk

- With the normal distribution, the 5% tail probability of adverse move starts at 1.645 standard deviation below the mean. 

![alt text](assets\IMG101.PNG)

$$μ – 1.645 × σ = 0 – 1.645 × 0.06 = -0.0987$$

- For the $12m position, VaR is -0.0987 × $12m is: –$1,184,400 
[i.e., there is 5% chance of losing $1,184,400 over the next 
month].
  - VaR = portfolio value x critical value (1 or 5%) x $\sigma _{t+1}$

> Gives you an idea of how much to hedge
> - now only 1,184,400

### Hedging Transaction Exposure
- Transaction exposure can be managed by contractual, operating, and financial hedges:
  - Contractual Hedges employ the use of 
    - Forwards/futures, Options, and Money Markets
  - Operating and Financial Hedges employ the use of 
    - Risk-Sharing Agreements, Leads and Lags in Payment Terms, Swaps and Other Strategies

### Contractual Hedging Techniques
- Forward/Futures Hedge 
     
- Currency option hedge
  - A way to hedge contingent exposure
- Money Market hedge: Taking a money market 
position to hedge future receivables/payables
         
- Structuring the Hedge 
  - exporters (sell FOREX, buy AUD) - receivables
  - importers (buy FOREX, sell AUD) - payables

> Main differences forwards/futures - forwards are OTC
> - options contract; can walk away from the options contract (lapse) if a dollar appreciates
> - Entering a tender for a contract in a foreign country; using an option to set the exchange rate would not make sense
> Structuring the hedge:
> - exporters have receivables that are denominated in a FC
>   - buy FC and sell AUD
> - importers have payables
>   - need AUD to buy FC

### Hedging FC receivables:
- Sell futures or forward 
(Go short) 
- Buy Put Option      
- Money market hedge
  - borrow foreign currency to be received
  - convert to domestic currency
  - invest for future use


### Hedging FC Payables
   
- Buy futures or forward (Go long) 
- Buy Call Option 
- Money market hedge
  - borrow home currency 
  - convert to foreign currency
  - invest for future use

> buying FC in the options market


### Using Futures to Hedge
- You have sold widgets in February -- contracted to receive €250,000 in mid-March
  - What’s the risk? 
- Hedge by acquiring a liability whose value is equivalent to the value of the underlying receivable.
- The following prices are observed:

![alt text](assets\IMG102.PNG)

- Your company sells two (2) March futures 
contracts. (why?)
- The final cash flows in mid-March is
  - Sells the euro receivables in the spot market in March. The cash flow is 
    - €250,000 × $1.35/€ = $337,500
  - The futures contract has **lost money** as the € has appreciated.
    - [($1.23/€) – ($1.35/€)] × €250,000 = -$30,000
  - The total cash flow from the € receivable:
    - $337,000 – $30,000 = $307,500

### Hedging with Options
- Recall, options give the option holder *the right, but not the obligation* to buy or sell a specified amount of the underlying asset (currency) at a pre-determined price.
  - **Premium is paid in advance** by the buyer to the seller.
- In the context of hedging, these contracts can be viewed as exchange rate insurance written against adverse exchange rate movements – options are written on the spot rate.
  - FOREX call options on spot can be used as insurance to establish a ceiling price on the home currency cost of foreign exchange. 
    - Ceiling Price = exercise price of call + call premium
  - FOREX put options on spot can be used as insurance to establish a floor price on the home currency cost of foreign exchange.
    - > minimum price to sell to an entity
    - Floor Price = exercise price of put – put premium


### Options Example
- As an importer of Swiss watches and you have to pay in the exporter’s currency (CHF).
- Payment of CHF750,000 is due on June 15. The following information is available
  - Spot rate: 71.42ȼ/CHF
  - Three-month forward rate: 71.14ȼ/CHF
  - Australian dollar three-month interest rate:  3.75%
  - Swiss Franc three-month interest rate:  5.33%
  - Option data for June contracts (ȼ/CHF):

![alt text](assets\IMG103.PNG)

- The concern is that CHF will strengthen against 
the \$.
- Should you use call or put? 
  - Buy the option that gives the right but not the obligation to buy CHF.
- Cash Flow today: Pay option premium of 
  CHF750,000 × $0.0155/CHF = $11,625

![alt text](assets\IMG104.PNG)


![alt text](assets\IMG105.PNG)

Finding S*, the future exchange rate, where the cost of both hedges are EQUAL
[S* + \$1.56ȼ/CHF] = 71.14ȼ/CHF

S* = 71.14ȼ/CHF – /$1.56ȼ/CHF = 69.58ȼ/CHF

> downsides of options contracts - trades on an exchange
> - may not be able to use options contract

### Money Market Hedge
- Assume Boeing is expected to receive 10m 
GBP (£) in one year's time
- Available Information:       
  - one-year forward rate: US$1.46/£
  - spot rate: US$1.50/£
  - put option on pounds with strike of US/$1.46 has a premium of US/$0.02 (i.e. 2ȼ)
  - interest rates:
    - US: 6.10% per annum
    - UK: 9.00% per annum

- Money Market Hedge:  Borrow (or lend) in the 
foreign currency to hedge its foreign currency 
receivables (payables) – match foreign currency 
assets & liabilities in the same currency
1. Borrow the PV of £10m = $\frac{10}{1.09} = 9,174,312 \pounds$
2. Convert £ into $ at $1.50/£  ($13,761,468 )
3. Invest $ in the US at 6.10% for one year 
( $13.761𝑚 × 1.0610 = $14,600,918 )
1. Collect £10m in one-year and repay the loan (the £ 
receivable offsets the loan)


### Alternate Hedging strategies

- Risk Shifting
- Leading and Lagging – used to manage net working capital needs of foreign affiliates
  - Leading is to accelerate timing of receivables/payables denominated in depreciating currency
  - Lagging is to delay timing of receivables/payables denominated in depreciating currency
- Currency Risk Sharing
- Cross-hedging
- Currency diversification

> Risk sharing - share the risk of unanticipated interest rate changes.
> - If the exchange rate reaches the agreed band when a second contract may come into place
> - Cross-hedging - use a second currency to hedge as long as the secondary currency is highly correlated
>   - use forward contracts in that instance
> - Currency Diversification
>   - maintain so many currencies that their contracts will cancel out interest rate risk
> - Leading and lagging

### Why Hedge
- Hedging is the taking of a position, either acquiring a cash flow or an asset or a contract (including a forward contract) that will rise (fall) in value and offset a drop (rise) in value of an existing position. 
- Hedging, therefore, protects the owner of the existing asset from loss (but it also eliminates any gain resulting from changes in exchange rates on the value of the exposure).  


## Impact on Hedging on E(Cash flows)

![alt text](assets\IMG106.PNG)

Hedging reduces the variability of expected cash flows about the mean of the distribution.
This reduction of distribution variance is a reduction of risk.
> protect yourself by minimising the risk of extreme movements in exchange rates

### Adjusted NPV View of the World
- Reducing the uncertainty of future cash flows by 
hedging is problematic

![alt text](assets\IMG107.PNG)

- If goal is to maximize shareholder value, then hedging 
only makes sense if it INCREASES equity value

> Adjusted NPV - add/subtract of the project's cash flow
> - figure out what the value of the transaction will be
> - In a world with taxes of frictions, you only participate in hedging if it increases the NPV of the transaction

### Views of Hedging
Is the reduction of variability of cash flows then sufficient 
reason for currency risk management? 
- Opponents of currency hedging commonly make the following arguments:
  - Stockholders are much more capable of diversifying currency risk than the management of the firm. 
  - Currency risk management does not add value to the firm, and it incurs costs (i.e., it is costly).
  - Hedging might benefit corporate management more than shareholders. 
  - Management’s motivation to reduce variability is sometimes driven by accounting reasons.

> - Only risk that matters is idiosyncratic risk
> - if the risk is systematic, it makes a lot of sense
> - Hedging is expensive; margin calls etc.
> - Argument is that investors should be hedging themselves
> - If you don't hedge, potential to make huge losses
>   - obvious when you make a loss - have to question the management's motivations


### Proponents of Hedging
- Proponents for currency hedging argue: 
1. Risk Profile of Investments (Agency Costs)
- Shareholders hold an option on the value of the firm and would prefer riskier projects.  
  - Since, riskier projects reduce the value of bondholders’ claims, bondholders are likely to require compensation in the form of a higher returns.
  -  If shareholders can credibly commit not to unduly increase risks, a lower cost of debt financing could result.
- Additional sources of agency costs come from managers’ preference for less risky projects (job security).

![alt text](assets\IMG108.PNG)

> Agency costs will drive the decision
> - transaction costs argument; cheaper for large investment company to hedge than retail investor

2. Reduction of risk in future cash flows reduces the likelihood that the firm’s cash flows will fall below a necessary minimum (and put the firm in financial distress).
3. Reduction of risk in future cash flows improves the planning capability of the firm.
  - If the firm can more accurately predict future cash flows, it may be able to undertake specific investments or activities that it might otherwise not consider.  
4. Individuals and corporations do not have same access to hedging instruments or same cost.