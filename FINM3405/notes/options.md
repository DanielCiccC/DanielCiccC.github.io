# FINM3405 Revision

# lecture 4-8 Options

1. Definitions and Concepts
2. Moneyness (ITM, ATM, OTM).
3. Payoffs vs profits (including the premium).
4. Main contracts and markets, contract specifications.
5. Pricing bounds and put-call-parity.
6. American call premium = European call premium when no dividends.
7. Time value and intrinsic value.

8. European option premiums/prices via the Black-Scholes model:
  - 8.1. On non-dividend paying assets.
  - 8.2. For dividend/income paying assets.
  - 8.3. For currencies (simply viewed as dividend paying assets).
9. Black-Scholes assumption of geometric Brownian motion and consequent log-normal distribution of the underlying asset’s price, or normal distribution of the asset’s returns.
10. Simulating geometric Brownian motion in preparation for the Monte Carlo approach to derivative security pricing.
11. Heuristic (non-rigorous) discussion of risk-neutral pricing.
12. Heuristic (hand-waving) interpretation of the factors affecting option prices, and quantification of this via the Black-Scholes model Greeks.

13. Using delta ∆ and gamma Γ to predict small changes in option prices due to small changes in the price of the underlying asset (in preparation for delta and delta-gamma hedging).
14. More detailed discussion of theta θ and associated concept of time decay, and how it relates to moneyness.
15. Scholes Hedging
  - 15.1 Static delta hedging
  - 15.2 Static delta-gamma hedging
  - 15.3 Dynamic delta hedging.
16. Implied volatility 
  - 16.1 volatility smile and term structure
  - 16.2 related VIX index enabling volatility to be directly traded.
17. Trading strategies and their payoff and profit/loss diagrams.

18. Binomial and Monte Carlo numerical option pricing methods:
  - 18.1 The need for numerical methods:
  - 18.2 Price more complex derivative securities.
  - 18.3 More complex pricing methods than the Black-Scholes model, in particular because returns are not normally distributed.
19. 1-period binomial model for European option price and delta.
  - 19.1 Multi-period binomial model for European option price and delta.
- More rigorous introduction of risk-neutral pricing via binomial model.
- Monte Carlo pricing of European options.
  - Simple method that simulates only final asset price.
  - More general method that simulates entire asset price paths in preparation for Monte Carlo pricing of path dependent options.

---
### Aside - Notation
- We work on a given time interval $0 ≤ t ≤ T$ where:
  - Time $t = 0$ is the date we enter into a contract.
  - Time $T$ is the expiry date.
  - Time $t$ is some intermediate date $0 ≤ t ≤ T$.
- $S_t$ is the underlying asset’s price at time $t$.
  - We write $S = S_{0}$ to reduce notation.
- $r$ is the risk free rate.
- $K$ is the strike or exercise price (some authors use X).
- $C_{t}$ and $P_{t}$ are the call and put prices (premiums) at time $t$.
  - Again, we write $C = C_{0}$ and $P = P_{0}$.
- $q$ dividend yield

Black Scholes
- $\sigma$ is the volatility of the underlying asset

---

# 1. Definitions and Concepts

Recall that there is two types of plain vanilla European options:
- **Call option**: Gives the holder the right but not the obligation to **buy** the underlying asset for the strike price $K$ on the expiry date $T$.
- **Put option**: Gives the holder the right but not the obligation to **sell** the underlying asset for the strike price $K$ on the expiry date $T$.


# 2. Moneyness
At time $t$ an option is:
- **In the money** if it has positive intrinsic value:
  - $K < S_{t}$ for a call option.
  - $S_{t} < K$ for a put option.
- **At the money** if $S_{t} = K$ (intrinsic value is 0).
- **Out of the money** if its intrinsic value is 0 and $S_{t} \ne K$
  - $S_{t} < K$ for a call option.
  - $K < S_{t}$ for a put option.

# 3 Payoffs and Profits

### 3.1 Payoffs

At any time $t$, an option’s **intrinsic** or exercise value (IV) is

