# Lecture 10


### Floating rate notes (FRN)

- We start with FRN since they’re needed for swap pricing.

A (forward looking) floating rate note (FRN) is a fixed interest security that promises to pay regular coupon payments which are calculated from a reference interest rate (such as Term SOFR, Euribor, etc) and also pay back the notional principal or face value at maturity.
- FRN are important in their own right but we mostly cover them since they’re useful for pricing fixed-for-floating interest rate swaps.
- They’re used to price the hypothetical “floating leg” of the swap. But what do we mean by “forward looking”?

> - Need to price floating rate notes to price interest rate swaps
>   - Floating rate note, fixed interest security
> - What risk are you exposed to with a floating rate note?
>   - risk of interest rates rising and falling
>
> Forward looking


**Remark**

By forward looking we mean that a given interest period’s
coupon (or interest) payment, which is payable at the end of the
interest period, is calculated at the start of the interest period
(using the spot reference rate whose maturity date is the end of
the interest period). Backward looking means that the coupon
is not only paid but also calculated at the end of the interest
period based on “some kind of formula” involving the reference
rate’s values or behaviour over the interest period.
- They’re not overly complicated, and they’re quite common
and interesting, but we don’t cover backward looking FRN.


> - only know what the next coupon is going to be at the start of the coupon period
> - Is going to be calculated at the spot reference rate
> - In terms of how the coupon is calculated
>
> Backwards looking
> - calculate based on the preceding period
> - Backwards add a lot of extra sophistication, don't know in the actual interest period
> - Usually just estimate based on pervious few periods


---
### Example

![alt text](assets\IMG205.PNG)

> - Calculate the reference rate the covers the coupon period
> - Don't know the second month, have to wait till the end of the first month
>   - Can get an expected/average estimate
> - Calculate implied and forward BBSW rate

![alt text](assets\IMG206.PNG)

---

### Floating rate notes (FRN)

- $F$ is the face value and $T$ is the maturity date in years.
- $t_i$ for $i = 1, . . . , N$ are the interest or coupon dates in years.
- $r_i$ for $i = 1, . . . , N$ are the reference rate’s spot rates for the time period $[0, t i ]$, thus the reference rate’s yield curve.
- $r_{i−1,i}$ for $i = 1, . . . , N$ are the implied forward rates for coupon period $[t_{i−1}, t_i ]$ embedded in the yield curve.
- $f_i$ is the floating rate for coupon period $[t_{i−1} , t_i ]$, which is known only at time $t_{i−1}$, the start of the coupon period.
- $C_i$ for $i = 1, . . . , N$ are the coupon payments for period $[t_{i−1}, t_i]$, calculated from $f_i$ at time $t_{i−1}$ , paid at time $t_i$ .

> - $i$ starts at 1


So the time $t_i$ coupon or interest payment $C_i$ is calculate at time $t_{i−1}$ as

$$C_i = F \cdot f_i \cdot d$$

where d is the time in years between coupons (so d = 1/4 for quarterly, d = 1/2 for semiannual, etc) and the floating rate is usually given by

$$f_i = r + m$$

where $m$ is the margin (risk premium) over the spot reference rate $r$
covering the period $[t_{i−1}, t_i]$ once it’s known in the market at time $t_{i−1}$ .
- But for simplicity, we assume m = 0.


> margin should be basically equal to the credit default spread


### FRN valuation
Question: How do we price a FRN, given that we don’t know what the
floating rates $f_i$ and thus coupons $C_i$ will be for $i = 2, . . . , N$ until the
start $t_{i−1}$ of each coupon period $[t_{i−1}, t_i ]$?
Answer: We use forward rate agreements (FRA) to calculate certain, risk-free cashflows

$\bar{C}_i$ at each coupon date $t_i$ called the certainty equivalents of the coupons $C_i$, and then use arbitrage arguments to show that the value at time $t = 0$ of an FRN is

$$V = \sum ^N _{i=1} \frac{\bar{C}_i}{1+r_i t_i} + \frac{F}{1+r_N T}$$

> - Lock in interest rates with interest rate agreements
>   - At the end of each interest period
> - PV of risk free coupons discounted back at the risk free rate
>   - Assume our reference interest rate is risk free
>   - Face value discounted back

After doing this we’ll actually see that the value of an FRN is simply:

![alt text](assets\IMG207.PNG)

where $\hat{r}$ is the spot reference rate covering the time period $[s, t_i]$.

> - just the face value 
> - All we are going to prove is that the value is the PV of the next coupon + the face value
> - Face value represents all the future coupons
> - reference rate with hat, going to use the spot reference rate

![alt text](assets\IMG208.PNG)

### FRN valuation
We construct the certainty equivalent cashflows $\bar{C}_i$ at time $t_i$ as follows:

![alt text](assets\IMG209.PNG)


