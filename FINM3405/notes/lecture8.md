# Lecture 8
# Week 8: Pricing American and path-dependent options

> - Path dependent options (exotic and simple conceptually)
> - Vanilla puts and calls are tip of the iceberg
> - Don't have closed formed solutions for many of these, need to use numerical methods


This week we use the binomial and Monte Carlo methods to price:
1. American options (don’t have closed-form Black-Scholes prices).
2. Some simple exotic path-dependent options (some actually do haveclosed-form solutions but we largely ignore them).

The binomial model and Monte Carlo method (and PDE approach) have strengths and weaknesses. One should always use the computational technique that is most tractable, practical, accurate, efficient and numerically stable for the pricing application at hand, and we’ll do this.

## American options

An American option gives the holder the right (but not the obligation)
to exercise it at any point up to and including the expiry date $T$.

- This early exercise feature actually introduces quite a bit of mathematical complexity into the pricing of American options.
- We immediately run into the problem of not having a closed-form solution for the price of an American option.

**Remark** Recall that the price of American and European call options coincide on non-dividend-paying stocks.
- Can use the Black-Scholes model for these American calls.

> American option, exercise any time up to


In these notes we’ll use the binomial model for pricing American options since it’s conceptually very simple and is also very accurate.

- Modifying the Monte Carlo approach for American options is conceptually and mathematically a bit of a stretch for FINM3405.
- The PDE approach is extensively used for American options but it’s mathematically a bit beyond FINM3405.


A very simple adjustment needs only be made to our previous binomial model approach of stepping backwards through the asset price tree in order to price American options, and it is motivated by some of the pricing bounds previously noted for American options: 

- American options are worth at least as much as European options:

$$0 ≤ C_{Eu} ≤ C_{Am}$$
and 
$$0 ≤ P_{Eu} ≤ P_{Am}$$

- American options are worth at least as much as their intrinsic value:

$$\max{0, S − K} ≤ C_{Am}$$
and 
$$\max{0, K − S} ≤ P_{Am}$$
(lower pricing bounds) because they can be exercised immediately

> - how we might consider modifying the binomial model?

The adjustment to price American options is:

A each node, set the American option price equal to the maximum of the “1-step European price” and the option’s intrinsic value:


- Recall we discretise the interval $[0, T]$ into $N + 1$ equally-spaced
dates ${t_0 , . . . , t_N }$ with $t_0 = 0, t_N = T$ and spacing $dt = \frac{T}{N}$

- At date $t_j$ there are $j + 1$ asset prices $S_{ij} = Su^i d^{j−1}$ for $i = 0, . . . , j$.

The (American and European) option payoffs at expiry are

$$C^{Am}_{iN} = \max \{ 0, S_{iN} - k \}$$
and

> - At point in time $j$ in the tree, 
> - Capital N in the above equation denoting you are in the final layer of the tree

- The “1-step European” option prices at node ij on the tree are

$$C^{Eu}_{ij} = e^{-rdt}\left[ qC^{Am}_{i+1, j+1} + (1-q)C_{i, j+1}^{Am}  \right]$$
$$P^{Eu}_{ij} = e^{-rdt}\left[ qP^{Am}_{i+1, j+1} + (1-q)P_{i, j+1}^{Am}  \right]$$

> - call price at a given node in the tree
>   - one period binomial model risk neutral price
>   - present value of the risk free rate, multiplied by the probability of the up step multiplied the price price of the option in the up step, plus (1-p) of the down step in the asset tree

- The call and put option intrinsic values at node  $ij$ are

$$C^{iv}_{ij} = \max \{ 0, S_{ij}-K \}$$
and
$$P^{iv}_{ij} = \max \{ 0, K - S_{ij} \}$$

Hence, the American option prices at node $ij$ are

$$C^{iv}_{ij} = \max \{C^{Eu}_{ij}, C^{iv}_{ij} \} $$

$$P^{iv}_{ij} = \max \{P^{Eu}_{ij}, P^{iv}_{ij} \} $$

> - In an exam, could probably only ask you to do a one-step

---
### Example

![alt text](assets\IMG172.PNG)

![alt text](assets\IMG173.PNG)

---

Let’s consider a continuous dividend yield $y$ (sorry for the notation).

- The European binomial model with a dividend yield is the same as without one except we set the risk-neutral probability to

$$q = \frac{e^{(r-y)dt}-d}{u-d}$$