call $IV_{t} = \max \{ 0, S_{t} − K \}$ 

and put $IV_{t} = \max \{ 0, K − S_{t} \}$

### 3.2 Profits
- call holder profit = $\max \{ 0, S_T − K \} − C$,
- put holder profit = $\max \{ 0, K − S_T \} − P$

and the writer’s (short position) profits are the negative of these:
- call writer profit = $C − \max \{ 0, S_T − K \}$,
- put writer profit = $P − \max \{ 0, K − S_T \}$.


# 4. Main contracts and markets, contract specifications.

- Will be given in final assignment


# 5. Pricing bounds and put-call parity

## 5.1 put-call parity

Developing mathematical models for pricing options (calculating the fair value of the option premium), such as the Black-Scholes option pricing model, is a major part of the theory and practice of options.

Form a portfolio long 1 European call and short 1 European put, both with the same underlying, strike and expiry.

This portfolio’s current price is C − P and its payoff at expiry is

$$\text{portfolio payoff} = \underbrace{\max\{0, S_T - K\}}_{\text{long call}} - \underbrace{\max\{0, K - S_T\}}_{\text{short put}}$$

## 5.2 Pricing bounds

1. First note that American options are worth at least as much as European options over the same underlying asset and with the same strike and expiry:

$$0 \le C_{Eu} \le C_{Am}$$
and 
$$0 \le P_{Eu} \le P_{Am}$$

American options can be exercised any time up to and including expiry

### 5.2.1 Option Pricing Bounds - American
**Lower Pricing bounds - American**
2. American options are worth at least their intrinsic (exercise) value:

$$\max \{0, S − K \} ≤ C_{Am}$$
and 
$$\max \{0, K − S \} ≤ P_{Am}$$

 because they can be exercised immediately

**Upper Pricing bounds - American**
3. American calls can never be worth more than the underlying spot price, and American puts can never be worth more than the strike:

$$C_{Am} ≤ S$$
and 
$$P_{Am} ≤ K$$

**Combined**

Combining the lower and upper bounds from the previous two slides leads
to the important pricing bounds for American options:

$$ \max \{ 0, S − K \} ≤ C^{Am} ≤ S $$
And
$$ \max \{ 0, K − S \} ≤ P^{Am} ≤ K$$


### 5.2.2 Option Pricing Bounds - European


**Upper Pricing bounds - European**

$$0 \le P^{Eu} \le Ke^{-rT}$$

because a European put can only be exercised at expiry, where it is known with certainty that their maximum payoff at expiry is $K$.

From this, deep in-the-money European puts can have *negative time value* (their premium can be less than their intrinsic value).

**Combined**

European calls

$$\max \{ 0, e^{-qT}S-e^{-rT}K \} \le C^{Eu} \le S$$

European puts

$$\max(0, e^{-rT}K - e^{-qT}S) \le P^{Eu} \le Ke^{-rT}$$

- Key note: discount exercise price to $t_0$

# 6. No early exercise of American calls

early exercise is never optimal for an American call option on a non-dividend-paying stock

- Under no dividends, so $q = 0$, from above we start with

$$\max (0, S − e^{−rT}K) ≤ C^{Eu} ≤ C^{Am}$$

- If $r > 0$ then $e^{−rT} K < K$ and we get a strict inequality

$$\max(0, S − K) < \max (0, S − e^{−rT}K) ≤ C^{-rT} ≤ C^{Am}$$

But $\max(0, S − K)$ is just the call’s intrinsic value. So if there’s no dividends, call options will always have strictly *positive time value*.

# 7. Time value and intrinsic value.

From above, we noticed that call options on non-dividend-paying stocks have a premium that is strictly larger than the option’s intrinsic value.
$$\text{time value = premium − intrinsic value}$$

# 8. European option premiums/prices via the Black-Scholes model
The Black-Scholes European option pricing model is a mathematical equation for pricing plain vanilla European call and put options.

## 8.1 European option premiums on non-dividend paying assets
Black-Scholes European call option pricing model is

