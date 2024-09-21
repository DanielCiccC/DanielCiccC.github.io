# Lecture 9
# Credit default swaps (CDS)

### Mechanics
This week we turn to the next section of the course covering credit
default swaps, interest rate swaps (along with FRN), and currency swaps.
All these instruments are negotiated and originated OTC and dominate
global financial markets on most measures of market size and activity.
This week we cover credit default swaps (CDS) and the material will be
very useful for your Team Project on Bill Ackman and Pershing Square.

> - spectulate in options
>   - hedge, hedge against the passage of time, volatility
>
> CDS, whole new asset class
> - credit risk (default risk)
> - speculating (hedging) government or soverign nation states defaulting on debt
> - Banks when you look at asset base, have to hold a certain amount of capital to cover their loans
>   - When banks could offload credit risk, increase their profitability

A credit default swap (CDS) is like an insurance contract in which:
- The CDS buyer “takes out insurance” against a credit event (e.g.
default) of a company or sovereign state and in return pays the CDS
seller a regular, fi xed “insurance” premium for the insurance.
- The CDS seller receives the CDS premium and agrees to pay the
buyer a compensation amount upon occurrence of the credit event.
- If the credit event occurs, the compensation is paid, the CDS buyer
pays the period’s accrued premium, and the CDS ceases to exist.
- If no credit event occurs, the CDS buyer keeps paying the periodic
premium until the CDS maturity date.
We now go into the details of CDS terminology, mechanics and pricing:

> Why is it called a swap?
> - swapping risk
> - Like an insurance contract
> - Take out insurance over some future event
> - Insuring yourself against negative credit event in the future
>   - Don't have to hold bonds to enter into credit default swap
> - Pay premium up to a certain date
>   - Have to finish paying for premiums to the seller
>
> Typically defined for 5 years
> - Premiums usually paid quarterly
> - A credit default swap buyer is called the protection buyer

- The CDS buyer is called the protection buyer.
- The CDS seller is called the protection seller or swap writer.
- The company or sovereign in the CDS is the reference entity.
- The particular debt securities (bonds, loans, floating rate notes, etc) of the reference entity over which the CDS is written are called reference assets or bonds or securities or obligations.
- The credit events relating to the reference entity’s reference assets as specified and defined in the CDS are called reference events.
- The “insurance” or compensation amount paid upon the occurrence of a reference event is called the CDS payout.

> - Bonds, loans, CDO's writing the CDS's over called reference entity
> - compensation amount is called the payout

The CDS can be single-name or multi-name:
- Above we’re referring to single-name CDS, which are written over
the reference assets of one single reference entity.
- Multi-name CDS, sometimes called basket CDS, are written over
the reference assets of multiple reference entities, and the nature of
their payouts can diff er (add-up basket, k th -to-default basket, etc).
There’s also CDS indices (see wiki), which are eff ectively basket CDS:
- The CDX range (also see Investopedia and the CDS Indices Primer).
- The iTraxx range (also see Investopedia and wiki). They’re important for your Team Project and we cover them later.


> - single name, reference asset is one individual country or asset
> - basket CDS written over a whole bunch of entities
> - Different payout structures in company CDS
> - CDS over a whole bunch of countries
>   - When one reference entity defaults, get the payout from the reference entity, 
>   - Company ceases to exist and exits the entity
>   - CDS stays in existence until maturity
> - Instruments making credit events an asset class you can trade
>   - In a major macroeconomic event, company expected to tank
>   - When the credit risk (prob default) payout to a CDS increase
>   - Hedge on macroeconomic events 


**Reference events** specified in a CDS include, but are not limited to:
- Default: Failure of the reference entity to pay interest/loan/coupon payments or the principal or face value of the reference asset.
- Bankruptcy: Official or legal/judicial administration, liquidation or winding up of the reference entity rendering it unable to meet, either partially or wholly, its obligations of the reference asset.
- Restructuring: Corporate or debt restructuring that changes the nature of the reference asset in terms of its original structure and the original agreement between the reference entity and its creditors.

