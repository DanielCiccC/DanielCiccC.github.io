# FINM3405 Revision - CDS

1. Basic definitions and concepts for credit default swaps.
2. More precise description of mechanics, including notions of:
  - 2.1. Analogy with insurance contracts.
  - 2.2. Parties: protection buyer and seller.
  - 2.3. Reference entity, assets and events.
  - 2.4. Payout, including physical vs cash delivery.
  - 2.5. Recovery rate and loss given default.
  - 2.6. CDS coupon or spread or premium.
  - 2.7. Single name vs multi name, basket, CDS indices.
  - 2.8. Idea that CDS spreads reflect credit risk perceptions, and relation between breakeven CDS spread and reference entity’s risk premium.
  - 2.9. Survival and default probabilities.

### Notation
So far we have the following CDS notation and terminology:
- $F$ is the notional principal or face value.
- $R$ is the recovery rate.
- $k$ is the CDS spread.
- $kFd$ is the CDS premium, where $d$ is the time between premium payments in years (say $d = 1/4$ for quarterly).
- $(1 − R)F$ is the payout upon occurrence of a reference event.


- $t_1 , . . . , t_N$ is the premium payment and payout dates.
- $r_1 , . . . , r_N$ is the risk-free rate yield curve for these dates.
- $q_i$ is the (risk-neutral) probability of default in period i.
  - Probability of a reference event occurring in period i.
- $s_i$ is the survival probability up to time $t_i$ .
  - Probability that no reference event occurred up to time $t_i$.
- $d$ is the time between premium payments in years


# 2. Mechanics

## 2.1 analogy

- The CDS buyer “takes out insurance” against a credit event (e.g. default) of a company or sovereign state and in return pays the CDS seller a regular, fixed “insurance” premium for the insurance.
- The CDS seller receives the CDS premium and agrees to pay the buyer a compensation amount upon occurrence of the credit event.
- If the credit event occurs, the compensation is paid, the CDS buyer pays the period’s accrued premium, and the CDS ceases to exist.
- If no credit event occurs, the CDS buyer keeps paying the periodic premium until the CDS maturity date.


## 2.2. Parties

- The CDS buyer is called the **protection buyer**.
- The CDS seller is called the **protection seller** or **swap writer**.

## 2.3. Reference entity, assets and events

**Reference Entity**
- The company or sovereign in the CDS is the reference entity

**Reference Assets**
- The particular debt securities (bonds, loans, floating rate notes, etc) of the reference entity over which the CDS is written are called reference assets or bonds or securities or obligations.

**Reference Events**
- The credit events relating to the reference entity’s reference assets as specified and defined in the CDS are called reference events.

Reference events specified in a CDS include, but are not limited to:
- *Default*: Failure of the reference entity to pay interest/loan/coupon payments or the principal or face value of the reference asset.
- *Bankruptcy*: Official or legal/judicial administration, liquidation or winding up of the reference entity rendering it unable to meet, either partially or wholly, its obligations of the reference asset.
- *Restructuring*: Corporate or debt restructuring that changes the nature of the reference asset in terms of its original structure and the original agreement between the reference entity and its creditors.
- *Repudiation/moratorium*: The reference entity disputing aspects of or failing to recognise the reference asset and its obligations, thereby disputing, delaying or refusing payment (common when the reference entity is a sovereign or sovereign state).
- *Covenants*: The reference entity’s breaching or noncompliance with debt covenants, including due to deterioration in financial position or the devaluation or writing off of assets used as security/collateral.
- *Ratings downgrade*: The downgrading of a reference entity by a credit ratings agency (such as S&P, Moody’s, Fitch, etc).

## 2.4. Payout, including physical vs cash delivery
The payout upon the occurrence of a reference event is defined as:

- A CDS is written over a notional principal or face value $F$.

CDS can be physically deliverable or cash settled upon the occurrence of a reference event (after which the CDS vanishes):
- Physical delivery: The protection seller agrees to buy the reference asset holding from the protection buyer at its total face value $F$. 
- Cash settled: The protection seller agrees to pay the protection buyer the difference $F − V$ between the face value $F$ and the market value $V$ of the reference asset.

