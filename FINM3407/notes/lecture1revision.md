# lecture 1, revised
# Introduction to Behavioral Finance and Traditional Finance Theories

### Overview
[Part One – Introduction to Behavioral Finance]
- **1** Overview of neoclassical economics
  - **1.1** Preference Relation
  - **1.2** Utility Function and Expected Utility Theory
  - **1.3** Brief Introduction to Behavioural Finance

[Part Two – Foundations of Finance]
- **2** Foundations of Finance II: Asset Pricing, Market Efficiency and Agency Relationships
  - **2.1** Risk and Return Relationship
  - **2.2** CAPM model and Fama and French 
  - **2.3** Market Efficiency (brief introduction = > more details in Topic 3)
  - **2.4** Agency Relationships and Corporate Governance


# 1 Neoclassical economics - normative theory (versus positive)

1. People have rational preferences across possible outcomes or states of nature.
2. People maximize utility and firms maximize profits.
3. People make independent decisions based on all “relevant” information.

> - normative - expect how people *should* behave and react
> - not for just investment decisions
>
> Positive model - what people are actually doing

## 1.1 Preference Relation

- Economists use preferences to understand and analyse people’s decision-making process
- In the most fundamental sense, the theory of rational choice specifies what types of preferences are considered to be rational in neoclassical economics 

**Weak preference**

$x \succsim y$ "x is at least as good as y


**Strict Preference**

$x \succ y$ "x is strictly preferred to y"

$x \succ y \Leftrightarrow x\succsim y \: \: \text{but not} \: \: y \succsim x$

**Indifference**

$x \sim y$ "x is indifferent to y"

$x \sim y \Leftrightarrow x\succsim y \: \: \text{and} \: \: y \succsim x$


The preference relation  $\succsim$  is rational if it has the following two properties:

### 1) Completeness (Ordering)
for all $x, y \in X$, we have that $x  \succsim  y$ or $y \succsim x$ 
(or both if there is indifference)
- e.g., My preference on fruit: Banana $\succsim$ Apple, Apple $\succsim$ Banana => My preference is complete


### 2) Transitivity
for all $x, y, z \in X$, if x  $\succsim$  y and y  $\succsim$  z, then x  $\succsim$  z 
- e.g., My preference on fruit: Banana  $\succsim$   Apple, Apple  $\succsim$  Watermelon,  we can imply that Banana  $\succsim$  Watermelon
- My preference is transitive 

### Utility function

Utility Function: measures the satisfaction an individual gained from a preference

$$u(w) = ln(w)$$

![alt text](assets\IMG2.PNG)

## 1.2 Expected Utility Theory

Says that individuals should act when confronted with decision-making *under uncertainty in a certain way*.

- Theory is really set up to deal with **risk**, not uncertainty:
- Risk is when you know what the outcomes could be, **and can assign probabilities**
- Uncertainty is when you can’t assign probabilities; or you can’t come up with a list of possible outcomes

> - with risk we say that we can quantify it
> - with uncertainty, you can assign probabilities or not even know the outcomes


**Example**

Say there are a given number of states of the world:
- A sunny and warm – 50%
  -  $500/day
- B rainy and cold – 50%
  -  $100/day

Prospect:
$$P1(0.5, 500, 100)$$

### Expected utility of a prospect

$$U(P) = pr_{A}  * u(w_{A}) + pr_{B}  * u(w_{B}) + pr_{C}  * u(w_{C})$$

**Example**
$$u(w) = w^{0.5}$$

**Prospects:**
- P4(0.5, 1000, 500)  Exp outcome = 750
- P5(0.6, 1200, 300) Exp outcome = 840

**Utility:**
- For P4: $U(P4) = (0.5 * 1000)^{0.5}  + (0.5 * 500)^{0.5}  = 26.99$
- For P5: $U(P5) = (0.6 * 1200)^{0.5}  + (0.4 * 300)^{0.5}  = 27.71$

**So:**
$$P5 \succ P4$$

### Properties of utility functions
- Certain properties of utility functions can be demonstrated:
  - Unique up to a positive linear transformation
  - Upward-sloping
  - Latter allows one to set u(lowest outcome)=0 and u(highest outcome)=1, which can be useful for proving certain things
- Other properties such as differentiability (implying continuity) are often assumed.

![alt text](assets\IMG3.PNG)

### Certainty equivalents

Assume utility function $u(w) = \ln(w)$

Consider prospect P6:

$$P6(0.5, 5, 100)$$ 
- Expected outcome = 62

We have:
$$U(P6) = 0.40(1.6094) + 0.60(4.6052) = 3.41$$

Equivalent guaranteed wealth ($62)

$$u(E(w)) = ln(62) = 4.13$$

Risk-averse: $U(E(w)) > U(P)$
- Prefers the expected value of a lottery to the lottery itself.

**Certainty equivalent** is defined as that wealth level that leads decision-maker to be indifferent between a particular prospect and a certain wealth level, *implied by the expected utility of the prospect.*

## 1.3 Introduction to Behavioural Finance

