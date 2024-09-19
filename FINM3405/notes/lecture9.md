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