# Lecture 2, revised
# Prospect Theory, Framing and Mental Accounting

### Overview

[Part One – Prospect Theory]
- **1** Overview about Prospect Theory
  - **1.1** Risk Aversion vs. Risk Seeking
  - **1.2** Development of Prospect Theory
  - **1.3** Prospect Theory Value Function
  - **1.4** The Weighting Function

[Part Two – Mental Accounting]
- **2** Mental Accounting
  - **2.1** Integration vs. Segregation
  - **2.2** Theater Ticker Problems
  - **2.3** Opening and Closing Accounts


# 1 Introduction to Prospect Theory

- Prospect theory was developed by two psychologists, **Kahneman and Tversky (1979)** based on <u>observing actual behaviour</u> (aka. Positive model).
- Experimental evidence suggests that individuals frequently <u>deviate from the behavioural predictions of expected utility theory</u> (Normative model).
- Prospect theory has a solid mathematical basis. 
- Unlike expected utility theory which concerns itself with how decisions under uncertainty should be made (a prescriptive approach), prospect theory concerns itself with how decisions are actually made (a descriptive approach)

### Recap:

- Expected Utility can be defined as:

$$E(U) = \sum^{N}_{i=1}P_{i}U(w_{i})$$

Where:
- $P_{i}$ - probability of each outcome
- $U(w_{i})$ is the utility derived from each outcome ($w_{i}$ = wealth)

**Example:**
- If you face this gambling opportunity: 50% win $105, 50% lose $100. Take it?
- If you are an expected utility maximizer with wealth W, you should take the gamble if
current utility < expected utility
  - expected outcome - $2.5
- Von Neumann and Morgenstern 
  - if you follow certain axioms, you must maximize “expected utility.”

### 1.1 Loss Aversion vs Risk Aversion

**Loss Aversion** | **Risk Aversion**
 | --- | --- | 
 Strong preference to avoid losses rather than acquiring equivalent gains. <br> - Feelings of loss are psychologically about twice as powerful as feelings of gain. <br> - May lead to taking bigger risks to avoid losses. | - Preference for lower levels of risk and uncertainty.<br> - Choice of guaranteed outcomes, even if less profitable.<br> - Drives decisions towards certainty over uncertainty.

### 1.2 Development of prospect theory
- The prospect theory was proposed in 1979 to address certain empirical observations that Expected Utility Theory failed to explain.
  - Value vs. Utility & Difference in Wealth vs. Total Wealth 

Three Key characteristics of the value function include:
1. Reference Dependence: Value perception is relative to a specific reference point, typically the status quo.
2. Loss Aversion: Losses impact utility more than equivalent gains.
$$v(x) < -v(-x)$$
3. Diminishing Sensitivity: Sensitivity to wealth changes decreases as the magnitude of gain or loss increases.


![alt text](assets\IMG9.PNG)

### 1.3 Common value functional form of Prospect Theory

**Positive Domain**
$$v(z) = z^{\alpha}  \; \text{for} \; z≥0, \; \; 0< \alpha <1  $$

- $z$ is change in wealth (horizontal line)
- Value function (not utility) so $v$ is used.

**Negative Domain**
$$  v(z) = -\lambda(-z)^{\beta} \; \text{for} \; z<0, \: \: \lambda >1, \;\; 0<\beta<1 $$

- The factor $\lambda$, which is greater than 1, introduces loss aversion 
- The parameter β (0<β<1) controls the curvature of the function on the loss side, similar to α on the gain side (see Appendix). 
- Kink at origin.

### 1.4 Common ratio effect and weighting function

The answer lies in its **nonlinear weighting function**. In  Prospect  Theory,  probabilities  are  not  treated linearly. *Small probabilities* are **overweighted**,  which means they seem larger than they are, and *moderate to  high  probabilities*  are  **underweighted**,  appearing smaller than they are.

This  distortion  of  probabilities  can  make  option  B  in Prospect Pair 5 seem more attractive than it would be under  expected  utility  theory,  thus  reconciling  the 
apparent contradiction.

### Lottery effect

Prospect pair 6 -- choose between:
- A: (0.001, $5,000)
- B: ($5)

Most prefer A which is inconsistent with risk aversion.
- People  seem  to  overweight  low-probability events  (which  is  why  people  buy lottery tickets)

### Insurance

Prospect pair 7 -- choose between:
- A: (0.001, -$5,000)
- B: (-$5)

Most prefer B which is inconsistent with risk seeking.
- Insurance need
- Once  again,  people  seem  to  overweight  low-probability  events  (which  is  why  people  buy insurance)


### weighted sum of utilities

Prospect  theory  assumes  people  maximize  a  “weighted  sum  of  utilities,”  although  the weights are not the same as the true probabilities, and the “utilities” are determined by a value function rather than a utility function:

$$\max: E(v) = \sum \pi (p_{i}) \times (x_{i}-r)$$

- Where $\pi$is a non-linear weighting function,
- $v(x_{i} - r)$ is the value function evaluated with respect to the reference point, $r$ [Change in Wealth]

> - $r$ is your reference point
> - $p_{i}$ prospect part $i$


### 1.4 Weighting function

- The decision weighting function is non-linear with the probability $p$. 
  - That is, decision weights are not probability.
  - They do not obey the probability axioms.
  - They should not be interpreted as measures of belief.
- Properties of the weighting function: 
  - $\pi '(p) > 0$  is an increasing function of $p$
  - $𝝅(0) = 0$:  outcomes contingent on an impossible event are ignored 
  - $𝝅(1) = 1$: scale is normalised so the certainty event has a π value of 1. 
 
For small $p$,  𝝅 (r*p) > r 𝝅 (p) where $0<r<1$:𝝅  is subadditive
- Ex:  $𝝅 (0.001)/ 𝝅 (0.002) > 1/2$
- Meaning: when winning is possible but not probable (i.e., small p), most people choose the prospect that offers larger gain : V(6,000, 0.001) > V(3,000, 0.002)

This (displayed) mathematical function is

$$\pi (pr) = \frac{pr^{\gamma}}{[pr^{\gamma}  + (1- pr)^{\gamma} ]^{1/\gamma}}  , \text{where} \;\; \gamma = .65$$

- Weighting function for losses can vary from weighting function for gains.
- Low probabilities are given relatively higher weights than more probable events.
- And certainty is weighted highly vs. near-certainty. 
- Using functions like this solves some earlier puzzles.

---
### Example - valuing prospects under prospect theory
$$V(P) = \pi(pr_{A}) * v(z_{A}) + \pi(1 - pr_{A}) * v(z_{B})$$

Steps:
- Convert probabilities to decision weights
- Calculate values of wealth differences
- Use the above formula

> - DO THIS LATER
---

**Frames**
- Essential condition for a theory of choice is principle of invariance: Different representations of same problem should yield same preference.

### Mental accounting
Related to prospect theory and frames.
- Accounting is process of categorizing money, spending and financial events.
- Mental accounting is a description of way people intuitively do these things, and how it impacts financial decision-making.
- Often tendency to use mental accounting leads to odd and suboptimal decisions.

