# Tutorial 7 - Topic 6 Heuristics and Its Implications 

### 1. Differentiate the following terms/concepts:
**a. Primacy and recency effects**
A  primacy  effect  is  the  tendency  to  rely  on  information  that  comes  first  when  making  an 
assessment, whereas a recency effect is the tendency to rely on the most recent information 
when making an assessment. 

### b. Salience and availability

- Salience - refers to how much it stand out relative to other events
- Availability, how easily the event is recalled from memory, e.g. freely available, easily processed information is more compelling

### c. Fast-and-frugal heuristics and bias-generating heuristics
Fast and frugal heuristics require a minimum of time, knowledge and computation in order to 
make choices.  Often they lead to very good choices.  Sometimes however heuristics go astray 
and generate behavioral bias. 


### d. Autonomic and cognitive heuristics
Autonomic heuristics are reflexive, autonomic, non-cognitive, and require low effort levels.  
Cognitive heuristics require more deliberation.  Autonomic heuristics are appropriate when a 
very quick decision must be made or when the stakes are low, whereas cognitive heuristics are 
appropriate when the stakes are higher.   


### 2*. Which description of Mary has higher probability?
- A. Mary loves to play tennis.
- B. Mary loves to play tennis and, during the summer, averages at least a game a week.

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

> Conjunction fallacy
> - The second probability has to be less because it has one more requirement
> - When people commit then conjunction fallacy, they will think the second (joint) event is more likely because it sounds logical that someone who loves tennis will also play regularly

### **3. * Suppose you have invested in two different stocks, Stock A and Stock B. Based on historical data, the probability that Stock A will increase in value over the next year is 0.6. For Stock B, the probability is 0.5. The probability that both stocks will increase in value over the next year is 0.3. What is the probability that at least one of the two stocks will increase in value over the next year?**

$$P(A) = 0.6$$
$$P(B) = 0.5$$
$$P(A \cap B) = 0.3$$
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$= 0.6+0.5 - 0.3 = 0.8$$

### **4. *Rex is a smart fellow. He gets an A in a course 80% of the time. Still he likes his leisure, only studying for the final exam in half of the courses he takes. Nevertheless when he does study, he is almost sure (95% likely) to get an A. Assuming he got an A,how likely is it he studied? If someone estimates the above to be 75%, what error are they committing? Explain.**

$$P(A) = 0.8$$
$$P(B) = 0.5$$
$$P(A | B) = 0.95$$

$$P(B | A) = P(A|B) \cdot \frac{P(B)}{P(A)}$$

$$= 0.95 \cdot \frac{0.5}{0.8} = 0.59375$$

**5. *What is the relationship between intersection (i.e., P(A∩B)) and conditional probability (i.e., P(A∣B))?**

- $P(A \cap B)$ is the probability of both events
- $P(a|B)$ is the conditional probability of A happening, given that B has already happened
- $P(A|B) = P(A \cap B) / P(B)$


**6. *Imagine you are a portfolio manager looking at historical data for Stock C and Stock D in your portfolio. You find that the probability Stock C will have a positive return in a given month is 0.70. The probability Stock D will have a positive return in the same month is 0.60. However, if Stock C has a positive return, the probability Stock D will also have a positive return increase to 0.80. What is the conditional probability that Stock C will have a positive return given that Stock D has a positive return?**

$$P(C) = 0.7$$
$$P(D) = 0.6$$
$$P(D|C) = 0.8$$

$$P(C|D) = P(D|C) \cdot \frac{P(C)}{P(D)}$$

$$= 0.8 \cdot \frac{0.7}{0.6} = 0.9 \bar{3}$$

### 8.  How  do  gambling  fallacy  and  clustering  illusion  relate  to  representativeness?  Provide examples from sports.  In what way are they different? 
Representativeness exists when one thinks that A should look like B.  A can be the sample and B the distribution, or vice-versa.  A belief in a hot hand is thinking the conditional distribution should look like the sample.  But sometimes it seems that people think the reverse, namely that the sample, however small, should look like the distribution, in the sense that essential features should be shared.  A hot hand often comes into play in sports when people don’t know for certain the skill level of an athlete, and the extent to which it may change.  Gambler’s fallacy is likely to exist when the underlying distribution (e.g., cards or dice) is well-known. 

