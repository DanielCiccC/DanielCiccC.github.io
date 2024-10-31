# Tutorial 1

### 1.* Differentiate the following terms/concepts: 

**a. Prospect and probability distribution**

A prospect is a lottery or series of wealth outcomes, each of which is associated with a probability, whereas a probability distribution defines the likelihood of possible outcomes. 

**b. Risk and uncertainty**
- Risk is when you know what the outcomes could be, **and can assign probabilities**
- Uncertainty is when you can’t assign probabilities; or you can’t come up with a list of possible outcomes


**c. Utility function and expected utility**

A utility function, denoted as $u(w)$, assigns numbers to possible outcomes so that preferred choices receive higher numbers. Utility can be thought of as the satisfaction received from a particular outcome. 

"Expected utility" is an economic term summarizing the utility that an entity or aggregate economy is expected to reach under any number of circumstances. The expected utility is calculated by taking the weighted average of all possible outcomes under certain circumstances. 

**d. Risk aversion, risk seeking, and risk neutrality**

- Risk aversion describes someone who prefers the expected value of a lottery to the lottery itself.  
- Risk seeking describes someone who prefers a lottery to the expected value of a lottery.
- Risk neutrality describes someone whose utility of the expected value of a lottery is equal to the expected utility of the lottery

### 2*. When eating out, Rory prefers spaghetti over a hamburger.  Last night she had a choice of spaghetti and macaroni and cheese and decided on the spaghetti again.  The night before, Rory had a choice between spaghetti, pizza, and a hamburger and this time she had pizza.   Then, today she chose macaroni and cheese over a hamburger.  Does her selection  today  indicate  that  Rory’s  choices  are  consistent  with  economic  rationality?  Why or why not? 

- spag $\succ$ ham
- spag $\succ$ mac&cheese
- pizza $\succ$ spag
- pizza $\succ$ ham
- mac&cheese $\succ$ ham

Consistent with rationality, complete and transitive. the ordering is

pizza $\succ$ spag $\succ$ mac&cheese $\succ$ hamburger

### 3*. Consider a person with the following utility function over wealth: u(w) = e w , where e is the exponential function (approximately equal to 2.7183) and w = wealth in hundreds of thousands of dollars.  Suppose that this person has a 40% chance of wealth of $50,000 and a 60% chance of wealth of $1,000,000 as summarized by P(0.40, $50,000, $1,000,000).

**a. What is the expected value of wealth?**

$$P(0.40, \$50,000, \$1,000,000)$$

$$E(w) = 0.4 * 0.5 + 0.6 * 10 = 6.2M$$

$$U(P) = 0.4e^{0.50}  + 0.6e^{10}  = 13,216.54M $$

**b. Construct a graph of this utility function.**

![alt text](assets\IMG32.PNG)

**c. Is this person risk averse, risk neutral, or a risk seeker?**

- Risk seeker because graph is convex.

**d. What is this person’s certainty equivalent for the prospect?**

$e^{w} = 13,216.54$ gives $w = 9.4892244$ or \$948,922.44 

**Certainty equivalent** is defined as that wealth level that leads decision-maker to be indifferent between a particular prospect and a certain wealth level, *implied by the expected utility of the prospect.*

### 4. An individual has the following utility function: u(w) = $w^{.5}$  where w = wealth. 

**a. Using expected utility, order the following prospects in terms of preference, from the most to the least preferred:**
- P1(0.8, 1,000, 600) 
- P2(0.7, 1,200, 600) 
- P3(0.5, 2,000, 300) 

![alt text](assets\IMG33.PNG)

**b. What is the certainty equivalent for prospect P2?**

![alt text](assets\IMG34.PNG)

**c. Without doing any calculations, would the certainty equivalent for prospect P1 be larger or smaller?  Why?**

- smaller, because the utility is smaller

### 5*. Consider two prospects: 

![alt text](assets\IMG35.PNG)

It  has  been  shown  by  Daniel  Kahneman  and Amos  Tversky  (1979,  “Prospect  theory: An analysis of decision under risk,” Econometrica 47(2), 263-291) that more people choose B when presented with problem 1 and when presented with problem 2, most people choose C.  These choices violate expected utility theory. Why? 

![alt text](assets\IMG36.PNG)

### 6*. Additional Question regarding expected utility: Bill loves maple syrup and makes regular monthly purchases. Each bottle costs $50 (it’s a very special maple syrup). You’ve known Bill for a long time, and have observed, first handed, the ups and downs of his economic situation. 

![alt text](assets\IMG120.PNG)

### (b) When Bill was appointed a lecturer, his (disposable) income rose to $5,000 per month. The price of maple syrup did not change, and Bill still bought 25 bottles each month. Illustrate his new budget constraint and indicate Bill’s optimal bundle on your graph. 

# Part 2 - Foundations of finance

### 1*. Differentiate the following terms/concepts: 

**a. Systematic and non-systematic risk**
- Non diversifiable or systematic risk is risk that is common to all risky assets in the system and cannot be diversified.
- Diversifiable or unsystematic risk is specific to the asset in question and can be diversified. 

