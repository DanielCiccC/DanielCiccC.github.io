# Revision Lecture 7
# Cost of Capital & Political Risk

- Cost of capital can be defined as the MINIMUM rate of return a firm has to pay in order to entice 
investors to buy and hold its securities.
  - Given by WACC – weighted average of the financing costs
- Question:  Should the cost of capital of foreign projects be higher or lower than that of domestic investment?

**Integrated**
- If all capital markets are fully **integrated**, securities of comparable expected return and risk should have the same required rate of return in each national market after adjusting for foreign exchange and political risks.

**Segmented**
- A national capital market is **segmented** if the required rate of return on securities in that market differs from that for securities of comparable expected return traded on other national securities markets (e.g., New York and London).

### Causes of Segmentation
- Market segmentation is a financial market 
imperfection caused by government constraints and investor perceptions.
- The most important imperfections are:
  - Information Barriers – Lack of transparency & information disclosure
  - Market illiquidity
  - Transaction Costs
  - Regulatory Barriers/Capital Controls
  - Foreign Exchange Risk
  - Country Risk (and Political Risk)

### Market liquidity

- Market Liquidity is the degree to which a firm can issue a new security without depressing the existing market price, as well as the degree to which a change in price of its securities elicits a substantial order flow.

### Transaction Costs
- How much does it cost to buy or sell securities? 
- Why is this important to know?
  1. Transactions costs can wipe out trading profits, so ignoring them lead to incorrect asset allocation strategies. 
  2. Price impact in emerging markets, a.k.a. “hot money”, can destabilize markets. 

### Measuring Country Risk
- Difficult to define and therefore to measure 

$$\text{Country risk = ability to pay + willingness to pay}$$
- Incorporates political stability and economic measures, capital flight, a country’s resource base and privatization measures, sovereign rating etc. Long run economic health is a good indicator.

### What about capital controls?
- Various foreign exchange controls are often imposed, especially in Emerging Markets. 
- Some countries have special classes of shares for foreigners (e.g., China, Mexico, Philippines)
- Some allow only “authorized foreign investors” to trade in their markets (e.g., India, Taiwan).
- Different classes of shares and their pricing: shares for foreign investors may sell at a discount or premium to domestic shares.
- Repatriation restrictions (e.g., Chile, Malaysia) and the prevention of conversion from local currency into foreign currency.

### ICRG Country Risk Components

- International country risk guide
  - Religious tensions, law and order, corruption
  - Quality of the bureaucracy
  - able to pay off foreign debts; 
  - Corruption

![alt text](assets\IMG131.PNG)
![alt text](assets\IMG132.PNG)

### Corruption
- Illegitimate payments and favors outside the rule of law
- Corruption occurs to some extent in all countries, but large differences across countries exist 

### Political Risk

Political Risk
- Political Risk can be described the influence of non-business events on the value of the firm.
- It is more than Expropriation. Can also be
  - currency or trade controls
  - changes in tax or labour laws
  - changes in ownership policies
  - Political problems etc.
- Political Risk can be decomposed into:
  - Macro Risk which affects all firms
    - Expropriation (See slide on Russian Oligarchs; Argentina)
    - Ethnic Strife (Balkans, Rwanda, Russia/Ukraine etc.)

- **Expropriation** is defined as official government seizure of private property.


### Hedging Political Risk
1. Take conservative approach:
  - Adjust NPV for political risk.
  - Political risk may be diversifiable to some extent.
  - Don’t put all your eggs in one basket.
2. Minimize exposure to political risk:
  - Joint Venture
  - Consortium of international companies
  - Use local debt
3. Purchase insurance:
  - Private insurance (Lloyd’s of London, AIG)
  - Government export credit agencies (OPIC in the US and EFIC in Australia)

### Estimating the Cost of Capital
- The Weighted Average Cost of Capital/Discount Rate/Hurdle 
Rate
  - The opportunity cost of investing capital in projects of similar risk and duration

$$WACC=E(r_{e})\cdot \frac{E}{V} + E(r_{d})(a+\tau)\frac{D}{V}$$

  - The Cost of Equity given by the CAPM

$$ E(r_{e}) = r_{f} + \beta_{e}(E(r_{M})-r_{f})$$

- $r_{f}$ the risk free rate, 
- $\beta_{e} = cov(r_{e}, r_{m}) / var(r_{m})$
- $E(r_{M})-r_{f}$ the market risk premium

- To estimate the CAPM:
  - We need data on returns on equity, return on the market portfolio and interest rate on risk-free asset
  - Obtain an estimate of $\Beta _{e}$
  - Determine the market risk premium

**Domestic CAPM**

$$ E(r_{i}) = r_{f} + \beta^{Domestic}_{e}((r^{D}_{M})-r_{f}), \;\;\; \beta_{i} = \frac{cov(r_{i}, r^{D}_{M})}{var(r^{D}_{M})}$$

- Substituting the definition of beta into the cost of capital formula we get

$$ E(r_{e}) = r_{f} + cov(r_{i}, r^{D}_{M})\frac{[(r^{D}_{M})-r_{f}]}{var(r^{D}_{M})}$$

**World CAPM:**

$$ E(r_{e}) = r_{f} + \beta^{World}_{e}(E(r^{W}_{M})-r_{f}), \;\; \beta_{e}^{W} = \frac{cov(r_{i}, r^{W}_{M})}{var(r^{W}_{M})}$$

### Applying the CAPM
- From the capital raising firms’ point of view, the cost of 
capital should be lower due to globalization. Why?
  - As investors become better diversified, they require a smaller risk premium for capital.
- Stulz (1995) determines the cost of (equity) capital for Nestlé.*
  - Which market portfolio? The options are the Swiss Market Index or the World Market Index

![alt text](assets\IMG141.PNG)

### Getting the benchmark wrong
- How large is the error likely to be?
1. First, estimate expected return of the home market (i.e., Swiss 
market) on the World market portfolio.

$$ E(r_{Home}) = r_{f} + \beta_{Home}^{World}(E(r^{W}_{M})-r_{f})$$

2. Next, estimate the difference between the two costs of equity capital for Nestlé (domestic CAPM – world CAPM) 

$$\text{Error} = [r_{f} + \beta^{Home}_{Nestle}((r^{Home}_{M})-r_{f})] - [\beta^{World}_{Nestle}((r^{W}_{M})-r_{f})]$$

$$= (\beta^{Home}_{Nestle} \cdot \beta_{Home}^{World} - \beta^{World}_{Nestle}) [r^{W}_{M}-r_{f}]$$

Error in beta:

$$(\beta^{Home}_{Nestle} \cdot \beta_{Home}^{World} - \beta^{World}_{Nestle})$$ 

$$= (0.885 \cdot 0.737) - 0.585 = 0.067$$

Stulz assumes an excess return on the world market portfolio $E(r_{M}^{W}) - r_{f}$ of 5.4%

$$\text{Error}= 0.067 \cdot 0.054 = 0.0036 = 0.36\%$$

- Using the domestic CAPM would mean that the expected return for Nestle is 0.36% **higher** than is should be

