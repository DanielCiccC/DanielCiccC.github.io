# Lecture 9: Mortgages

> Mortgage Mathematics - IMPORTANT


### Objectives:

- Understand to legal and histrocial context of mortgages in Queensland and the role they play in real estate finance
- Understand the role of mortgages as part of collateralised debt obligations and how this influenced the GFC
- Be able to explain and apply the different types of mortgage repayment structures

## What is a mortgage?

- Term mortgage comes from old Norse French “mort” meaning death and “gage” referring to a “pledge.
- A mortgage is taken over a property as security for a loan. A mortgage is a contractual arrangement where one party (the mortgagor) provides property as security for a loan provided by the other party (the mortgagee). When the debt is repaid, the mortgage expires.
- The offer of property as a security becomes an interest in the land for the lender.  The land becomes encumbered by the mortgage – historically mortgagee held the physical Certificate of Title to effectively stop any sale without the debt being paid off.
- Like leases it creates both contractual rights (rights in personam) and property rights (rights in rem).

> - Taken out over a particular property
>   - Used as a form of security that is granted by somebody
> - Securitise a loan that has nothing to do with the security
>   - mortgagor just needs to have some sort of security
> - Offer property as security, mortgagor has interest in the land
>
> Historically, proof of title was handed over to mortgagee as security
>  - only stopped about 25 years ago - banks held a vault with property titles
>  - Title used to be handed over physically at the same of property - hence 'conveyancing' the property over to another party
>
> Not just a contractual right

### Overview of Mortgages in Queensland
- A mortgage is a legal agreement between a borrower and a lender in which the borrower 
pledges property as security for a loan.
- In Queensland, mortgages are governed by the Part 7 of the Property Law Act 1974
(currently a Property Law Bill 2023 is before parliament – will update but not fundamentally 
alter rules)
- A mortgagee (the lender) has the right to take possession of or sell the property if the 
borrower defaults on the loan.
- Mortgages must be registered on the title of the property to be enforceable against third 
parties. Otherwise just contractual remedies for lender against borrower.

### Registered Mortgages

- A registered mortgage is a legal interest in the property that is recognized by law and is 
registered on the property's title.
- A registered mortgage gives the mortgagee the right to take possession of or sell the property 
if the borrower defaults on the loan.
- If a mortgage is not registered, it may not be enforceable against third parties, and the 
mortgagee may not have the legal right to take possession of or sell the property in the event 
of default.
- It's important for both borrowers and lenders to ensure that a mortgage is properly registered 
on the title of the property in order to ensure that the rights and obligations under the 
mortgage are legally binding and enforceable.

> If you as a borrower don't pay the loan, lender has a right to take possession of the property
> - mortgagees can take possession of the property if you are doing something that destroys it's value
> - taking possession to everything - to rents maintenance, insurance, everything on the land, etc.
>
> If mortgagee can't enforce payment of rent (after the possession), e.g. if the mortgage is not registered.

### Equity of Redemption

- The equity of redemption is the borrower's right to redeem the property by paying the 
outstanding debt before the mortgagee exercises their power of sale.
- The equity of redemption is a fundamental principle of mortgages in Queensland.
- The mortgagee must provide the borrower with notice before exercising their power of sale.
- The borrower has the right to challenge the mortgagee's decision to exercise their power of 
sale in court.

> Can't destroy the equity of the property when exercising their power of sale


### Power of Sale
- The power of sale is the mortgagee’s right sell the property in the event of default.
- Mortgagee in Possession – can lead to a sale or can result in mortgagee operating the property.
- The mortgagee must strictly comply with certain requirements before exercising their power of sale, such as providing notice to the borrower – opportunity to remedy etc.
- If the sale of the property does not cover the outstanding debt, the borrower may still be liable for the remaining amount.
- If the sale generates more than the outstanding debt, the mortgagor will receive the difference (after mortgagee’s costs).

### Mortgagee in Possession