Behavioural economists believe that:
- the deviations from rationality are large enough, systematic enough, and consequently predictable enough, to warrant the development of new descriptive (aka Positive) theories
- in many cases normativity (normative) and adequate descriptivity (positive) cannot be embodied in the same theory 


### 1.3.1 Loss Aversion

Losses loom **greater** than gains. 

Considering the following two cases:
- A: Receiving $100 for sure.
- B: 50% chance of winning $300 and 50% chance of losing $100.

E(rA) = $100
E(rB) = $100

Some real-life examples of loss aversion:
- Not selling a stock when your current rational analysis of the stock clearly indicates that it should be abandoned as an investment.
- Selling a stock that has gone slightly up in price just to realize a gain of any amount, when your analysis indicates that the stock should be held longer for a much larger profit [Diposition effect].


### 1.3.2 Representative
- People frequently make the mistake of believing that two similar things or events are more closely correlated than they actually are.
- Judging the likelihood of things in terms of how well they seem to represent, or match, particular prototypes.

> Considering Laura, she is 31, single, outspoken, and very bright. She majored in economics at university as a student, and she was passionate about the issues of equality and discrimination.
Which of the following is more likely true:
> - A. Laura works at a bank.
> - B. Laura woks at a bank and is active in the feminist movement. 

### Mental Accounting
- Individuals classify money differently based on subject criteria.

> mentally assigning money to different accounts
> - money earned in gambling vs money in wallet - money won more likely to be spent using risk seeking behaviour
> - some amount in superannuation fund vs other portfolio - more risk seeking in separate portfolio, have baseline investment
>   - more stable investment as you become older


### Fear of Regret
- Make decisions based on minimising the possibility of experiencing regret in the future, even if it means avoiding potential opportunities or taking risks. 

Some examples:
- You are a conservative investor and always invest in low-beta stocks. Recently, you noticed the “UQ Coin” craze is unfolding in the financial markets, and you saw your friend purchasing UQ Coins as well. You decided to buy some yourself, ignoring potential risks, to avoid the regret of not purchasing it if it runs up further. 

> - Won't want to regret decision in the future
>   - Minimise the chance of you regretting something
> - May be a conservative investor; invest in other stock/security for fear of missing out despite obvious risks
> - Similar to FOMO 

# 2. Foundations of finance

## 2.1 Risk and Return

Return is the **Weighted average of returns of individual securities**

$$r_{p} = \sum ^{k}_{i=1} r_{i}\omega _{i}$$

- Total risk is measured as the standard deviation (volatility)

$$\sigma _{p} = \sqrt{w_{1}^{2}\sigma _{1}^{2} + w_{2}^{2}\sigma _{2}^{2} + 2w_{1}w_{2}\rho_{1,2}\sigma _{1}\sigma _{2} }$$

- Portfolio risk is less than a weighted average of risks of individual securities – if correlations are less than 1.
- The lower the correlations the lower the risk of a portfolio.
- Lower portfolio risk through Diversification.
- Can’t reduce risk to 0, can only diversify Unsystematic Risks, **not Systematic Risks**. 

![alt text](assets\IMG7.PNG)


### 2.2 CAPM Model

$$ E(r_{e}) = r_{f} + \beta_{e}(E(r_{M})-r_{f})$$

![alt text](assets\IMG8.PNG)

- CAPM is an equilibrium model: it brings all investors together.
- According to CAPM, only risk related to market movements (systematic risks) is priced by the market.
- Because all other risks can be diversified away (and they should be).
- SML is the graphical representation of CAPM.

> - difference SML and CML - x-axis
> - CML has standard deviation on the x-axis
> - SML has beta on the x-axis
> - SML for CAPM - for a given level of beta, and **not** for combination of assets


### 2.3 Market Efficiency
**Operational definition:**
- Financial markets are efficient if no one can consistently earn excess returns.
- Security prices should respond quickly and accurately to new information
- Professional investors should not outperform net of all fees
- Simulated trading strategies should fail
- Abnormal profits should not be consistently made.

**Efficient Market Hypothesis (EMH)**
- Weak form: Only past (historical prices & volume) information is available in the market
- Semi-strong form: Only past & public (e.g. financial statements) information  is available in the market
- Strong form: All information (past, public & private) is available in the market

### 2.4 Agency Relationships and Corporate Governance

**Agency relationship and agency problem**
-  An agency relationship exists whenever the principal contracts with an agent to take action on their behalf and represent the principal’s interests.
- In an agency relationship, the agent has the authority to make decisions for the principal.
- An agency problem arises when the agent’s and principal’s incentives are not aligned.

**Agency Cost**
- Direct costs: expenditures that benefit the managers but not the firms & costs arise from monitoring management actions
  - Example: the cost of hiring outside auditors, business trips using a private jet instead of commercial flights
- Indirect costs: results from lost opportunities
Example: managers of a firm that is an acquisition target may resist the takeover attempt because of concern about keeping their jobs, even if the shareholders would benefit from the merger.