The above $\bar{C}_i$  is the time $t_i$ certainty equivalent cashflow, namely:

$$\bar{C}_i = Fr_{i-1,i}d$$

So if you held a FRN, from each coupon $C_i$ you could construct its risk-free certainty equivalent $\bar{C}_i$ via the process above.


- The value of the FRN is sum of the present values of these risk-free cashflows $\bar{C}_i$ discounted at the risk-free reference rates r i , namely

$$V = \sum ^N _{i=1} \frac{\bar{C}_i}{1+r_i t_i} + \frac{F}{1+r_N T}$$

- otherwise its an obvious arbitrage opportunity

If someone off ers you to an FRN for a price less than this theoretically correct market value, buy it and issue the same FRN in the market for its higher correct value. The coupons cancel out.

- You can do the case of the FRN priced greater than V.

> - if you if someone comes along to you and offers you a cheaper floating rate note, then you just buy it and you will receive these and you lock in the certainty equivalent cash flows 
> - go and issue a floating rate note in the market for a higher price, and you will pay the future cash flows.
> - The future cash flows all net each other out, and you receive an immediate upfront positive cash flow, which is an arbitrage.

What’s important to us is to show that

![alt text](assets\IMG210.PNG)

and we start with the case of time t = 0. We calculate that:

![alt text](assets\IMG211.PNG)

The above was for time t = 0, but for any other coupon date $t_i$, we can just view $t_i$ as the new “current date”, so we just have a “new” FRN with less time periods to maturity, and the above holds verbatim.

- When we’re at an intermediate date $s$ in $[t_{i−1}, t_i ]$, there is a known cashflow of $C_i$ at time $t_i$, and the FRN has value $V = F$ at time $t_i$, and thus could also be sold for $V = F$ at time $t_i$. So

$$V = \frac{C_i + F}{1 + \hat{r}(t_i -s)}$$

at time $s$ in coupon period $[t_{i−1}, t_{i}]$, where $\bar{r}$ is the spot reference
rate known at time $s$ for the period $[s, t_i ]$, so maturing at time $t_i$.

### Interest rate swaps
- We mostly covered FRN valuation since it’s used in swap pricing.
We now turn to fixed-for-floating interest rate swaps, in particular their pricing and using them for hedging and speculating.
- Recall that a fixed-for-floating interest rate swap is a financial instrument that enables parties to “swap” or exchange their interest rate exposure or obligations, or their investment or lending income:


Interest payments, exposure or obligations:
- A fixed interest borrower, or issuer of a fixed coupon bond, can turn
their fixed interest payments into variable interest payments, or their
fixed coupon bond into a FRN.
- A variable interest borrower, or issuer of a FRN, can turn their
variable interest payments into fixed interest payments, or their FRN
into a fixed coupon bond.

> - swap exposure or obligations
> - Issued a fixed coupon bond
>   - turn fix interest into floating coupon payments
> - Variable interest borrower, use a swap to turn your floating rate note into a fixed coupon bond
>
> - Other investor, imagine you hold a fixed coupon bond
> - Use a swap to imagine you are holding a floating rate note
> - If interest rates go up, receiver of a floating rate note will receive more


### Interest or lending income:
- A fixed interest investor, or holder of a fixed coupon bond, can turn
their fixed interest rate into a variable interest rate, or the fixed
coupon bond into a FRN.
- A variable interest investor, or holder of a FRN, can fix their interest
rate, or turn the FRN into a fixed coupon bond.
We will see below how this enables borrowers and lenders/investors to
hedge their interest rate risk, by which we basically mean their exposure
to roughly parallel shifts in the yield curve.

But, like CDS, interest rate swaps can also be traded as “standalone”
instruments purely for speculative (or other, such as arbitrage) purposes,
and that’s how we’ll treat them from now on:
-  We just view interest rate swaps as “just another derivative security”
that can be traded, and ignore any “underlying” exposure, cashflow
obligations or investment income stream of either counterparty.
And we’ll use the following additional notation:

> - Purely for speculative or arbitrage

- $k$ is the fixed interest rate in the swap.
- $C = Fkd$ is the fixed coupon in the swap.


In this light there is two parties to a fixed-for-floating interest rate swap:
1. Receive fixed, pay floating : This party agrees to receive a fixed investment interest rate k and pay a floating borrowing interest interest. (Also called the pay floating, received fixed party.)
2. Pay fixed, receive floating : This party agrees to pay the fixed borrowing interest rate k and receive a floating investment interest rate. (Also called the receive floating, pay fixed party.)

An example probably best illustrates the basic idea:

> - Receive fixed: receiving the fixed rate in the swap, and paying a floating rate

---
### Example

![alt text](assets\IMG212.PNG)

![alt text](assets\IMG213.PNG)

> - second part is the floating aspect of the swap
> - fix rate payer - floating rate receiver
>   - fixed coupon is larger than the floating coupon

---