> - Events that would cause a CDS to payout
> - international swaps and derivatives association, regulated and covered by ISDA
> - Company going bust - company going to be worth a whole lot less
> - Restructuring - anything that alters the original structure of the corporations debt


- Repudiation/moratorium: The reference entity disputing aspects
of or failing to recognise the reference asset and its obligations,
thereby disputing, delaying or refusing payment (common when the
reference entity is a sovereign or sovereign state).
- Covenants: The reference entity’s breaching or noncompliance with
debt covenants, including due to deterioration in financial position or
the devaluation or writing off of assets used as security/collateral.
- Ratings downgrade: The downgrading of a reference entity by a
credit ratings agency (such as S&P, Moody’s, Fitch, etc).

> - Repudiation/moratorium - dispute the fact that they have to pay the debt
>   - A lot of developing countries have done that
> - Covenants
>   - certain financial ratios, levels of health, etc. If the company breaches these obligations then that could be a reference event as well

**Remark**
An intuitive way to think about reference events is they could potentially be anything that materially changes the ability of the reference entity to meet its original obligations of the reference assets, and which therefore would materially or significantly reduce the market value of the reference assets. 
- It makes sense that creditors/lenders and other debt investors/holders may want to protect themselves against reference events, and they do this with CDS.

The idea of a reference event leading to a significant decline in the market value V of the reference entity’s reference assets leads to:

## Payout

The payout upon the occurrence of a reference event is defined as:

- A CDS is written over a notional principal or face value $F$.
- The protection buyer is taking out protection (“insurance”) over a
holding of the reference entity’s reference assets of total face value F.
- CDS can be physically deliverable or cash settled upon the
occurrence of a reference event (after which the CDS vanishes):
- Physical delivery: The protection seller agrees to buy the reference asset holding from the protection buyer at its total face value $F$. 
- Cash settled: The protection seller agrees to pay the protection
buyer the difference $F − V$ between the face value $F$ and the market value $V$ of the reference asset.

> - Precisely (quantitiatively)
> - Paid out over face value (can take up protection of the reference asset to a total principle of face value F)
>   - notional (no exchange of money takes place)
> - Either physically deliverable or cash settled
>   - Physically deliverable - e.g. if trading at about par, if a reference event occurs, value of the bond portfolio tanks, protection seller will buy at face value
> - Cash settled - Protection seller agrees to pay the difference between the FV and the value of the bond after the reference event
>   - would still get the full FV back

**Remark** Most CDS are cash settled. Also, in the theoretical treatment of pricing and hedging/speculating with CDS, there is no difference between a CDS being cash settled or physically delivered.
- So for simplicity we assume that CDS are always cash settled.

We define the important concept of the recovery rate R:
- It is the market value V of the reference asset expressed as a percent of the notional principal F after a reference event:

$$V = RF$$

> - Pricing CDS - the recovery rate
> - Think there is going to be a reference event, value of the portfolio is going to fall by a certain amount v 
> - Trying to predict the probability of default


- From another perspective, R tells us “how much we would recover” if we held a portfolio of the reference asset of total face value F and then sold it after a reference event occurred: We receive $V = RF$. It also follows then that the payout $F − V$ for a cash settled CDS is

$$\text{CDS payout} = (1 − R)F$$


**Remark** This payout $(1 − R)F$ is sometimes called the loss given default since it’s how much we’d lose on a holding of the reference asset.

The above illustrates one way in which CDS are used for hedging:
- Suppose you hold a portfolio of the reference entity’s reference assets (say bonds) of a total face value of $F$.
  - Suppose it’s roughly trading at par value, so $V ≈ F$.
- Upon the occurrence of a reference event (say a default), the market value of the reference asset falls to $V = RF$
  - It falls by an amount of $F − V = (1 − R)F$.
- The CDS then pays out this amount $(1 − R)F$.
  - It covers your loss upon the default of the reference entity.

