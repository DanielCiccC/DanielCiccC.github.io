# Tutorial 7

**1. Differentiate the following terms/concepts:**
a. Primacy and recency effects

- Primacy effect is the tendency to reply on information that comes first when making an assessment, whereas
- Recency effect is the tendency to rely on the most recent information when making an assessment

### b. Salience and availability

- Salience - referes to how much it stand out relative to other events
- Availability, how easily the event is recalled from memory, e.g. freely available, easily processed information is more compelling

### c. Fast-and-frugal heuristics and bias-generating heuristics
- Fast and frugal require a minimum of time, knowledge and computation in order to make choices
- Sometimes heuristics go astray and generate behavioural bias

> - Make decisions within limited time and knowledge, amount to *doing the best that they can under the circumstances*


### d. Autonomic and cognitive heuristics
- Automatic -  are reflexive, autonomic, non-cognitive, and require low effort levels
- Cognitive heuristics require more deliberation
- Autonomic heiristics are appropriate when a very quick decision must be made


### 2*. Which description of Mary has higher probability?
- A. Mary loves to play tennis.
- B. Mary loves to play tennis and, during the summer, averages at least a game a week.

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

> COnjunction fallacym the second probability has to be less because it has one more requirement
> When people commit then conjunction fallacy, they will think the second (joint) event is more liekly because it sounds logical that someone who loves tennis will also play regularly



**3. * Suppose you have invested in two different stocks, Stock A and Stock B. Based on historical data, the probability that Stock A will increase in value over the next year is 0.6. For Stock B, the probability is 0.5. The probability that both stocks will increase in value over the next year is 0.3. What is the probability that at least one of the two stocks will increase in value over the next year?**

$$P(A) = 0.6$$
$$P(B) = 0.5$$
$$P(A \cap B) = 0.3$$
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$= 0.6+0.5 - 0.3 = 0.8$$

**4. *Rex is a smart fellow. He gets an A in a course 80% of the time. Still he likes his leisure, only studying for the final exam in half of the courses he takes. Nevertheless when he does study, he is almost sure (95% likely) to get an A. Assuming he got an A,how likely is it he studied? If someone estimates the above to be 75%, what error are they committing? Explain.**

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

## Part Two: The Impact of Heuristics and Biases on Financial Decision-making

### 1*. Differentiate the following terms/concepts:

a. Good company and good stock
- A good company has positive attributes such as strong management
- A good stock is one you expect to outperform in the future. If markets are efficient there are no good or bad stocks

> - Loosely speaking, good companies will already sell at high prices, and bad companies already sell at low prices


**b. Momentum-chaser and contrarian**

- A momentum chaser buys stocks that have performed well in the past (buy high, sell higher)
- A contrarian buys stocks that have not performed well in the past

**c. International diversification and domestic diversification**
- Portfolio theory teaches us that diversification pays off, if we stick with domestic securities, this is domestic diversification
- If we move to foreign securities this is international diversification

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

### 4*. In Canada there are two official languages, French and English. Some Canadian corporations are headquartered in Quebec where French is the official language. Most however are headquartered outside Quebec where English is dominant. Would you expect Quebecers to invest more in Quebec companies, and nonQuebecers to invest more in companies based outside Quebec? Also, do you think the first language of the CEO might matter in accounting for investor preferences? Explain.

- We would expect to see English-speaking investors preferring companies based outside of Quebec and French-speaking investors preferring companies based inside of Quebec
- We might expect to see a preference on the part of English-speaking investors for English-speaking CEOs (and the same for French-speaking investors)
  
> - related to home bias