**b. Beta and standard deviation**
- Beta is the CAPM’s measure of risk.  It takes into account an asset’s sensitivity to the market and only measures systematic, non diversifiable risk.  
- The standard deviation is a measure of dispersion that includes both diversifiable and non diversifiable risks. 

**c. Direct and indirect agency costs**
Agency costs arise when managers’ incentives are not consistent with maximizing the value of the firm.  
- Direct costs include expenditures that benefit the manager but not the firm, such as purchasing a luxury jet for travel.  Other direct costs result from the need to monitor managers, including the cost of hiring outside auditors.  
- Indirect costs are more difficult to measure and result from lost opportunities. 

**d. Weak, semi-strong, and strong form market efficiency**

- Weak form market efficiency prices reflect all the information contained in historical returns.  
- With semi-strong form market efficiency prices reflect all publicly available information. 
- Strong form market efficiency prices reflect information that is not publicly available, such as insiders’ information. 

### 2*. Suppose you find that prices of stocks before large dividend increases show on average consistently positive abnormal returns. Is this a violation of the EMH? 

Market efficiency implies investors cannot earn excess risk-adjusted profits. If the stock price run-up occurs when only insiders know of the coming dividend increase, then it is a violation of strong-form efficiency. If the public also knows of the increase, then this violates semistrong-form efficiency. 

> - strong-form efficiency posits that even insider information is reflected in current stock prices.


### 3*. A stock has a beta of 1.2 and the standard deviation of its returns is 25%.  The market risk premium is 5% and the risk-free rate is 4%. 

**a. What is the expected return for the stock?**

$$E(R) = 0.04 + 1.2(0.05) = 0.10$$

**b. What are the expected return and standard deviation for a portfolio that is equally invested in the stock and the risk-free asset?**

$$E(R_{P}) = 0.5(0.10) +0.5(0.04) = 0.07$$

$$ σ p  = (0.5) (0.25) =0.125$$

> - this is because $\sigma _{r_{f}} = 0$

### c. A financial analyst forecasts a return of 12% for the stock. Would you buy it? Why or why not? 

If you believe the source is very credible, buy it as it is expected to generate a positive abnormal (or excess) return.

### 4. The monthly rate of return on T-bills is 1%. The market went up this month by 1.5%. In  addition, AmbChaser, Inc., which has an equity beta of 2, surprisingly just won a lawsuit that awards it $1 million immediately. 

**a. If the original value of AmbChaser equity were $100 million, what would you guess was the rate of return of this month?** 

Based on broad market trends, the CAPM indicates that AmbChaser stock should have 
increased by: 1.0% + 2.0 × (1.5% – 1.0%) = 2.0% 

Its firm-specific (nonsystematic) return due to the lawsuit is $1 million per $100 million initial equity, or 1%. Therefore, the total return should be 3%. (It is assumed here that the outcome of the lawsuit had a zero expected value.) 

**b. What is your answer to (a) if the market had expected AmbChaser to win $2 million?**

If the settlement was expected to be $2 million, then the actual settlement was a “$1 million disappointment,” and so the firm-specific return would be –1%, for a total return of 2% – 1% = 1%. 

### 5*. What is the joint hypothesis problem?  Why is it important? 

If when testing one hypothesis another must be assumed to hold, a joint-hypothesis problem arises. For us, this is of particular interest when we are testing market efficiency because of the need to utilize a particular risk-adjustment model to produce required returns, that is, to risk-adjust.    

This would not be a problem if we knew with certainty what the correct risk adjustment model is, but unfortunately we do not. If a test rejects the EMH, is it because theEMH does not hold, or because we did not properly measure abnormal returns? We simply do not know for certain the answer to this question.   

### 6*. Warren Buffett has been a very successful investor.  In 2008 Luisa Kroll reported that Buffett  topped  Forbes  Magazine’s  list  of  the  world’s  richest  people  with  a  fortune estimated to be worth $62 billion (March 5, 2008, "The world's billionaires," Forbes).  Does this invalidate the EMH? 

Warren Buffett’s experience does not necessarily invalidate the EMH.  There is the possibility that  he  is  just  lucky:  given  that  there  are  numerous  money  managers,  some  are  bound  to perform well just by luck. Still, many would question this here because Buffett’s track record has been consistently strong. 

7*. You are considering whether to invest in two stocks, Stock A and Stock B.  Stock A has 
a beta of 1.15 and the standard deviation of its returns has been estimated to be 0.28.  For 
Stock B, the beta is 0.84 and standard deviation is 0.48. 

**a.  Which stock is riskier?**

Stock A is riskier, though stock B has greater total risk. 
- Stock B's risk can be diversified away

**b.  If the risk-free rate is 4% and the market risk premium is 8%, what is the expected return for a portfolio that is composed of 60% A and 40% B?**

$$R_{p}  = .6(.132) + .4 (.1072) = .12208$$

**c.  If  the  correlation  between  the  returns  of A  and  B  is  0.50,  what  is  the  standard deviation for the portfolio that includes 60% A and 40% B?**

$$σ_{p}^{2}  = (.6) 2 (.28) 2  + (.4) 2 (.48) 2  + 2*.5(.6)(.4)(.28)(.48) = 9.7\%, \: \: σ_{p}  = 31.2\% $$
