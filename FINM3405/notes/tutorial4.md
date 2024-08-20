# Tutorial 4

### Q1 4. Why do options have premiums and which party pays it to which?

The payoff to the taker/holder of an option is non-negative, so this party can pretty much never lose money. Hence, the take need to compensate the writer in order to entice the writer to enter into an options contract.

### 5. What do the terms in-the-money, at-the-money and out-of-the-money mean?

- Calls: when $S_{T} > K$
- Put: when $S_{T} < K$

- An option is in-the-money (ITM) if the spot price of the underlying asset is currently "in the holders favour", meaning that it is greater than the strike price in the case of a call, and less than the strike price in the case of a put.

- An option is at-the-money (ATM) is the spot price of the underlying asset is equal to the strike price. 

- An option is out-of-the-money (OTM)  if the spot price is "not in the holder's favour" meaning $S < K$ for call and $S > K$ for puts


### 6. What is the diff erence between writing an option naked vs covered?

- Naked means writing them with "Nothing backing them". Contrasting this with covered options:

- A covered call -> involved writing call options over an asset that you already hold to a $FV$ of $F=hkm$ not exceeding the total value of the asset $V=QS$ of your asset holding.
  - So, if you were exercised in a call option and had to sell the underlying asset to the holder, you have the holding in the underlying asset to cover this.
- A covered put involves writing put options to $F=hkm$ no exceeding a total amount of cash you have on hand available to cover having to buy the underlying asset if you get exercise

- $h$: no. contracts
- $k$: strike price
- $m$: contract multiplier
- $S$: Spot price
- $Q$: The number of units of the asset we hold

### Q1 7. What is the intrinsic value and time value of an option?

An options intrinsic value 
