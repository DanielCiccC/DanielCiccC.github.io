# FINM3405 Revision
# FRN and Interest Rate swaps

1. Floating rate notes (FRN) definition, concepts and pricing in preparation for fixed-for-floating interest rate swap pricing.
2. Fixed-for-floating interest rate swap definitions and concepts.
3. Calculating the net cashflows on each coupon or interest date.
4. The idea that a position in a fixed-for-floating interest rate swap can be replicated via positions in a FRN and a fixed coupon bond.
5. Interest rate swap pricing: calculating the fixed rate.
6. Hedging and speculating with interest rate swaps.

### Notation
- $F$ is the face value and $T$ is the maturity date in years.
- $t_i$ for $i = 1, . . . , N$ are the interest or coupon dates in years.
- $r_i$ for $i = 1, . . . , N$ are the reference rate’s spot rates for the time period $[0, t_i ]$, thus the reference rate’s yield curve.
  - $r_{i−1,i}$ for $i = 1, . . . , N$ are the implied forward rates for coupon period $[t_{i−1}, t_i ]$ embedded in the yield curve.
- $f_i$ is the floating rate for coupon period $[t_{i−1} , t_i ]$, which is known only at time $t_{i−1}$, the start of the coupon period.
- $C_i$ for $i = 1, . . . , N$ are the coupon payments for period $[t_{i−1}, t_i]$, calculated from $f_i$ at time $t_{i−1}$ , paid at time $t_i$ .
- $k$ is the fixed interest rate in the swap.
- $C = Fkd$ is the fixed coupon in the swap.


# 1. Definitions

## 1.1. Floating Rate Notes

A (forward looking) floating rate note (FRN) is a fixed interest security that promises to pay regular coupon payments which are calculated from a reference interest rate (such as Term SOFR, Euribor, etc) and also pay back the notional principal or face value at maturity.

### 1.1.1. Forward-Looking

By forward looking we mean that a given interest period’s coupon (or interest) payment, which is payable at the end of the interest period, is *calculated at the start of the interest period* (using the spot reference rate whose maturity date is the end of the interest period).

Backward looking means that the coupon is not only paid but also calculated at the end of the interest period based on “some kind of formula” involving the reference rate’s values or behaviour over the interest period.

## 1.2 Pricing

So the time $t_i$ coupon or interest payment $C_i$ is calculate at time $t_{i−1}$ as

$$C_i = F \cdot f_i \cdot d$$

where $d$ is the time in years between coupons (so $d = 1/4$ for quarterly, $d = 1/2$ for semiannual, etc) and the floating rate is usually given by

$$f_i = r + m$$

where $m$ is the margin (risk premium) over the spot reference rate $r$
covering the period $[t_{i−1}, t_i]$ once it’s known in the market at time $t_{i−1}$ .
- But for simplicity, we assume $m = 0$.

### 1.2.1 Certainty Equivalents
We use forward rate agreements (FRA) to calculate certain, risk-free cashflows $\bar{C}_i$ at each coupon date $t_i$ called the certainty equivalents of the coupons $C_i$

The above $\bar{C}_i$ is the time $t_i$ certainty equivalent cashflow

$$\bar{C}_i = Fr_{i-1,i}d$$

The value of the FRN is sum of the present values of these risk-free cashflows $\bar{C}_i$ discounted at the risk-free reference rates $r_i$, namely

$$V = \sum ^N _{i=1} \frac{\bar{C}_i}{1+r_i t_i} + \frac{F}{1+r_N T}$$


## 2. Interest Rate Swaps

### 2.1. Fixed-For-Floating 
Recall that a fixed-for-floating interest rate swap is a financial instrument that enables parties to “swap” or exchange their interest rate exposure or obligations, or their investment or lending income:

- $k$ is the fixed interest rate in the swap.
- $C = Fkd$ is the fixed coupon in the swap.

In this light there is two parties to a fixed-for-floating interest rate swap:
1. Receive fixed, pay floating : This party agrees to receive a fixed investment interest rate k and pay a floating borrowing interest interest. (Also called the pay floating, received fixed party.)
2. Pay fixed, receive floating : This party agrees to pay the fixed borrowing interest rate k and receive a floating investment interest rate. (Also called the receive floating, pay fixed party.)

## 2.5 Pricing a fixed-For-Floating Swap

Pricing a fixed-for-floating swap involves determining the theoretically correct or “fair” fixed rate $k$ in the swap.

**Note**:

The floating rates $f_i$ for $i = 1, . . . , N$ are already specified in the swap as being the reference rate (usually plus a risk premium or margin m), but each period’s floating rate $f_i$ is known only at the start $t_{i−1}$ of the coupon period $[t_{i−1}, t_i ]$, and not at time $t = 0$.


The cashflows of the *receive fixed, pay floating party* to an interest rate swap can be replicated via the following portfolio:
- Buying a fixed coupon bond with face value $F$, maturity date $T$, and coupon rate $k$ and thus fixed coupons $C = F × k × d$.
- Issuing a FRN with face value $F$, maturity date $T$, and floating coupons given by $C_i = F × f_i × d$ at time $t_i$ for $i = 1, . . . , N$.

So the value of a swap to the receive fixed, pay floating party must be the value of a fixed coupon bond minus the value of a FRN, both with face value $F$ and maturity date $T$, or else there’s an arbitrage opportunity.

$$\text{V = value of fixed rate coupon bond - value of FRN}$$

$$= \sum ^N _{i=1} \frac{C}{1+r_i t_i} - \frac{F}{1+r_NT}-F$$

- The second part of this (i.e. $F$) is the value of an FRN at time $t=0$

the fixed rate $k$ is set so that

$$k= \frac{1+\frac{1}{1+r_NT}}{d \sum ^N _{i=1} \frac{1}{1+r_it_i}}$$


## 2.6. Hedging and speculating with interest rate swaps

### 2.6.1 Speculating
To speculate with interest rate swaps:
- If you believe that the yield curve will shift up, then enter into an interest rate swap as the pay fixed, receive floating party.
- If you believe that the yield curve will shift down, then enter into an interest rate swap as the receive fixed, pay floating party.


### 2.6.2 Hedging

