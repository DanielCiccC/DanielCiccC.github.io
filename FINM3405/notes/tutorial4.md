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

An options intrinsic value is its payoff if it was able to be exercised immediately

- The option premium is almost always greater than the option's intrinsic value (IV) and we define time value as the difference between the two

Time value = premium - intrinsic value

### Question 2. What does it mean to exercise an option? Which party gets to choose whether they exercise an option?

The holder gets to choose whether to exercise the option, the writer is 'at their mercy'.
- Exercising a call option means the holder exercising their right to buy the underlying asst off the writer for $K$. Opposite for puts.

### Q4 What is the maximum profit an option writer can earn, and what is their potential loss? Why would you ever consider writing options?

- The most an option writer can earn is the premium received. Their loss is unlimited when writing a call, and limited to the $K$ minus the premium when writing puts.

**Lecturers answers**
- It is common to write covered calls in order to generate additional income on a portfolio
- It is also common to write covered puts in order to 'leg in' to buying stock for a cheaper price if you're exercised or simply earn the premium if you're not.

### Q5 - on iPad

### Q6 -  expect the Harvest CSI 300 CSI to go sideways
- The strategy in question is a covered call, also called a buy-write (buy the stock and write the calls)

- $m=10,000$ So you would write $50$ just out-of-the-money calls. If the market went sideways you would keep you premium and your portfolio, achieving your goal of generating additional income.
- If the market went down, you'd have the same outcome except of course your value of you portfolio is less. If the market goes up, you'll get exercised and have to sell your holding.

**1. What do I mean when I say “either side of the money”?**
- Pretty much close to at-the-money

**2. Which options are in-the-money? Which are out-of-the-money?**
- The last traded price of CBA was $S=128.11$ so calls with a strike less than this are in-the-money and with a strike greater are out-of-the-money. Puts are the opposite

**3. What is your profit if you took 10 just out-of-the-money calls and CBA closed at $135 in 7 days? What about at $125? What if you wrote the calls?What about for puts? Use the last traded prices. Plot profit diagrams.**

- Just out-out-the-money calls have a strike of K=130 and last trade premium price of $C=\$1.10$
- $m=100$ so 1 option contract represents a total exposure of $F=100 \cdot K = 100(130)=\$13,000AUD$
- If you took 10 options with will cost you $hCm = 10\cdot 1.10\cdot 100 = \$1,100$AUD
- If CBA closed at $S_{T} = \$135$ on expiry, your profit is

$$h(S_{T}-K)m-hCm = 10(135-130)100 - 1100 = \$3,900$$

### 4. What is the intrinsic and time values of the options close to at-the-money?

- Lets consider American options whose strike are 130 and 128
- Their last traded premium prices are 1.10 and 2.20 for 128


- $K=130$ is out of the money, it's intrinsic value is 0 
  - $\therefore$ time value = premium
- $K=128$ is in-the-money, $128.11-128 = 0.11$
  - Time value = $2.2-0.11 = 2.09$