- If the rent received from taking possession of a property is more than the mortgage 
payments, the mortgagee may be able to keep the difference as income. However, the 
mortgagee must still comply with the terms of the mortgage and act in good faith towards the 
borrower.
- Under the Property Law Act 1974 in Queensland, if a mortgagee takes possession of a 
property and generates income from it, they must apply the income towards the following in 
the following order of priority:
1. Any expenses associated with managing the property, such as repairs, maintenance, and insurance.
2. The mortgage payments owed by the borrower.
3. Any other amounts owed by the borrower under the mortgage or related agreements.

> Have to maintain property and receive any surplus from rent, etc

## Current issues and trends

![alt text](assets\IMG72.PNG)

> Interest rates are low, but the amount you have to borrow vs disposable income is very high
> - More and more expensive to have a mortgage than it used to be

### Mortgages from an Investment Perspective
- Broadly, mortgages are divided into residential mortgages and commercial mortgages.
  
Differ in several respects:
  - Individual residential loans are much smaller amounts on average, but much more numerous than commercial loans
  - Residential owner-occupied properties generate no income, so the lender depends on the individual borrower’s income to service the loan, while commercial loans can be serviced by the income produced by the property securing the debt.
  - Resi borrowers are not financial or business professionals and are only in the market for a loan on occasion, commercial borrowers are typically commercial or financial entities staffed by professionals with much greater financial expertise.

- Commercial properties tend to be more unique, while single-family homes tend to be more 
homogenous
- Social and political concerns, and the resulting government involvement, are much greater 
regarding residential loans than commercial loans, including different statutory and common 
laws governing foreclosure and bankruptcy for residential versus commercial loans
- Residential mortgage business has become more of a “mass production” fairly standardised 
industry.
- Commercial mortgages remains more of a “custom shop” where individual loans are crafted 
and negotiated.

> legitimate investment tool
> - residential loans are small but lots of them
> - If borrowing sits within trend range
>
> Valuers are engaged to find LTV is adequate
> - Extent to which the government wants to play in this space will change investment in property
> - legislation changes rights of sale, can materialise into a riskier investment
>  - E.g. government makes it harder to evict you out of your house, riskier investment
>
> Bundling a bunch of mortgages together
>  - residential mortgages make sense, all pretty generic
>  - Commercial properties are a lot more difficult, loan terms can be a lot more different
>  - Bank to bank will be different

### Calculating Loan Payments and Balances
There are Four Basic Rules for calculating loan payments and balances:
- Rule 1: The interest owed in each period equals the applicable interest rate times the outstanding 
principal balance at the end of the previous period.

$$INT_{t} = (OLB_{t-1})_{rt}$$


- Rule 2:  The principal amortised (paid down) in each payment equals the total payment (net of 
expenses and penalties) minus the interest owed: 

$$AMORT_{t} = PMT_{t}-INT_{t}$$

- Rule 3: The outstanding principal balance after each payment equals the previous outstanding principal balance minus the principal paid down in the payment:

$$OLB_{t}=OLB_{t-1}-AMORT_{t}$$

- Rule 4:  The initial outstanding principal balance equals the initial contract principal specified in the 
loan agreement: 

$$OLB_{0} = L$$

> - How much you have to pay, how much you have to pay back at any period of time

![alt text](assets\IMG73.PNG)

> need to work out frequency of payments, frequency of payments, e.g.


### Applying the Rules to Design Loans
- There are a number of loan types which the Four Rules can be 
applied to:
- Interest-only loan
- Constant Amortization Mortgage (CAM)
- Graduated Payment Mortgage (GPM)
- Adjustable Rate Mortgage (ARM)


### 1. Interest Only Loan

$$PMT_{t} = INT_{t} = OLB_{t} \times i$$

or equivalently, $OLB_{t} = L, AMORT_{t} = 0$ for all $t$

- Oldest and most basic of loan payments.
- In interest only loan, no amortization of principal
  - Outstanding loan balance remains constant throughout the life of the loan
  - Entire original principal must be paid back to the borrower in a lump sum (balloon) at the loan’s maturity date.
  - Regular loan payments consist purely of interest
  - If interest rate is fixed, loan payments will remain constant

