# Revision, lecture 1 & Chapt 5 textbook

### Spot market
The	spot market	involves almost	immediate purchase or sale of foreign exchange
 Quoted in direct or indirect terms
 - Direct: Home currency per unit of foreign currency (FC)
 - Indirect: Foreign currency (FC) per unit of Home currency

$S(j/k)$ will refer to the price of one unit of currency $k$ in terms of currency $j$.

**Cross-exchange rate** is an exchange between a currency pair where neither currency is the U.S. dollar

### Bid-Ask spread
- Bid - the price in which the bank dealer will pay (buy) the currency for
- Ask - the price in which the bank dealer will sell the currency for

### Calculating the cross-exchange rate Bid-Ask spread
- use two direct or indirect quotes

$$S^{a}(\pounds / SFr) = S^{a}( \pounds / \$  ) \times S^{a}(\$/SFr)$$

- a direct bid is the reciprocal of an indirect ask
- a direct ask is the reciprocal of an indirect bid
![Alt text](assets\IMG88.PNG)

### Forward market
- Contracting today for the future purchase or sale of foreign exchange
- $F_{N}(j/k)$, the price of one unit of currency $k$ in terms of currency $j$ for delivery in $N$ months
- under certain conditions the forward exchange rate is an unbiased predictor of the expected spot exchange rate $N$ months into the future. 
  - Trading at a premium to the dollar in American terms, we can say the markets expect the US dollar to *depreciate* relative to the Swiss franc
  - When the dollar is trading at a *discount* to the Swiss franc, we can say the market expects the Swiss franc to appreciate, or become more valuable, relative to the dollar. It costs fewer francs to buy a dollar forward.

### Forward premium
- Express the premium or discount as an annualised percentage deviation from the spot rate

- There are three ways to express forward rates:
  - Via points to be added or subtracted from spot rate [known as swap points]
  - Outright quotes
  - As an annualized percentage forward premium or discount 


### Annualised percentage
Formula for calculating the forward premium or discount for currency $j$ over $N$ period in American terms is 

$$f_{N,j} = \frac{f_{N}(\$ /j)-S(\$/j)}{S(\$/j)}$$

3-month forward premium or discount for the Japanese yen versus dollar.

Current: .00897
3-month forward: .00903

$$f_{N,j} = \frac{0.00903 - 0.00897}{0.00897} \times \frac{360}{91} = 0.0265$$
three-month forward premium is 0.0265 

### Forward point transaction
 forward rates might be displayed as:

![Alt text](assets\IMG89.PNG)

- When the second known pair is smaller than the first, the dealer 'knows' the forward points are subtracted from the spot bid and ask price
- 
![Alt text](assets\IMG90.PNG)


### Over/under valuation:

| **Expected vs actual** | **Outcome** | **Reason** | Arbitrage profit
| --- | --- | --- | ---
Expected exchange rate (QC/BC) > actual exchange rate | - base currency is undervalued <br> - Quotation currency is over-valued | - You could be potentially earning more of the quotation currency given 1 unit of BC | - Buy the undervalued base currency <br> - Borrow/Sell the overvalued quotation currency 

### Triangular arbitrage
- Think of it in terms of the base currency. I.e., if the investment is in terms of $1M AUD, convert the cross rates to have an AUD base currency
  - Between the synthetic cross rate and the actual cross rate
- You will want to transact the most expensive cross rate first. Because the rates are in BC of the investment, you would multiple by the first investment, and divide by the second.

![alt text](assets\IMG200.PNG)

> - Risk free profit

### Is Arbitrage Risk-free?
However, when a mispricing occurs, strategies designed to correct can be risky
and costly, thereby allowing the mispricing to survive for a long time.

Example: A shares vs. H shares

What hampers arbitrage exploitation?
1. Fundamental risk
2. Noise-trader risk
3. Implementation costs


### Fundamental Risk

- If you think a stock is underpriced you can buy it, but:
  - You might be sideswiped by the market.
  - Or maybe by the industry.
  - Plus, there is idiosyncratic risk.
- Pure arbitrage seeks to eliminate all of these.
- Problem: you need to find perfect substitutes. Or we can say it is the risk when a perfect 
substitute is not available.
- Ex 1: Ford is overpriced. Sell Ford and buy GM? But is GM a perfect substitute for Ford? (next slide)
- Ex 2: Huaneng power (902) vs. Datang power (991) 

> - Perfect arbitrage should not have any risk


- Say Ford is too cheap.
- You buy Ford.
  - But market may drop.
  - Or auto industry may drop.
