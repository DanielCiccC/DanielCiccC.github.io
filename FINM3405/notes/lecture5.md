# Lecture 5

The Black-Scholes European option pricing model is a mathematical
equation for pricing plain vanilla European call and put options.

> In general the “Black-Scholes model” is a mathematical framework in which we derive mathematical models for pricing derivatives.

In the Black-Scholes framework, some types of derivatives have nice
equations for their price or value, but most do not. When they don’t, we
have to use numerical methods to approximate the solution, such as:
- Lattice based method like the binomial and trinomial models.
- Monte Carlo simulation methods.
- Numerically solving partial diff erential equations.

> - Focus on the black-Scholes framework
>   - Standard market model
>   - Can derive a clean neat price for the derivatives
>   - Not going to focus on complex derivative securities
> - Model itself is pretty unique, and do have a formula for their price
>   - most models you cannot derive a formula, sometimes they don't even exist
> - Use numerical techniques
>   - Not going to solve partial differential equations
>     - which represents the price of the derivative


This week we cover the Black-Scholes option pricing model for:
- The basic equations for European options.
- European options on equities or indices that pay a dividend yield $q$.
- European currency options, being mindful of the domestic $r_{d}$ and
foreign $r_{f}$ risk-free rates, as well as currency quoting conventions. In later weeks we cover numerical methods for other types of options that don’t have neat Black-Scholes pricing equations.

> - numerical methods will be in-semester test

Quite simply, the Black-Scholes European call option pricing model is

$$C = S\mathcal{N} (d_{1}) − Ke^{−rT}\mathcal{N} (d_{2})$$

Where:

$$d_{1} = \frac{\log \frac{S}{K} + (r+\frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

And 

$$d_{2} = d_{1} - \sigma \sqrt{T}$$
$$d_{2} = \frac{\log \frac{S}{K} + (r -\frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

Let’s recall the notation and variables in the Black-Scholes model:

### Notion and variables

- The current date is time $t = 0$.
- $C$ is the current European call option premium.
- $T$ is the expiry date (and also time to expiry).
- $S$ is the current price of the underlying asset.
- $r$ is the risk-free rate.
- $K$ is the exercise or strike price.


First, $\sigma$ is the volatility of the underlying asset, which we can take as the
standard deviation of its continuously compounded annual returns.
- $\sigma$ can be calculated from historical data as follows:

![alt text](assets\IMG59.PNG)

> - sample of daily prices of the asset
> - N+1 price observations, N daily returns
> - Calculate the sample standard deviation
>
> Traders don't use historical data, they use market

Second, $\mathcal{N}(x)$ is the CDF evaluated at $x$ of a standard normal random
variable $X$. It gives the probability that $X$ is less than or equal to $x$:

$$\mathcal{n}(X) = \mathbb{P}(X \le x) = \frac{1}{\sqrt{2 \pi}} \int^{x}_{- \infty } e^{- \frac{z^{2}}{2}} dz$$

Graphically, it’s the area under the standard normal PDF:

![alt text](assets\IMG60.PNG)


> - Probability standard normal random variable $\le$ x
> - Area under the curve of standard probability density function
> - Use computers to calculate it for us

**Python**
```python
In [1]: from scipy . stats import norm
In [2]: x = 0.75
In [3]: N = norm.cdf(x) # SciPy ’s norm.cdf () is N()
In [4]: N
Out [4]: 0.7733726476231317
```

### Black Scholes Model

**In R**
```r
S = 50
K = 50
r = 0.05
T = 1/2
sigma = 0.25
d1 = (log(S/K) + (r + 0.5* sigma ^2)*T)/( sigma *sqrt(T))
d2 = d1 - sigma *sqrt(T)
C = S* pnorm (d1) - K*exp(-r*T)* pnorm (d2)
```

Gives:
```r
> C
[1] 4.130008
```

**In Python**
```Python
import numpy as np
from scipy . stats import norm
S = 50
K = 50
r = 0.05
T = 1/2
sigma = 0.25
d1 = (np.log(S/K) + (r + 0.5* sigma **2)*T)/( sigma *np.sqrt(T))
d2 = d1 - sigma *np.sqrt(T)
C = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
```
gives

```python
In [1]: C
Out [1]: 4.130007599671615
```

Use the yfinance Python module to calculate the historical
volatility of the S&P/ASX 200 Index and price some September index
option contracts, where here we’ll ignore dividends (for now).

**Interest Rates** | **Option Prices**
| --- | ---
![alt text](assets\IMG61.PNG) | ![alt text](assets\IMG62.PNG)

```python 
 import numpy as np , yfinance as yf
 from scipy . stats import norm
 P = yf. download ("^AXJO")["Adj Close "]
 ret = np.log(P).diff (1). dropna ()
 sigma = np.std(ret)*np.sqrt (252)
 K = 7775; S = 7761.7; T = 41/365
 r = (0.042923+0.04335) /2 # average of 1 & 2 month BBSW rate
 d1 = (np.log(S/K) + (r + 0.5* sigma **2)*T)/( sigma *np.sqrt(T))
 d2 = d1 - sigma *np.sqrt(T)
 C = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2) # call price
 P = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1) # put price
```

This code gives σ = 0.15375 and European call and put prices

```
1 In [1]: C
2 Out [1]: 171.73
3 In [2]: P
4 Out [2]: 147.45
```

> - options prices potentially be off - using historical volatility and options traders don't do that
>   - us their own market conventions


## Black-Scholes Model Puts

$$P =  Ke^{−rT}\mathcal{N} (-d_{2}) - S\mathcal{N} (-d_{1})$$

where all variables and notation are as above.
- Alternatively, we can use put-call parity:

$$P = C + e^{−rT}K − S$$

We check that they agree, using the original “generic” example above:

```python
P = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
P1 = C + np.exp(-r*T)*K - S # using put -call parity
```

> - Exam situation, formula will be provided

### Incorporating dividends

We now incorporate dividends into the Black-Scholes European option pricing equations, in order to more accurately price equity options.

Incorporating a continuously compounded dividend yield $q$ into the basic Black-Scholes model is relatively easy. We can show that the pricing equations for European call $C$ and put #$P$ options become

$$C = Se^{-qT}\mathcal{N} (d_{1}) − Ke^{−rT}\mathcal{N} (d_{2})$$

$$P =  Ke^{−rT}\mathcal{N} (-d_{2}) - S e^{-qT}\mathcal{N} (-d_{1})$$

Where:

$$d_{1} = \frac{\log \frac{S}{K} + (r - q + \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

And 

$$d_{2} = d_{1} - \sigma \sqrt{T}$$
$$d_{2} = \frac{\log \frac{S}{K} + (r - q - \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

> - Black Scholes prices of plain vanllia options including dividends

```python
import numpy as np , yfinance as yf
from scipy . stats import norm
XJO=yf. download ("^AXJO")["Adj Close "]
ret=np.log(XJO).diff (1). dropna (). rename (" returns ")
sigma =np.std(ret)*np.sqrt (252)
K =7775; S =7761.7; T =41/365; q =0.042 # dividend yield 4.2%
r =(0.042923+0.04335) /2 # average of 1 & 2 month BBSW rate
d1 =( np.log(S/K)+(r-q +0.5* sigma **2)*T)/( sigma *np.sqrt(T))
d2=d1 - sigma *np.sqrt(T)
C=S*np.exp(-q*T)*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
P=K*np.exp(-r*T)*norm.cdf(-d2)-S*np.exp(-q*T)*norm.cdf(-d1)
```
This code gives European call and put prices

```
In [1]: C
Out [1]: 152.87
In [2]: P
Out [2]: 165.12
```

**Remark:**

Some reasons for inaccurate S&P/ASX 200 Index option prices:
- We’re using historical volatility for σ but in practice options
traders tend to use the Black-Scholes model with “rules of
thumb” and their own estimates of σ.
- Our dividend yield may not be accurate: We assumed a
continuously compounded yield. It should be a forecast. And
should we incorporate dividend imputation/franking?
- The time stamps on our data don’t align.

## Currency Options

When applying the Black-Scholes model to pricing currency options, we
need to be mindful about the currency quoting conventions of S and K,
as well as the handling of the domestic $r_{d}$ and foreign $r_{f}$ interest rates.
- Let’s recall our currency quoting convention:


Let $S_{f:d}$ and $K_{f:d}$ be the spot and strike prices of 1 unit of the foreign
currency (the underlying asset) in terms of the domestic currency.

The modification to the Black-Scholes model is relatively easy:

- It turns out that we view the foreign risk-free rate r f as the
“dividend” on the underlying asset (the foreign currency):

> - Cutting out messiness, European options on currencies is the same as dividend yields

$$C_{f:d} = S_{f:d}e^{-qT}\mathcal{N} (d_{1}) − K_{f:d}e^{−rT}\mathcal{N} (d_{2})$$

$$P_{f:d} =  K_{f:d}e^{−rT}\mathcal{N} (-d_{2}) - S_{f:d} e^{-qT}\mathcal{N} (-d_{1})$$

Where:

$$d_{1} = \frac{\log \frac{S_{f:d}}{K_{f:d}} + (r - q + \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

And 

$$d_{2} = d_{1} - \sigma \sqrt{T}$$
$$d_{2} = \frac{\log \frac{S_{f:d}}{K_{f:d}} + (r - q - \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

This is sometimes called the **Garman-Kohlhagen (GK)** equations, who
suggested in their paper Foreign Currency Option Values the idea of
viewing a currency option as an option on a stock paying a dividend $r_{f}$.

### Example
We use Python to download exchange rates and price a 3-month
at-the-money EUR:USD currency option (EUR = foreign currency).

> - SOFR - risk free interest rate in America
> - Euribor - $r_{f}$ in Euro


|SOFR | Euribor | Spot| 
| --- | --- | ---
|![alt text](assets\IMG63.PNG)|![alt text](assets\IMG64.PNG)| ![alt text](assets\IMG65.PNG)

Let’s fi rst convert the simple Term SOFR and EURIBOR interest
rates to continuous compounding. The future value of \$1
invested at a simple interest rate $s$ is $1 + sT$. Under compound
interest $r$, it is $e^{rT}$. Hence, for each of these rates, we want to find $r$ satisfying $1 + sT = e^{rT}$. Rearranging, we get

$$r=\frac{1}{T}\log (1+sT)$$

I calculate the continuously compounded rates to be $r_{f} = 0.03553$ and $r_{d} = 0.05071$.


```python
import numpy as np , yfinance as yf
from scipy . stats import norm
EURUSD = yf. download (" EURUSD =X")["Adj Close "]
ret = np.log( EURUSD ).diff (1). dropna ()
sigma = np.std(ret)*np.sqrt (252)
T = 90/360; S = 1.1024; K = S # at -the - money
rf = (360/90) *np.log (1+0.03569*90/360) # Euro is the foreign currency
rd = (360/90) *np.log (1+0.0510283*90/360) # USD is the domestic currency
d1 = (np.log(S/K) + (rd -rf +0.5* sigma **2)*T)/( sigma *np.sqrt(T))
d2 = d1 - sigma *np.sqrt(T)
C = S*np.exp(-rf*T)*norm.cdf(d1) - K*np.exp(-rd*T)*norm.cdf(d2)
P = -S*np.exp(-rf*T)*norm.cdf(-d1) + K*np.exp(-rd*T)*norm.cdf(-d2)
```

This code gives $σ = 0.11245$ and call and put option values

```
In [1]: C
Out [1]: 0.0266
In [2]: P
Out [2]: 0.0225
```

## Risk-neutral pricing and geometric Brownian motion
The ideas of risk-neutral pricing and geometric Brownian motion are central to all of quantitative finance and derivative security pricing.
- We touch on the very basics as a starting point into more advanced quantitative finance.
- We will also use both concepts for pricing options via Monte Carlo simulation in a few weeks time.

> - Risk-neutral approach
>   - Present some exotic options, priced with Monte Carlo techniques


It’s important to note that the Black-Scholes model is derived under a
large list of assumptions. Some of these include what might be called the
“usual assumptions” in financial theory and modelling:
- Constant risk-free rate r and volatility σ over life of option.
- No restrictions on borrowing and lending.
- Borrowing and lending rates are equal.
- No transaction costs like brokerage, bid-ask spreads, taxes, etc.
- Assets are infinitely divisible (can buy “1.0346” units).
- No restrictions on short selling.
- Trading is continuous (at infinitesimally small time intervals).
- There are no arbitrage opportunities in markets.

> - Standard market modelling - Black Scholes
>   - usual assumptions you come across in classical theory
>   - Assumptions around people's behaviour
>   - Borrowing and lending rates equal, etc.

We’re not so much interested in them as we are in the assumption on the
stochastic or random process followed by the underlying asset.
- This assumption basically characterises the Black-Scholes framework
and tells us the correct interpretation of the volatility parameter σ.
In the risk-neutral pricing approach, we can prove that the underlying
asset follows **geometric Brownian motion (GBM)**

$$S_{t} = Se^{(r-\frac{1}{2} \sigma ^{2})t + \sigma \sqrt{t} Z} \: \: \text{for} \: \: 0 \le t \le T$$

> - Assumptions of the underlying asset
> - Underlying assets returns are normally distributed