## 2.5. Recovery rate and loss given default

We define the important concept of the recovery rate $R$:
- It is the market value $V$ of the reference asset expressed as a percent of the notional principal $F$ after a reference event:

$$V = RF$$

- From another perspective, R tells us “how much we would recover” if we held a portfolio of the reference asset of total face value F and then sold it after a reference event occurred: We receive $V = RF$. It also follows then that the payout $F − V$ for a cash settled CDS is

$$\text{CDS payout} = (1 − R)F$$

**Loss Given Default**

This payout $(1 − R)F$ is sometimes called the *loss given default* since it’s how much we’d lose on a holding of the reference asset.

## 2.6. CDS coupon or spread or premium.

The regular, fixed “insurance premium” paid by the protection buyer to the protection seller is called the CDS coupon or spread or premium.

- The premium $C$ is given as a percent $k$ of the notional principal:

$$\text{premium} = C = kFd$$

with $d = 1/2$ if semiannual premiums, $d = 1/4$ if quarterly premiums, etc. The market convention is premiums are usually paid quarterly.
- Here, $k$ is also called the CDS spread.

## 2.7. Single name vs multi name, basket, CDS indices.


The CDS can be single-name or multi-name:
- **Single-name CDS** are written over the reference assets of one single reference entity.
- **Multi-name CDS**, sometimes called **basket CDS**, are written over the reference assets of multiple reference entities, and the nature of their payouts can differ (add-up basket, kth -to-default basket, etc).

There’s also CDS indices (see wiki), which are effectively basket CDS:
- The CDX range (also see Investopedia and the CDS Indices Primer).
- The iTraxx range (also see Investopedia and wiki)

## 2.8. Idea that CDS spreads reflect credit risk perceptions, and relation between breakeven CDS spread and reference entity’s risk premium

**Why is k called the CDS spread?**

Let $r$ be the risk-free rate, or a reference rate such as
Term SOFR or Euribor which are effectively risk-free rates. Also
let $y$ be the yield on the reference entity’s reference asset.
- Then $y − r$ is the reference asset’s risk premium or spread.
- k rises (falls) when this perceived credit risk rises (falls).

## 2.9. Pricing

### Buyer
From the perspective of the protection buyer:
- The regular premium payments $kFd$ are cash outflows.
- The payout $(1 − R)F$ is a cash inflow.

So the value of a CDS to the protection buyer is

$$\text{CDS value = PV( E [payouts]) − PV( E [premiums])}$$

### Payouts

PV of expected payouts: At time $t_i$ there is a payout of:
- $(1 − R)F$ with probability $q_i$.
- $0$ otherwise.

Hence, the expected payout at time $t_i$ is

$$\mathbb{E}[\text{payout}_i]=q_i(1-R)F$$

Present value of all payouts is

$$\text{PV(}\mathbb{E}\text{[payouts])} = \sum ^N _{i=1} e^{-r_i t_i} q_i (1-R)F$$

### Premiums

At time $t_i$ there is a premium of:
- $kFd$ with probability $s_i$.
- 0 otherwise (note that we’re ignoring any accrued premium).

Hence, the expected premium at time $t_i$ is

$$\mathbb{E}[\text{premium}_i] = s_i kFd$$

The present value of all premiums are:

$$\text{PV(}\mathbb{E}\text{[premiums])} = \sum ^N _{i=1} e^{-r_i t_i} s_i kFd$$


### Pricing

The value of a CDS is:

$$V_{\text{CDS}} = \text{PV(}\mathbb{E}\text{[payouts])} - \text{PV(}\mathbb{E}\text{[premiums])}$$

The breakeven CDS spread k that which gives the CDS 0 initial value:

$$\text{PV(}\mathbb{E}\text{[payouts])} = \text{PV(}\mathbb{E}\text{[premiums])}$$

which we rearrange to get

$$k= \frac{\text{PV(}\mathbb{E}\text{[payouts])}}{\sum ^N _{i=1} s_iFd}$$

$$k= \frac{\sum ^N _{i=1} e^{-r_i t_i} q_i (1-R)F}{\sum ^N _{i=1} s_iFd}$$