# Lecture 8 Revision
# International Capital Budgeting

### Net present Value
- The NPV is the present value of future cash flows 
discounted at an appropriate rate minus the initial 
net cash outlay for the project. 
- In mathematical terms, the formula for net present 
value is: 

$$NPV = -I_{0} + \sum ^{ \infty}_{t=1}\frac{CF_{t}}{(1+r)^{t}}$$

- Projects with a positive NPV should be accepted; negative NPV projects should be rejected. 
- The discount rate is the expected rate of return on projects of similar risk.

### Free Cash Flow Definitions
![alt text](assets\IMG144.PNG)

### Cash flows to Claimholders

![alt text](assets\IMG145.PNG)

### Adjusted Present Value

$$APV = NPV(100\% equity financed) + PV(tax shields) + PV(other imperfections)$$

### Stage 1: Project is 100% Equity Financed

Cash-flows: Need Free Cash Flows.
- You need the rate that would be appropriate to discount the firm’s cash flows as if the firm/project were 100% equity financed.
- This rate, $r_{A}$, is the expected return on equity if the firm were 100% equity financed.
- To determine the return on assets ( $r_{A}$ ), you need to:
  - Find comparables, i.e., publicly traded firms in same business.
  - Estimate their expected return on equity if they were 100% equity financed by unlevering.

### Stage 2: PV of Tax Shields
- The expected tax saving is $\tau_{c}r_{d}D$ where $\tau_{c}$ is the corporate tax rate
  
  - If D (the amount of borrowing) is expected to remain stable, then discount $\tau_{c}r_{d}D$ using $r_{d}$

$$PV(TS) = \frac{\tau_{c}r_{d}D}{r_{D}} = \tau_{C}D$$

If the leverage ratio (i.e. D?V) is expected to remain stable, then discount $\tau_{c}r_{d}D$ using $r_{A}$

$$PV(TS) = \frac{\tau_{c}r_{d}D}{r_{A}}$$

- Intuition:
  - If D/V is constant, $\tau_{c}r_{d}D$  moves up/down with V
  - The risk of $\tau_{c}r_{d}D$ is similar to that of the firm’s assets, so use $r_{A}$

### Stage 3: PV of Other “Imperfections”
1. PV of Distress Costs
- These arise when firms take on debt
  - Direct costs of financial distress
  - Indirect costs of financial distress
- They tend to be difficult to estimate 
  - Usually ignored.
2. The Costs of Issuing Securities
3. PV of Subsidised Financing

### Parent vs Subsidiary Cash flows
- Whose perspective should the analysis take?
  - Substantial difference between the parent vs subsidiary (project) cash flows
    - Royalty payments
    - Licensing agreements
    - Overhead management fees
    - The purchase of inputs from the parent
  - The role of taxation and exchange controls
  - The effect of exchange rates

### Cash flows of subsidiary

![alt text](assets\IMG194.PNG)

![alt text](assets\IMG195.PNG)

### Cash flow of parent

![alt text](assets\IMG196.PNG)

![alt text](assets\IMG197.PNG)

### What about exchange rates?
- Firms have revenues and costs in multiple currencies.
- **First Approach:** Local Currency NPV 
  - Perform revenue and cost projections using local currency figures and then discount cash flows at the local currency cost of capital. Then convert local currency NPV to dollars (home 
currency) using current spot rate
  - Denoted as 
  
  ![alt text](assets\IMG154.PNG)


- **Second Approach**: Period-by-Period Conversion
  - Use local currency projections and convert each periods cash 
flow into dollars using the forward rate or exchange rate 
projections.

![alt text](assets\IMG155.PNG)

  - Discount the dollar cash flows with a dollar (or home country) discount rate with adjustments for country and project risks.
  - Explicit about exchange rate movements and discount rate adjustments.
  - Easier to perform sensitivity analysis.

### Example: Horse for Courses

- Investment banker/ Fund manager/ Executive of domestic firm: Focus on domestic firm/project
  - Local, single country CAPM:

$$E(r_{i}) = r_{f, Local} + \beta_{i}E(r^{M}_{Local}-r_{f, Local})$$

A real world application of the above:

$$E(r_{BHP}) = r^{Aust}_{f} + \beta_{BHP, ASX200} E(r_{ASX200} - r^{Aust}_{f})$$

The issue is it assumes that the assets of a country are held only by local (Australian) investors, hence there would be no international diversification of risk.

- How would an Australian fund manager evaluate a foreign firm to include in his portfolio?
- How would a manager estimate the cost of capital for an overseas project? Say in Chile.
- Should there be an additional risk premium for country (political) risk? 
  - It depends in whether the risk is diversifiable or not. To answer this the manager needs to know
- Who the marginal investor is and what type of portfolio they hold?
- Is the country risk country specific, i.e., are the correlations between countries low?

### Country Risk

- If country risk matters, how would they estimate the risk premium?

**Historical Risk Premiums**
- Calculate the average equity market risk premiums $\overline{R_{M}-R_{f}}$ over a period 
of time.
- What are the problems with this approach?

- Modified Historical Risk Premiums 
$$\text{Equity Risk Premium} = \text{Base premium for developed market} + \text{country risk premium}$$
- Country equity risk premium reflects the **additional risk** of investing in a specific emerging market (e.g., Chile). This needs to be estimated.

**Measures of country risk **
1. Sovereign rating from S&P & co. The S&P rating for Chile is A (investment grade).
2. Country risk scores from International Country Risk Guide.
3. Do own research by studying economic fundamentals, state of the country’s equity market. 

- Now we need to estimate the premium this risk would command.

### Measures of Country Risk premiums

Bond Default spreads:

$$Yield^{Emerging market}_{USD}-Yield^{developed market}_{USD}$$

- Requires: (a) yields on country bonds issued by the emerging market (e.g., Chile) denominated in USD or other hard currencies; (b) yield on developed market bonds of the same maturity in the same hard currency. The US market is usually used as a proxy for the developed market.

$$\text{Country Premium} = \text{Bond Yield}^{Chile}_{USD} - \text{Bond Yield}^{US}_{USD}$$

- Relative Equity Market Standard Deviations: Incorporates equity risk (standard deviation of stock returns). Higher risk implying higher premiums. 

$$\text{Risk Premium}_{\text{Emerging mkt}} = \text{Risk Premium}_{\text{Developed mkt}} \cdot \frac{\sigma_{\text{emerging mkt}}}{\sigma_{\text{Developed mkt}}}$$

$$\text{Country Premium} = \text{Risk Premium}_{text{Emerging mkt}} - \text{Risk Premium}_{\text{Developed mkt}}$$

**Bond Default Spreads + Relative Equity Market Standard Deviations:**
- Default spreads only captures default risk. The risk associated with investing in equity has to be greater than default risk. So, we would expect equity risk premium to be LARGER than bond default spreads. The premium will increase is the country’s sovereign rating is downgraded or if 
the relative volatility of the equity market increases.

$$\text{Country Premium} = \text{Default Spread} \cdot \frac{\sigma_{\text{Equity}}}{\sigma{\text{Country Bond}}}$$

### The cost of Equity Capital
- For valuing emerging market firms/projects – the options are varied

**Brute force method**

$$E(r_{i}) = r_{f} + \beta_{i}E(r^{M}_{Developed} -r_{f}) + \text{Country Risk Premium}$$

**Beta Method**

$$E(r_{i}) = r_{f} + \beta_{i}E[r^{M}_{Developed} -r_{f} + \text{Country Risk Premium} ]$$

- Use this approach if the belief is that not all companies in the developing market is equally exposed to country risk. 

**Local country risk exposure model**

$$E(r_{i}) = r_{f} + \beta_{i}E(r^{M}_{Developed} -r_{f}) + \lambda \cdot \text{Country Risk Premium}$$

- $\lamda$  firm’s exposure to local country risk. This could be  estimated as the % of revenues the firm derives from the local country relative to the % of revenues in the country for the average company.