> consistent, every month and payment


- Normally, a relatively short term maturity 4 to 5 yrs, so best is used to finance property investments with correspondingly short holding periods (or re-finance during longer holding periods).
- Used extensively for taxation purposes.
- The repayment spike at the end of the loan confronts the borrower with the need to either refinance the loan or sell the property when the loan matures.
  - Can cause problems if either the property or the debt market is not favourable at that time.

- Classical payment pattern of long-term corporate and government bonds and is not unusual in commercial mortgages.
- Has advantage to the borrower of regular payments that are less than those of equivalent amortising loan.
- Because principal is not paid down, maximises the total dollar magnitude of interest paid over the lifetimes of the loan, compared to other amortizing loans.

> good for taxation purposes, all interest payments are tax deductable

![alt text](assets\IMG74.PNG)

### Interest Only Mortgages 
**Key Advantages**
- Low payments (compared to principal & interest)
- Payments are entirely tax deductible
- PMTs always the same (easy to budget/administer) for fixed rate loans.
- Payments do not vary with maturity.
- Very Simple, easy to understand loan

**Key Disadvantages**
- Big ‘balloon’ payment (refinancing risk amplified because term of loan is 
generally short)
- OLB never decreased (therefore Interest payments never decrease)
- Can have slightly higher interest rates than amortising loans
- Lack of principal pay down can increase default risk
- Builds equity slower than with amortising loan structures
- The predominant loan type for investment properties – commercial 
and residential.

> - interest payments never decrease
> - banks will make you pay slightly more
> 
> ![alt text](assets\IMG75.PNG)

### Constant-Amortisation Mortgage (CAM)

$$AMORT_{t} = L/N$$
- Simplest way to solve the problem of the repayment spike at the end of the interest-only mortgage is to pay down a constant amount of principal in each loan payment.
- Such loans used for a time in the 1930s when interest-only loans were causing havoc during the Great Depression and when persistent deflation resulted in declining rent and land values.
- Characterised by a declining payment pattern.  As the loan balance is reduced by a constant amount each period, the interest owed falls by a constant amount as well. 

> Paying the principle down, along with interest
> - pay back some of the principle, what of the payment equal interest?
> ![alt text](assets\IMG76.PNG)
> Every month your principle deducted is the same
> means that your payment is varied

- Payments on a CAM are computed by dividing the initial principal by the number of payments to compute the amortisation amount per period, and then applying rule 2 to compute the total payment due each period as the sum of the amortisation and the interest computed based on rule 1.
- Capital Sum (Principal paid back incrementally)

> ![alt text](assets\IMG77.PNG)
> ![alt text](assets\IMG78.PNG)

**Key Advantages**
- Results in a quicker reduction in the outstanding balance
  - Suits borrowers who dislike bearing debts
- Quicker recovery of interest for lenders
- Allows for tax shield at the beginning of the loan because of the 
higher amount of interest.

**Key Disadvantages**
- Difficult for borrowers to manage because this method requires larger payments at 
the onset of the loan 
  - Borrowers incomes that tend to increase over the years
  - High initial payments does not match the likely income generation of the property
- Change in payment contributions may make it difficult to manage budgets
- In an economy free of persistent deflation, declining payment pattern is undesirable.
  - From mortgage investors, CAM likely requires an inconvenient reinvestment of 
capital each period as the mortgage is amortised.
- Not widely used today

### Fully Amortising Mortgages 
- Fully amortising means the regular PMTs will fully repay the loan by the 
end of the term.
- Each payment comprises the interest accrued since the last PMT + a portion 
of the remaining principal balance.
- PMT is constant over loan term (at fixed i), but the proportion of the 
principal (PPMT) & interest (IPMT) components of PMT alter over time
- Loan terms of between 15 & 30 years common

EXAM - IMPORTANT
> consistent way of receiving funding from an amortising bank
>
> ![alt text](assets\IMG79.PNG)
>
> ![alt text](assets\IMG80.PNG)


