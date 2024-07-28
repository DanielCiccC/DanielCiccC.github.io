# Lecture 1 - neoclassical economics & asset pricing, market efficiency and Agency Relationships


## Neoclassical economics - normative theory (versus positive)
1. People have rational preferences across possible outcomes or states of nature.
2. People maximize utility and firms maximize profits.
3. People make independent decisions based on all “relevant” information.

> - normative - expect how people *should* behave and react
> - not for just investment decisions
>
> Positive model - what people are actually doing
>
> 3. People will make independent decisions on all relevant information
>  - gangnam style became very popular, and father of company owns semiconductor company
>  - in a traditional finance theory, should only look at relevant information
>  - father's company increased by 800%

## (1) Preference Relation
- Economists use preferences to understand and analyse people’s decision-making process
- In the most fundamental sense, the theory of rational choice specifies what types of preferences are considered to  be rational in neoclassical economics 

**What is Preference?**
= > Preference is a relation that ranks alternatives (typically, consumption bundles) according to their desirability

> you can rank all your options 
> - use preference to understand how to make decisions
> - theory of rational choice, what kind of theory is rational

![alt text](assets\IMG1.PNG)

The preference relation ≿ is rational if it has the following two properties:

### 1) Completeness (Ordering)
for all $x, y \in X$, we have that $x  ≿  y$ or $y ≿ x$ 
(or both if there is indifference)
- e.g., My preference on fruit: Banana ≿ Apple, Apple ≿ Banana => My preference is complete


### 2) Transitivity
for all $x, y, z \in X$, if x  ≿  y and y  ≿  z, then x  ≿  z 
- e.g., My preference on fruit: Banana  ≿   Apple, Apple  ≿  Watermelon,  we can imply that Banana  ≿  Watermelon
- My preference is transitive 


### Utility Function: measures the satisfaction an individual gained from a preference

Notation: u(x,y,z)

Utility over goods:
 - u(2 bread, 1 water) > u(1 bread, 2 water)
Utility over money:
 - $u(w2) > u(w1)$ if w2 > w1

**Utility function over wealth, u(w) = ln(w)**

![alt text](assets\IMG2.PNG)

### (2) Expected utility theory

Says that individuals should act when confronted with decision-making under uncertainty in a 
certain way.
- Theory is really set up to deal with **risk**, not uncertainty:
- Risk is when you know what the outcomes could be, and can assign probabilities
- Uncertainty is when you can’t assign probabilities; or you can’t come up with a list of possible outcomes

> - with risk we say that we can quantify it
> - with uncertainty, you can assign probabilities or not even know the outcomes

**Example**

Say there are a given number of states of the world:
- A sunny and warm – 50%
  -  $500/day
- B rainy and cold – 50%
  -  $100/day

> What is the wealth outcome?

> called the 'prospect'
- P1(0.5, 500, 100)
  - Expected outcome = 300 (0.5x500+0.5x100)

Assume if it’s rainy and cold, the ice cream truck makes no profit
- P2(0.5, 500)
  - Expected outcome = 250 (0.5x500)
- P3(0.7,800,1000)
  - Expected outcome = 860
  - 

**An ordering of P1 vs. P2 and P1 vs. P3:**

P1 ≻ P2 and P3 ≻ P1
- Transitivity says: P3 ≻ P2 

### (2) Expected utility of prospect 

$$U(P) = pr_{A}  * u(w_{A}) + pr_{B}  * u(w_{B}) + pr_{C}  * u(w_{C})$$

Example
$$u(w) = w^{0.5}$$

Prospects:
- P4(0.5, 1000, 500)  Exp outcome = 750
- P5(0.6, 1200, 300) Exp outcome = 840

For P4: U(P4) = 0.5 * 1000 0.5  + 0.5 * 500 0.5  = 26.99
For P5: U(P5) = 0.6 * 1200 0.5  + 0.4 * 300 0.5  = 27.71

So P5  ≻  P4

Based on assumptions such as ordering and transitivity (and others), it can be shown that when such choices over risky prospects are to be made, people should act as if they are maximising expected utility:

### Properties of utility functions
- Certain properties of utility functions can be demonstrated:
  - Unique up to a positive linear transformation
  - Upward-sloping
  - Latter allows one to set u(lowest outcome)=0 and u(highest outcome)=1, which can be useful for proving certain things
- Other properties such as differentiability (implying continuity) are often assumed.

![alt text](assets\IMG3.PNG)

> - doesn't matter the risk tolerance level
> - always a continuing curve, will not have a sudden drop

### (2) Expected utility theory - Certainty equivalents
![alt text](assets\IMG4.PNG)

> same expected outcome
> - should feel the same about the two - probability about the two
> - Expected utility for guaranteed 62 - utility is more
>  - evidence showing that person is risk averse
> - If expected utility for the guaranteed amount is higher than the prospect, then you know you are risk averse
>
> What does it mean if you are risk averse?
> - may forgo some potential outcomes