**Remark**

Note that we don’t actually know what the other, later net
cashflows or payments in the swap will be because we don’t know
what the reference rate will be at the start of each coupon period,
until we arrive at that date. At time t = 0 we only know what the
first net cashflow will be (we’re covering forward looking swaps).

> - don't actually know what the net rate payments are going to be

### Pricing

Pricing a fixed-for-floating swap involves determining the theoretically
correct or “fair” fixed rate k in the swap.

**Remark**

The floating rates $f_i$ for $i = 1, . . . , N$ are already specified in the swap as being the reference rate (usually plus a risk premium or margin m), but each period’s floating rate $f_i$ is known only at the start $t_{i−1}$ of the coupon period $[t_{i−1}, t_i ]$, and not at time $t = 0$.

Question: How do we price a swap, given that we don’t know what the floating rates $f_i$ and hence coupons $C_i$ and net cashflows will be for dates $t_i$ for $i = 2, . . . , N,$ until the start $t_{i−1}$ of the coupon periods $[t_{i−1}, t_i ]$?


Answer: The cashflows of the say *receive fixed, pay floating party* to an interest rate swap can be replicated via the following portfolio:
- Buying a fixed coupon bond with face value F, maturity date T, and coupon rate k and thus fixed coupons $C = F × k × d$.
- Issuing a FRN with face value F, maturity date $T$, and floating coupons given by $C_i = F × f_i × d$ at time $t_i$ for $i = 1, . . . , N$.

So the value of a swap to the receive fixed, pay floating party must be the value of a fixed coupon bond minus the value of a FRN, both with face value $F$ and maturity date $T$, or else there’s an arbitrage opportunity.

> - definition of a swap
> - fixed rate receiver can be replicated by a long buying and issuing two bond positions (above)

---
### Example

![alt text](assets\IMG214.PNG)

---

Hence, the time $t = 0$ value $V$ of a fixed-for-floating interest rate swap
to the receive fixed, pay floating party (becoming a tongue-twister) is

![alt text](assets\IMG215.PNG)

where $C = Fkd$, and $\bar{C}_i = Fr_{i−1,i}d$ are the certainty equivalent cashflows.

But we previously showed that the value of a FRN at time $t = 0$ is simply $F$. So the value of an interest rate swap to the received fixed party is

![alt text](assets\IMG216.PNG)

An interest rate swap is priced via the usual principal:
The fixed rate $k$ in a fixed-for-floating interest rate swap is set so
that the swap has 0 value to either party at initiation, time $t = 0$.

> - A swap is priced so that there is 0 value to either party

As a result of the above usual principal, the fixed rate k is set so that

![alt text](assets\IMG217.PNG)

which, after recalling $C = Fkd$ and $\bar{C}_i = Fr_{i−1,i}d$, rearranges to give

![alt text](assets\IMG218.PNG)

> - EXAM QUESTION
---
### Example

![alt text](assets\IMG219.PNG)

![alt text](assets\IMG220.PNG)

![alt text](assets\IMG221.PNG)

---

### Speculation

> - Either going to be fixed rate receiver or payer
> - receiver, e.g. receiving a fixed rate amount
> - Actually receiving a lower fixed rate

![alt text](assets\IMG222.PNG)

![alt text](assets\IMG223.PNG)

> - in the swap, as the fixed rate receiver you have already contracted to receiver these amounts
> - Fixed coupon leg of the swap, discounted at the new yield curve
> - Exit out of the swap, you would have to pay 4 thousand

**Remark**

The other pay fixed, receive floating party could close out their profitable swap position with a swap dealer, thus realising their \$ 4,078.07 profit (net of fees and the swap dealer’s spread etc).

Consequently, to speculate with interest rate swaps:
- If you believe that the yield curve will shift up, then enter into an interest rate swap as the pay fixed, receive floating party.
- If you believe that the yield curve will shift down, then enter into an interest rate swap as the receive fixed, pay floating party.


---
### Hedging

![alt text](assets\IMG224.PNG)

> - issued a FRN, you are worried the yield curve will shift up
> - Hedge your exposure - fix your interest rate, so you are not exposed to that
> - Enter in as the fixed receiver

![alt text](assets\IMG225.PNG)

> - if interest rates did not stay the same, the cashflows would be those in the RHS of the table

![alt text](assets\IMG226.PNG)

> - still have the original fix rate locked in, but now have higher floating coupons
>   - that are received

**Remark**

You could imagine the following hedging scenarios:
- If you borrowed via FRN, we have the above example.
- If you borrowed via fixed coupon bonds, to hedge your exposure to falling interest rates you enter into a swap as the pay floating party.
- If you invested in FRN, to hedge your exposure to falling
interest rates you enter into a swap as the receive fixed party.
- If you invested in fixed coupon bonds, to hedge your exposure to increasing interest rates you enter into a swap as the receive floating party.