### Fully Amortising Mortgages
**Key Advantages**
- Build equity faster (than interest only loan)
- No balloon Pmt (no refinancing stress if loan runs full term & reduced refinancing stress if doesn’t run full term)
- Longer loan term can reduce financial risk
- Can have slightly lower interest rates than interest only loans
- Principal pay down can decrease default risk over time.
- Low Pmts possible with long amortisation periods.
- If on a fixed rate, Pmts constant so easy to budget/administer.
- Flexibility allows trade-offs e.g. between Pmts & terms, etc

**Key Disadvantages**
- Higher payment than interest only, particularly shorter term loans, hence reduced cashflow
- Principle component of payment is not tax deductible

**Are the predominant loan type for owner occupier home loans.**

> Initial stages feel like you're treading water

### Adjustable Rate Mortgages (ARM)
- Another way to improve affordability for a borrower is to allow 
the contract interest rate in the loan to adjust periodically to 
changes in the interest rates prevailing in the debt market. 
- Reduces interest rate risk for the lender, making a lower interest 
rate possible.
- Interest rates applicable over the life of an ARM are likely to 
vary up an down over time

> Changes interest rate in your calculator
> - When you borrow money from the bank and it is variable

- Reduce the initial interest rates for long-term mortgages during times when a steeply upward-sloping yield curve is prevailing in the bond market.
  - Short-term bonds are priced with a lower yield than long term bonds
  - Tends to occur when inflation is expected to increase in the long term, or when 
short-term real interest rates are temporarily depressed due to stimulative government policy
- ARM may be a long term mortgage, it is like a chain of short-term fixed rate loans linked together because the interest rate can be adjusted at relatively short intervals.

> ![alt text](assets\IMG81.PNG)
>
> ![alt text](assets\IMG82.PNG)

## Mortgage Backed Securities

### Commercial Mortgage Backed Securities
- Commercial Mortgage Backed Securities (CMBS) refers to commercial mortgages that are pooled together and sold to investors.
- Process is known as securitisation 
- During 1990s and until 2008 CMBS provided new & efficient form of debt 
capital for real estate
- Improved liquidity and transparency of commercial real estate & 
integration into other capital markets

### CBMS
- CMBS are financial instruments (bonds) backed by pools of commercial mortgages
- CMBS securities provide claims to components of the cash flow coming from underlying mortgages (borrowers pay principal and interest)
- Mortgage loans on individual commercial properties originated by lenders in the primary 
market are pooled together 
- Pool of loans are transferred to a trust – issue and sell classes of bonds to investors.

> Pool together a bunch of mortgages, sell as an investment
> - Way a bank can get more capital, and provide more mortgages
> - Financial instrument, integrates real estate into capital markets
>
> Claim from the CMBS to cash flows
> - transferred to a trust, paid in interest
> - Have their own value and market, which may be completed disassociated with the underlying value of the assets

- Many Australian listed and unlisted property trusts raised debt in this form in the early and mid-2000s
- The CMBS were backed by mortgages over several properties of one trust.
- Provide institutions investors returns based on loan payments and payment of capital at maturity.
- Until 2007 CMBS with AAA Rating were the norm for raising debt at a lower cost than banks.

> Another indirect way of interacting with sector
> - Given really high credit ratings
> - Able to access debt at rates better than going to the bank for the underlying security

### Key Features of Mortgage Backed Securities
1. Securitisation: process of pooling mortgages 
2. Tranching: separation of securities into classes
3. Bond Credit Rating: the riskiness of an investment
4. Other: Loan maturity, waterfall (tiering of creditor payment 
priority)

### 1. Securitisation: The Principle
- Loans earn interest but..
  - Are illiquid (maturity mismatch, interest rate risk…)
- Securitisation: bundle loans to standardised sizes and risk and sell the claims:
  - Immediate cash-inflow for the bank
  - Bank provides the service of collecting and passing through the loan 
cash flows
  - Default risk (by large) with the buyer

> Lent the money and have interest payments coming back
> - Get the capital back

- Combining similar loans in a portfolio
- Creating credit-enhanced claims against the cashflows of this portfolio (waterfall creditor priority)
- Sell these claims to investors