## Part Two: The Impact of Heuristics and Biases on Financial Decision-making

### 1*. Differentiate the following terms/concepts:

**a. Good company and good stock**
- A good company has positive attributes such as strong management
- A good stock is one you expect to outperform in the future. If markets are efficient there are no good or bad stocks

> - Loosely speaking, good companies will already sell at high prices, and bad companies already sell at low prices


**b. Momentum-chaser and contrarian**

- A momentum chaser buys stocks that have performed well in the past (buy high, sell higher)
- A contrarian buys stocks that have not performed well in the past

**c. International diversification and domestic diversification**
Portfolio theory teaches us that diversification pays off.  If we stick with domestic securities, 
this is domestic diversification.  If, as we should, we move to foreign securities as well, this is 
international diversification. 

> - Excessive optimism about prospects of domestic market
>   - Comfort seeking and familiarity

**d. Anchoring and herding**

- Anchoring means sticking with maintained or prior-views, new information is docounted
- Herding - going with the crowd

> - Investor that will follow the actions of the larger groups to make their investments


**2*. In a regression of perceived long-term investment value (LTIV) on size (S), book to market (B/M), and management quality (MQ), the following coefficients (all significant) were estimated:**

$$LTIV = -0.86 + 0.15log(S) + -0.11log(B/M) +0.85MQ$$

> - positive relative to the size of the firm
> - negative relation to the B/M
> positive relative to market value

- In this regression value as a long term investment is regressed on size, book-to-market, and management quality
- Management quality strongly impacts perceived investment value. This does not make sense because all positive attributes should already be embedded in stock price
- Big firms are viewed as good investments, and growth companies are viewed as good investments. Big high-growth firms are viewed as representative of good investments
- Interestingly the empirical evidence points in the opposite direction - it is small-cap value firms that have historically outperformed.

> - Small cap value firms have a lower investment value

### 3. Home bias has a potential information-based explanation. Discuss 

One  reason  why  investors  may  favor  local  markets  –  where  local  is  interpreted  as  either domestic or close-to-home but within the same country – **is because they may possess, or may feel that they possess, informational advantages**.  Gains from being geographically close to a company may appear in improved monitoring capability and access to private information.  One paper established that mutual fund managers, consistent with familiarity bias, tend to favor local investments, that is, they tend to buy firms headquartered within a 100-mile (or 161-kilometer)  radius  of  their  head  office.    Specifically,  they  conclude  that  the  average manager invests in companies that are located within 160-84 kilometers, or 9-11%, closer to her than the average firm she could have held.    

Research has shown a payoff to local investing.  Fund managers on average earn 2.67% per year more on local investments, while local stocks avoided by managers underperform by 3% per year.  Moreover, they find that those better able to select local stocks tend to concentrate their holdings more locally.  There is even evidence that retail investors are able to benefit from local investing.  Based on a dataset of retail investors, local investments outperform remote investments by 3.2% per year. 

### 4*. In Canada there are two official languages, French and English. Some Canadian corporations are headquartered in Quebec where French is the official language. Most however are headquartered outside Quebec where English is dominant. Would you expect Quebecers to invest more in Quebec companies, and nonQuebecers to invest more in companies based outside Quebec? Also, do you think the first language of the CEO might matter in accounting for investor preferences? Explain.

We  would  expect  to  see  the  same  as  in  the  study  using  Finnish  data  where  the  two languages/ethnicities were Swedish and Finnish.  Specifically, we would expect to see English-speaking  investors  preferring  companies  based  outside  of  Quebec  and  French-speaking investors preferring companies based inside of Quebec.  Similarly, we might expect to see a preference on the part of English-speaking investors for English-speaking CEOs (and the same for French-speaking investors). 
  
> - related to home bias