![alt text](assets\IMG5.PNG)

### Problems with expected utility theory

- A number of violations of expected utility have been discovered.
- Most famous is Allais (French- pronounced Allay ☺) paradox = > we are going to cover in tutorials .
- Alternative theories have been developed which seek to account for these violations.
- Best-known is prospect theory of Daniel Kahneman and Amos Tversky.

## (3) Introduction to Behavioural Finance

**Behavioural economists believe that:**

- the deviations from rationality are large enough, systematic enough, and consequently predictable enough, to warrant the development of new descriptive (aka Positive) theories
- in many cases normativity (normative) and adequate descriptivity (positive) cannot be embodied in the same theory 

**The key idea of behavioural finance:**

- Investors DO NOT always act RATIONAL (as per economics).
- Investors suffer from heuristics and biases

Four main categories：
1) Loss Aversion
2) Representative
3) Mental Accounting
4) Fear of Regret

> - Most people around the world are not rational/do not make rational decisions
>   - If we are systematic enough, develop new models and theory to explain bias
>
> normative and positive models often contradict each other

### Loss Aversion
Losses loom greater than gains. 

Considering the following two cases:
- A: Receiving $100 for sure.
- B: 50% chance of winning $300 and 50% chance of losing $100.

E(rA) = $100
E(rB) = $100

Some real-life examples of loss aversion:
- Not selling a stock when your current rational analysis of the stock clearly indicates that it should be abandoned as an investment.
- Selling a stock that has gone slightly up in price just to realize a gain of any amount, when your analysis indicates that the stock should be held longer for a much larger profit [Diposition effect].

> 'if I don't sell it, I don't lose it'
> - may see a stock and the quickly goes up, want to sell 
>   - want to prevent it from becoming a loss in the future

### Representative
- People frequently make the mistake of believing that two similar things or events are more closely correlated than they actually are.
- Judging the likelihood of things in terms of how well they seem to represent, or match, particular prototypes.

Considering Laura, she is 31, single, outspoken, and very bright. She majored in economics at university as a student, and she was passionate about the issues of equality and discrimination.
Which of the following is more likely true:
- A. Laura works at a bank.
- B. Laura woks at a bank and is active in the feminist movement. 

> Correct ans should be A - more likely, as B is adding more constraint
>  - joined probability in B

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
> - akin to FOMO 

# Foundations of Finance

### Portfolio Risk and Return

![alt text](assets\IMG6.PNG)

> - overall risk should always be less than the weighted average of the standard deviations of individual assets
>  - Will be the same if the correlation = 1 between all assets
> - Because unsystematic risk can be diversified away, investors are only compensated for bearing systematic risk


![alt text](assets\IMG7.PNG)

> - same returns, lower risk
> - From point G, the efficient frontier
> - combined with capital market line - risk free interest rate 
> - combination of risk-free and portfolio M

### CAPM Model

$$ E(r_{e}) = r_{f} + \beta_{e}(E(r_{M})-r_{f})$$

![alt text](assets\IMG8.PNG)

- CAPM is an equilibrium model: it brings all investors together.
- According to CAPM, only risk related to market movements (systematic risks) is priced by the market.
- Because all other risks can be diversified away (and they should be).
- SML is the graphical representation of CAPM.

> - difference SML and CML - x-axis
> - CML, standard deviation, SML, beta
> - SML for CAPM - for a given level of beta, and **not** for combination of assets


### (3) Market Efficiency
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

> - if the market is efficient, then we shouldn't be able to beat the market
> - Security price should reflect the value immediately
>
> EMH
> - weak, only past information is available in the market
>   - past trading volumes is useless
>   - past information only, shouldn't work to predict the future
> - semi-strong
>   - should be already reflected in price
> - strongly efficient
>   - should be immediately priced
>
> No clear answer how efficient the market is

### (4) Agency Relationships and Corporate Governance

**Agency relationship and agency problem**
-  An agency relationship exists whenever the principal contracts with an agent to take action on their behalf and represent the principal’s interests.
- In an agency relationship, the agent has the authority to make decisions for the principal.
- An agency problem arises when the agent’s and principal’s incentives are not aligned.

**Agency Cost**
- Direct costs: expenditures that benefit the managers but not the firms & costs arise from monitoring management actions
  - Example: the cost of hiring outside auditors, business trips using a private jet instead of commercial flights
- Indirect costs: results from lost opportunities
Example: managers of a firm that is an acquisition target may resist the takeover attempt because of concern about keeping their jobs, even if the shareholders would benefit from the merger.


> - misalignments in incentives
> - direct costs - choosing to hire a private jet, costs only benefitting the agent and not the firm
> - indirect costs - target firm for M&A resisting takeover for job security
>
> Prevent agency issues
> - Good corporate governance statement
> - Incentives for managers, etc.