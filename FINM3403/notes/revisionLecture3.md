# Lecture 3, revised
# Parity Conditions

- Parity Conditions provide an intuitive explanation of the movement of prices and interest rates in different markets in relation to exchange rates. 
- Parity conditions rely on ARBITRAGE to hold.

- The derivation of these conditions requires the assumption of Perfect Capital Markets (PCM).
  - no transaction costs
  - no taxes
  - complete certainty

### Purchasing Power Parity
- PPP is based on the notion of arbitrage across goods markets and the basic building block of PPP is given by the Law of One Price (LOP)
- LOP states that the price of an identical good should be the same in all markets (assuming no transactions costs).
  

### The law of one price
- States that a while product’s price may be stated in different currency terms, but the price of the product in a common currency should remain the same.
  - Comparison of prices would only require conversion from one currency to the other:

$$P_{\$} = S_{\$/\pounds}\cdot P_{\pounds}$$

Conversely, the exchange rate could be deduced from the relative local product prices:

$$S^{PPP}_{\$/\pounds} = \frac{P_{\$}}{P_{\pounds}}$$

### Absolute Purchasing Power Parity (PPP)
- A *less extreme* form of the Law of One Price is the ABSOLUTE PPP which says that the price of a basket of goods would be the same in each market. 
- The PPP exchange rate between the two countries would then be:

$$S^{A/B}_{t} = \frac{PI_{A, t}}{PI_{B,t}}$$

- $PI_{A, t}$ and $PI_{B, t}$ are the price indices of the two countries (i.e. CPI) at time $t$

**Violations**
- Violations of Absolute PPP occur in the short run, but it tends to hold in the long run (several years). 

### Relative PPP
-  Relative PPP claims that exchange rate movements should exactly offset any inflation differential between two countries
  
**Exchange rate differential = inflation rate differential**

$$\therefore \frac{S^{A/B}_{t+1}-S^{A/B}_{t}}{S^{A/B}_{t}} = \frac{\pi_{A}-\pi_{B}}{1+\pi_{B}} $$

- $\pi_{A}$, $\pi_{B}$ are the inflation rates of countries A and B, respectively

**Relative PPP**:

$$\frac{S^{A/B}_{t+1}}{S^{A/B}_{t}} = \frac{1+\pi_{A}}{1+\pi_{B}}$$

**Approximate inflation rate differential**

$$\pi_{A}-\pi_{B}$$

### Applications of relative PPP

1. Forecasting future spot exchange rates.
2. Calculating appreciation in “real” exchange rates. This will provide a measure of how expensive a country’s goods have become (relative to another country’s).
    - More expensive relative to another country creates challenges - more competition, etc.

### Forecasting Future Spot rates

- Suppose the ¥/$ spot exchange rate and expected inflation for Japan and Australia are:

$$S_{\yen/\$, t_{0}}=\yen87.86 ;$$
$$\pi_{AUS} = 1.9\%$$
$$\pi_{Japan} = 1\%$$

- What is the expected ¥/$ exchange rate if relative PPP holds?

$$S_{\yen/\$, t_{1}} = S_{\yen/\$, t_{0}} \cdot (\frac{1 + \pi_{\yen}}{1+\pi_{\$}}) = (87.86)\cdot (\frac{1.01}{1.019}) = 87.08 \;\yen/\$$$

### The Real Exchange Rate
- The real exchange rate measures deviations from PPP. 
- Changes in the spot exchange rate that do not reflect differences in inflation rates between the two currencies in question.

**Real Exchange Rate**
$$E = \frac{S^{Actual}_{t+1}}{S^{PPP}_{t+1}}$$

$$E = \text{1 + \% over-under valuation of denominator currency}$$

- When E = 1, the denominator currency is valued correctly. *The competitiveness of this country is unaltered.*
- When E < 1, the denominator currency is undervalued. Products from the other country seem expensive relative to the base year.  That is, the *competitiveness of the denominator country improves.*
- When E > 1, the denominator currency is overvalued. Products from the other country seem cheap relative to the base year.  That is, the *competitiveness of the denominator country deteriorates.*

## Interest Rate Parity

- Interest rate parity (IRP) is an arbitrage condition that provides the **linkage between the foreign exchange markets** and the **international money markets.**

$$\frac{F^{A/B}_{t, t+1}}{S^{A/B}_{t}} = \frac{1+i_{A}}{1+i_{B}}$$

**percentage forward premium = interest rate differential**
$$\therefore  \frac{F^{A/B}_{t, t+1} - S^{A/B}_{t}}{S^{A/B}_{t}} = \frac{i_{A} - i_{B}}{1+i_{B}}$$

- The currency trading at a forward premium is the one from the country with the lower interest rate.
- The currency trading at a forward discount is the one from the country with the higher interest rate.

### Why Parity Holds?
- This must hold by arbitrage. Otherwise, riskless profits could be made. This is known as covered interest arbitrage (CIA) and occurs whenever IRP does NOT hold.

- Covered interest arbitrage (CIA) should continue until interest rate parity is re-established, because the arbitrageurs are able to earn risk-free profits by repeating the cycle.
- But their actions nudge the foreign exchange and money markets back toward equilibrium:


### The Fisher Effect
- The Fisher effect (also called Fisher-closed) postulated by Irving Fisher states:
$$(1+i) = (1+r) \cdot (1+\pi)$$
$$i = r + \pi + r\pi$$

$\pi$ - inflation

$r$ - real interest rate

$i$ - nominal interest rate


This relation is often presented as a linear approximation stating that the nominal interest rate (i) is equal to a real interest rate (r) plus expected inflation ($\pi$)

$$i \approx r + \pi$$

### The International Fisher Effect

- The International Fisher Effect (also called Fisher-open or Uncovered Interest rate parity condition) states that the spot exchange rate should change to adjust for differences in <u>interest rates</u> between two countries:

$$\frac{S^{A/B}_{t, t+1}}{S^{A/B}_{t}} = \frac{1+i_{A}}{1+i_{B}}$$