- So you buy Ford and short GM.
  - But Ford itself may falter without industry or market dropping (idiosyncratic risk) .
- Even you totally manage fundamental risk, there is still noise-trader risk: spread may 
widen as investors get it even more wrong.

> - Industry may drop
>   - Long short position to offset this risk (hedge)
> - didn't hedge unsystematic risk

### 2) Noise Trader risk
The idea is introduced by De Long et al. (1991) and Shleifer and Vishny (1997). 
(Noise trader risk is the risk that mispricing being exploited by the arbitrageurs worsen in the short run)
- It has been shown that noise-trader risk is systematic, which means that it cannot be diversified away.
- Real world arbitrageurs cannot wait it out because as professional money managers they do not have long horizons – they are usually evaluated at least at once per year.

**== > Three issues:**
- (1) Principal – Agent Problems (Horizon Mismatch Risk)
- (2) Creditor Risk (Margin Risk)
- (3) Short Squeeze Risk

> - If it becomes sentiment, has potential power to move market
>   - If we have large enough former sentiment, can move the market
>   - Noise traders can influence the market as well
>   - Biggest and bullish enough, can be profitable
>
> It is the **systematic risk**
> - Eventually price should still be corrected
> - Not all investors can wait it out
>   - Also take leverage, causing creditor risk/margin
>   - price increase, force managers to buy it back and lose money

### 3) Implementation costs
- In some cases, horizon is short but short-selling is:
  - Expensive (commissions, spreads, price impact & fees for shorting stock)
  - Difficult or even impossible (lack of availability regardless of fees; legal factors: many 
institutions cannot short)
Plus there is cost of finding these arbitrage opportunities.
- Transaction costs: commissions, bid-ask spreads and price impact can make it less 
attractive to exploit a mispricing.
- Legal constraints: many pension and mutual fund managers are not allowed for short 
sales. 
- Other costs: the cost of finding and learning about a mispricing and the cost of the 
resource needed to exploit it.

> A lot of resources, time and money
> - Add on top to why arbitrage is limited

### 3Com and Palm
- March 2, 2000: 3Com carves out in an IPO 5% of its subsidiary Palm.
- At same time, 3Com announced that in the near future the remaining 95% of the shares would be distributed to current shareholders (roughly 1.5 of Palm/share of 3Com).
- Two ways of buying Palm:
  - Buy Palm directly.
  - Buy 3Com getting Palm and rest of 3Com business.

- Background: Before 2000, 3Com owned Palm (via an acquisition of U.S. Robotics), a maker of handheld computers. 3Com was being ignored by the stock market during the Internet bubble period, especially compared to those sexy Internet companies.
- To gain the market recognition, on 12/13/1999, 3Com announced that it would sell a fraction of its stake in Palm to the general public via an IPO.
- In this transaction (called equity carve-out), 3Com retained ownership of 95% of Palm shares.

> - Palm going public
> - selling 5% to investors, or get shares through 3Com
>
> Buy 3Com, get both

![alt text](assets\IMG201.PNG)

> 3Com's price dropped by 21%


- “Smart” investors were limited in their ability to short-sell Palm (as documented in Lamont and Thaler), so it wasn’t their fault.
- But this cannot explain why anybody would buy Palm instead of 3Com – for this one needs irrationality.
- In facts 2 things are needed for mispricing to exist:
  - Irrational investors
  - Limits to arbitrage (here due to implementation costs)
- 3Com & Palm case illustrates that mispricing does not imply a free lunch!

> - Both limits to arbitrage we also need irrational investors to have mispricing
>   - no limits to arbitrageurs, can be corrected straight away 
> - know 3Com undervalued and Palm overvalued, have limits to perform arbitrage
>


### Conclusion


- There  are  investors  who  are  not  fully  rational. Furthermore, investors are deviated from rationality in a systematic and consistent way.
- The  systematic  and  consistent  irrationality  cause security prices deviated from their fundamental values.
  - However, arbitrage is risky and therefore is limited and  mispricing  may  be  worsened  before  getting 
better.
- Do not jump in the conclusion too early to assume that noise traders are the losers.
- Noise traders take on more risk and they need not die out and may make more profits.

> - Go is a systematic and inconsistent way
> - security price will deviate from fundamental value
> - arbitrage is risky and expensive
>   - Best price can get worse before it gets better
> - With that information, noise traders are not always losers - more willing to take risk
>   - Can outperform professional managers

![alt text](assets\IMG202.PNG)