> - $F-V$, how much the portfolio falls (loss given default)
> - not necessarily for their pay
> - perceptions of credit risk of a company changes
>   - value of the credit default risk changes
> - People are trading credit risk perceptions
> - Trading credit perceptions  of the market

The regular, fixed “insurance premium” paid by the protection buyer to the protection seller is called the CDS coupon or spread or premium.

- The premium is given as a percent $k$ of the notional principal:

$$\text{premium} = kFd$$

> - regular premium for being insured by a credit default swap

with $d = 1/2$ if semiannual premiums, $d = 1/4$ if quarterly premiums, etc. The market convention is premiums are usually paid quarterly.
- Here, $k$ is also called the CDS spread.

Question: Why is k called the CDS “spread”?

> - just like pricing a bond
> - usually paid quarterly
>
> Why is it called a spread?

**Answer**: Let $r$ be the risk-free rate, or a reference rate such as
Term SOFR or Euribor which are effectively risk-free rates. Also
let $y$ be the yield on the reference entity’s reference asset.
- Then $y − r$ is the reference asset’s risk premium or spread.
- Below we use arbitrage arguments to show that $k$ should
approximately equal this risk spread $y − r$ of the reference
asset over the risk-free rate, hence the terminology.

Furthermore, we will indeed show that the CDS spread $k$ reflects
the perceived credit risk of the reference entity’s reference asset:
- k rises (falls) when this perceived credit risk rises (falls).

> - spread of the companies yield over debt
> - If the company deteriorates, risk premium goes up, CDS spread reflects perceived credit risk of the company
> - When you are speculating on risk premium, hoping CDS spread goes up
>   - sell to a dealer and realise the profit

So CDS spreads $k$ reflect the market’s assessment of the credit or default risk of the reference entity.
- In fact, we can use CDS spreads trading in the market to deduce the implied probability of default of the reference entity (numerically, like deducing option implied vols). In the light, the World Sovereign Bonds website gives CDS spreads for sovereigns and their implied probability of default.

> - CDS created a new asset class called credit, can reverse engineer the implied risk of a company
> - CDS spread - of 20.30 basis points e.g.
> - In financial markets, what is the global risk free rate
>   - Calculating individual countires over a risk free rate in the global economy

## Pricing
We now turn to CDS pricing which involves determining the fair or theoretical CDS spread $k$. The general principal is:

The CDS spread $k$ is set so that the CDS has 0 initial value to both the protection buyer and seller (like futures and forwards) so no initial exchange of money takes place at origination.

Here $k$ is called the breakeven CDS spread. However, note that after the GFC, even though CDS are originated and traded OTC, their terms and specifications have been standardised, and in particular CDS indices are originated with a fi xed CDS spread k and an initial exchange of money usually occurs between buyer and seller (as per the Team Project).

> - Involves calculating the theoretical spread
>   - So that the CDS initially has 0 value
>   - No different to futures
>   - When you enter into it upfront, no exchange of cash flows
> - CDS indices bill ackman used have a standard spread, work out the initial amount of money that has to take place
>

So far we have the following CDS notation and terminology:
- F is the notional principal or face value.
- R is the recovery rate.
- k is the CDS spread.
- kFd is the CDS premium, where d is the time between
premium payments in years (say d = 1/4 for quarterly).
- (1 − R)F is the payout upon occurrence of a reference event.

For simplicity, we assume that the payout occurs at the end of the
premium period in which a reference event occurs.

> - If premiums are paid quarterly, CDS would end when a legally defined reference event occurs
> - buyer pays the accrued premium on the date
> - cashflows are paid on the payment date
> - Payouts and premiums are only paid on the payment date

- $t_1 , . . . , t_N$ is the premium payment and payout dates.
- $r_1 , . . . , r_N$ is the risk-free rate yield curve for these dates.
- $q_i$ is the (risk-neutral) probability of default in period i.
  - Probability of a reference event occurring in period i.
- $s_i$ is the survival probability up to time $t_i$ .
  - Probability that no reference event occurred up to time $t_i$.