$$C = S\mathcal{N} (d_{1}) − Ke^{−rT}\mathcal{N} (d_{2})$$

Where:

$$d_{1} = \frac{\log \frac{S}{K} + (r+\frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

And 

$$d_{2} = d_{1} - \sigma \sqrt{T}$$
$$= \frac{\log \frac{S}{K} + (r -\frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

## 8.2 European option premiums incorporating dividends

pricing equations for European call $C$ and put #$P$ options become

$$C = Se^{-qT}\mathcal{N} (d_{1}) − Ke^{−rT}\mathcal{N} (d_{2})$$

$$P =  Ke^{−rT}\mathcal{N} (-d_{2}) - Se^{-qT}\mathcal{N} (-d_{1})$$

Where:

$$d_{1} = \frac{\log \frac{S}{K} + (r - q + \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

And 

$$d_{2} = d_{1} - \sigma \sqrt{T}$$
$$d_{2} = \frac{\log \frac{S}{K} + (r - q - \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

## 8.3. European option premiums for currencies
We view the foreign risk-free rate $r_f$ as the “dividend” on the underlying asset (the foreign currency):

$$C_{f:d} = S_{f:d}e^{-r_fT}\mathcal{N} (d_{1}) − K_{f:d}e^{−r_dT}\mathcal{N} (d_{2})$$

$$P_{f:d} =  K_{f:d}e^{−r_dT}\mathcal{N} (-d_{2}) - S_{f:d} e^{-r_fT}\mathcal{N} (-d_{1})$$

Where:

$$d_{1} = \frac{\log \frac{S_{f:d}}{K_{f:d}} + (r_d - r_f + \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$

and 

$$d_{2} = d_{1} - \sigma \sqrt{T}$$
$$ = \frac{\log \frac{S_{f:d}}{K_{f:d}} + (r_d - r_f - \frac{1}{2}\sigma ^{2})T}{\sigma \sqrt{T}}$$


## 9. key features/Assumptions of Black Scholes

1. We’re using historical volatility for σ but in practice options traders tend to use the Black-Scholes model with “rules of thumb” and their own estimates of σ.
2. Our dividend yield may not be accurate: We assumed a continuously compounded yield. It should be a forecast. And should we incorporate dividend imputation/franking?

Geometric Brownian Motion
- underlying assets follows geometric brownian motion
- Stock price $S_t$ in black Scholes model is log-normally distributed

## 10. Simulating geometric Brownian
- You can iteratively simulate geometric brownian motion over each subinterval to create a complete path
- Used in the Monte-Carlo simulation pricing of options (outlined below)

So in the risk-neutral pricing approach the value of a European option is
- the present value of its expected future payoff
- but discounted at the risk-free rate r.

# 12. Factors affecting options prices
How each of the input variables $K$, $S$, $r$, $T$, $σ$ and $q$ impact option premiums

We’re interested in the sensitivity of option prices to the other variables
$S$, $r$, $T$ and $σ$, and we give these sensitivities special Greek names:
- **Delta ∆** is the sensitivity of the option price to S.
- **Gamma Γ** is another measure of the relation between prices and S.
- **Rho ρ** is the sensitivity of the option price to rates r.
- **Vega ν** is the sensitivity of the option price to volatility σ.
- **Theta θ** is the sensitivity of the option price to time T.

## 12.1 Delta and Gamma
We know that as $S$ increases, calls premiums rise and put premiums fall.

![alt text](assets\IMG69.PNG)

We quantify this mathematically with the delta ∆, given by

$$∆_{C} = N(d_{1}) \: \: \text{and} \: \: ∆_{P} = N(d_{1}) − 1$$

Importantly, note the following

$$ 0 < ∆_{C} < 1 \: \: \text{and} \: \: -1 < ∆_{P} < 0$$

We interpret ∆ as the change in the premium due to a change in S, giving us the approximations

$$dC \approx \Delta _{c} dS \: \: \text{and} \: \: dP \approx \Delta _{p} dS $$

where $dC$ and $dP$ are a change in the premium and $dS$ a change in $S$.

We calculate the “new” premiums due to a change in S as

$$C_{new} \approx C + dC \: \: \text{and} \: \: P_{new} \approx P+dP $$

## 12.2 Rho

Rho ρ is the change in the premium from a change in $r$, and is given by

$$\rho_c = KTe^{-rT}\mathcal{N}(d_2)$$
and 
$$\rho_p = KTe^{-rT} \left[ \mathcal{N}(d_2) -1 \right]$$

Where 

$$0 < \rho_c$$
and
$$\rho_p < 0$$

| Example for call prices: |
| --- |
| ![alt text](assets\IMG258.PNG) |
(x axis is underlying stock price)

As $r$ increases, call premiums increase but put premiums decrease.
- An intuitive explanation for this is the present value $e^{−rT}K$ of the strike that the holder pays in a call, or receives in a put, decreases.

## 12.3 Vega
Vega ν is the change in the premium from a change in σ, and is given by:

$$\nu = Sf(d_{1})\sqrt{T}$$

- Same for calls and puts

with $f(x)$ the PDF of a standard normal random variable. Note that

$$0 < \nu$$

As σ increases, option premiums increase.

## 12.4 Theta

Theta θ is a bit ambiguous. It gives the *negative* of the change in the premium from a change in T. And the equations are more complex:

$$\theta_c = -\frac{Sf(d_1)\sigma}{2\sqrt{T}} -rKe^{-rT}\mathcal{N}(d_2)$$
and
$$\theta _p = \theta _c + rKe^{-rT}$$

θ is the *negative* of the partial derivative of the premium with respect to T, telling us the impact of approaching expiry.

$$\theta _c < 0$$
but we may have 
$$\theta _p \le 0$$
and 
$$ 0 \le \theta _p $$

- Impact of time on puts is ambiguous: From $\theta _{P} = \theta _{C} + rKe^{-rT}$ deep in-the-money put (large K) premiums may increase as expiry nears.
- This relates to something said last week: A deep in-the-money put is already close to its maximum payoff of K, so not much more payoff can be realised at expiry, but there is still a chance of an unfavourable movement in the asset price. But as we approach expiry, there is less chance of an unfavourable movement.


### 12.4.1 Time Decay
Premiums usually fall as expiry approaches

- Time decay works for option writers and against option holders.
- θ is most negative for options close to at-the-money.
- θ in fact gets more negative for options close to at-the-money as expiry approaches: Time decay “speeds up” as expiry approaches.

| Theta Call | Theta Put | 
| --- | ---
![alt text](assets\IMG78.PNG) | ![alt text](assets\IMG79.PNG)
![alt text](assets\IMG259.PNG) | ![alt text](assets\IMG260.PNG)



- 13. Using delta ∆ and gamma Γ to predict small changes in option prices due to small changes in the price of the underlying asset (in preparation for delta and delta-gamma hedging).
- 14. More detailed discussion of theta θ and associated concept of time decay, and how it relates to moneyness.
- 15. Scholes Hedging
  - 15.1 Static delta hedging
  - 15.2 Static delta-gamma hedging
  - 15.3 Dynamic delta hedging.
- 16. Implied volatility 
  - 16.1 volatility smile and term structure
  - 16.2 related VIX index enabling volatility to be directly traded.
- 17. Trading strategies and their payoff and profit/loss diagrams.

- 18. Binomial and Monte Carlo numerical option pricing methods:
  - 18.1 The need for numerical methods:
  - 18.2 Price more complex derivative securities.
  - 18.3 More complex pricing methods than the Black-Scholes model, in particular because returns are not normally distributed.
- 19. 1-period binomial model for European option price and delta.
  - 19.1 Multi-period binomial model for European option price and delta.
- More rigorous introduction of risk-neutral pricing via binomial model.
- Monte Carlo pricing of European options.
  - Simple method that simulates only final asset price.
  - More general method that simulates entire asset price paths in preparation for Monte Carlo pricing of path dependent options.