![alt text](assets\IMG83.PNG)

![alt text](assets\IMG84.PNG)

![alt text](assets\IMG85.PNG)

### 2. Value Creation: Tranching
- Different classes of securities are known as tranches
- Each tranche is characterised by its priority of claim on the mortgage pool’s 
cash flows
- Bond rating agencies assign a credit quality rating to each bond class.
- AAA Rating – Highest-quality, low risk, investment grade 

- Two dimensions of cash flow claim priority:
  - Credit losses
  - Loan retirement (maturity)
- Credit losses: default risk in securities
- Loan Retirement/ Maturity: duration and interest rate risk

### 3. Bond Credit Rating
- Liquid public market in CMBS requirements:
  - Passive investors to feel confident in default risk regardless of their real 
estate knowledge
  - Otherwise investors would not place their capital or;
  - require such high yields securitisation would be unprofitable or 
uncompetitive
- Bond rating agencies provide a credit rating for CMBS securities

### Collateralised Debt Obligations
- Collateralized debt obligations (CDO’s) 
- Developed in the boom of 2006-07
- Lower rated CMBS were re-securitised into a second (or third) layer 
of pooling and tranching and securities issuance
- Proved disastrous in financial crisis of 2008-09

> - sub prime mortgages
> securitised together, given a lower risk rating
> - when they defaulted, it snowballed

### The Giant Pool of Money Review
- Global Pool of Money increased from $36 trillion to $70 trillion in short period of 
time (2000 – 2006)
- Led by emerging economies – China, India, Abu Dhabi, Saudi Arabia
- Alan Greenspan – not raising Fed rate
- New loans now available in the mortgage market:
  - Stated income, verified asset
  - Stated income, stated asset 
  - No income, no asset (NINA)

- Investors trust credit rating agencies:
  - Moody’s, Standard & Poor’s, Fitch
  - Rating agencies using incorrect data 
  - Assumed foreclosure rate of below 2% with worst-case scenario of 8% - 12%
  - Historical data now irrelevant because of new mortgage types
  - Foreclosure rate to go to 50%
- “Money good” investments created by pooling thousands of risky 
mortgages

### Global Financial Crisis 
- What is the source of the GFC?
  - Step One: The Boom years
  - Step Two: The Rotten Apple
  - Step Three: Debt Deflation

> Debt was easy to obtain
> - Collateralised their debts

### GFC Step 1: The Boom Years
- Securitisation took off
- Banks and ratings agencies profited form securitisation
- Homebuyers got easier access to loans (subprime)
- House prices increased substantially
- Low interest rates
  - Increase in adjustable rate mortgages
- Homeowners used increase collateral for more loans

### GFC Step 2: The Rotten Apple
- Homebuyers’ moral hazard 
  - 100% debt finance + walk away policy =  free game
  - If house prices increase you win
  - If house prices go down the bank loses
- Bank’s moral hazard
  - If loans are on the balance sheet the bank can lose
- Rating agencies moral hazard / blind eye (?)
  - Bank pay for the rating; have to keep them happy
  - Rising house prices ‘hide the defaults’
- MBS buyer blind eye / herd behaviour (?)
  - Portfolio managers “have” to join the high return /”low” risk party
  - If the party is busted they can claim: “everybody did it too”

### GFC Step 3: Debt Deflation
- Non-recourse loans
  - The bank can either have the house or what’s left on the mortgage -
not both
  - You can turn over the key and walk away free and clear
  - The bank cannot come after you to collect the rest of the money owed
- Say your house is underwater – you owe more on your mortgage than what your house is worth.. What would you do..?


### Is there another GFC coming?

- Years of cheap capital – central banks printing money and low cash rates
- War in Ukraine and Covid – supply side issues results in large i inflation
- US Fed (plus Reserve Bank of Australia and other central banks) increased cash rate (large comparative percentage rise over short period)
- Silicon Valley Bank bankruptcy – role of social media

> People collateralising their loans don't to their due diligence properly