> - Derive a risk-neutral probability distribution
> - $s_i$ probability that the credit default swap survives (hasn't vanished)


---
### Example

![alt text](assets\IMG191.PNG)
---

Risk-neutral law of finance : The price of a derivative security, including a CDS, is the present value of its (risk-neutral) expected future cashflows discounted at the risk-free rate.

From the perspective of the protection buyer:
- The regular premium payments $kFd$ are cash outflows.
- The payout $(1 − R)F$ is a cash inflow.

So the value of a CDS to the protection buyer is

> - Calculate the PV of future cash flows
> - Perspective of protection buyer
> - Potential payouts, value of the CDS is the PV of payouts and premiums

$$\text{CDS value = PV( E [payouts]) − PV( E [premiums])}$$

> - Once it pays out, you stop paying the premiums


PV of expected payouts: At time $t_i$ there is a payout of:
- (1 − R)F with probability q i .
- 0 otherwise.

Hence, the expected payout at time $t_i$ is

$$\mathbb{E}[payout_i]=q_i(1-R)F$$

and the present value of all of the expected payouts is

![alt text](assets\IMG192.PNG)


PV of expected premiums: At time $t_i$ there is a premium of:
- $kFd$ with probability $s_i$ .
- 0 otherwise (note that we’re ignoring any accrued premium).
Hence, the expected premium at time $t_i$ is

$$\mathbb{E}[premium_i]= s_ikFd$$

and the present value of all of the expected premiums is

![alt text](assets\IMG193.PNG)



The breakeven CDS spread k that which gives the CDS 0 initial value:

$$PV( E [payouts]) = PV( E [premiums]),$$

which we rearrange to get

![alt text](assets\IMG194.PNG)

We now give an example showing how the calculate the CDS spread k.

---
### Example cont.

![alt text](assets\IMG195.PNG)

> - In an examl situation, the question you would get
> - premiums paid quarterly, yield curve given
> - We will not go into survival probabilities
> 


![alt text](assets\IMG196.PNG)

> - At each quarter, a default probability 
> - Find PV of expected payoff's
> - Look at CDS spreads in assignment
>   - won't have reference events at the same time

> - Modelled the default correlation
>   - only for good econopmic times
>   - When the housing market when bust, an extreme event where everyone went bust
> - CDS spreads were so low because they were mispriced
>   - systemic event, 

![alt text](assets\IMG197.PNG)

> - CDS spread is 2.52%
> - How much premium would they have to pay over the life of the event
>   - What to they expect the payoff to be


## Pricing cont

We now present an example of CDS pricing in which the CDS spread is set to k = 1% (100 basis points), a common market convention. We calculate the upfront cashfl ow needed between the protection buyer and seller at the initiation of the CDS. I’ll use the same fi gures as above.

---
### Example

![alt text](assets\IMG198.PNG)

> - If it is positive it benefits the seller, and will need to pay to open the CDS
> - PV payouts is the same

![alt text](assets\IMG199.PNG)


### Speculation and hedging

We already mentioned an example of hedging with CDS:
- You hold a portfolio of debt securities, buy CDS protection on it,
and upon the occurrence of a reference event the CDS gives you a
payout to off set the reduction in your portfolio’s value.
CDS can also provide a hedge against, or enable you to speculate on,
macroeconomic or political events that impact market-wide credit risk
perceptions, as in the case study of Bill Ackman and Pershing Square.
- We give an example of this that may assist with the Team Project.

> - Hold a portfolio of  debt securities and buy protection
>  - give you the payout but the exact amount it falls by
> - credit risk perceptions


---
### Example

![alt text](assets\IMG200.PNG)

> - Probability of default increased (default probability spiked)
> - A company, or a basket of companies
> - how could they close it out and earn a profit?


![alt text](assets\IMG201.PNG)

> - Assume recovery rate is the same, may not be
> - expected payout went up because default probability went up

![alt text](assets\IMG202.PNG)

> - Macroeconomic event occurs and economy changes
> - Value of CDS position increases
> - Speculating on the probability of default credit risk perceptions
>   - Calculate the breakeven CDS spread also


So the point of this example is:

- There was a large macroeconomic shock.
- Default probabilities, consequently breakeven CDS spreads, spiked.
- CDS spreads went from 252 basis points to 1025 basis points.
- The buyer made a large profit upon closing out the CDS position.
- This profit could be used to off set losses on say a share portfolio, like Bill Ackman did at Pershing Square (using CDS index).
- Alternatively, this is an example of how CDS can be used to speculate, like Michael Burry did during the GFC:

> - Used to speculate and make money

**Remark**

Now possibly revisit Michael Burry’s GFC CDS trade, in which he
purchased CDS on mortgage backed bonds. “On May 19, 2005,
Mike Burry did his fi rst subprime-mortgage deals. He bought $ 60
million of credit-default swaps from Deutsche Bank— $ 10 million
each on six diff erent bonds.” The rest is history and was made
into the movie The Big Short, and here’s the scene of Michael
Burry negotiating to purchase CDS of various banks.

### CDS spreads and risk premiums

We now provide a simple, intuitive argument for why the CDS spread k
on the reference asset of a reference entity should approximately equal the
reference entity’s risk premium over the risk-free rate r. Suppose you:
- Purchase a portfolio of the reference asset (say bond) for total face
value F, receiving a YTM of y, and approximately at par value.
- At par means the coupon rate is also y.
- Purchase CDS protection over the reference asset for a notional
principal of F and paying a breakeven CDS spread of k.
We also assume that (i) the reference asset coupon payments and CDS
premiums occur on the same dates (both semiannual, or quarterly, etc)
and (ii) the maturity dates of the reference asset and CDS align.


Then your “net YTM” is the reference asset’s YTM y you receive minus
the CDS spread k you pay. Consider the two possible scenarios:
- No reference event: If there’s no reference event over the life of
the reference asset/CDS, then you realise the “net YTM” of y − k.
- Reference event occurs: If a reference event occurs at some point
over the life of the reference asset/CDS, the CDS payout enables
you to recover the full face value F, which you can then invest at
the risk-free rate r for the remaining time to maturity.
Hence, the CDS turns the reference asset into a risk-free investment.
- The “net YTM” should equal the risk free rate, that is, y − k = r
and thus k = y − r, or else there is an obvious arbitrage opportunity.

### CDS Indices

We now turn to CDS indices, which are useful for your Team Project.

A CDS index such as those in the CDX or iTraxx families are tradable
baskets of single-name CDS. They have specifi c rules/features:
- Number, country, credit rating, etc, of constituent reference entities.
- Various maturities, but 5 years is the most common.
- Typically a fi xed CDS spread of k = 1% (100 basis points).
- Usually quoted as a breakeven CDS spread in basis points.
  - It’s roughly an average of the constituent breakeven CDS spreads.
- Constituent CDS are typically evenly weighted.
  - Typically all have same notional principal in the CDS index.
- Premiums typically paid quarterly.
- Index constituents usually updated semiannually.
- Precisely defi ned reference events leading to payouts.

> - Name - company or government
> - Have a CDS of 100M, of 10 companies, evenly weighted in terms of notional principle
> - update CDS constituents
> - precisely defined reference events


An important aspect of CDS indices is how payouts occur:
- If a reference entity of a single-name CDS constituent in the CDS index experiences a reference event, the CDS index protection buyer receives the payout as per usual from that single-name CDS.
- This single-name CDS then ceases to exist as per normal for a single-name CDS, and is removed form the CDS index.
- The CDS index continues to exist, just with 1 less constituent.

---
### Example 

![alt text](assets\IMG203.PNG)

Of interest to you for the Team Project, Bill Ackman at Pershing Square
purchased the CDX NA Investment Grade, CDX NA High Yield and
iTraxx Europe CDS indices to hedge his portfolio exposure.

![alt text](assets\IMG204.PNG)

