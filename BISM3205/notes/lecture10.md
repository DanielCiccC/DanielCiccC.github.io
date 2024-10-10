# Lecture 10
# PCI DSS – Payment Card Industry Data Security Standard

1. Customer pays with card
2. Payment is authenticated – merchant captures
customer’s account info and sends it to acquirer
3. Transaction is submitted – merchant acquirer
asks the card brand to get an authorization from 
the customer’s issuing bank
4. Authorization is requested – card brand submits 
the transaction to the issuer for authorization
5. Authorization response – issuing bank authorizes 
the transaction and routs the response back to the 
merchant
6. Merchant payment – issuing bank routes the 
payment to the merchant’s acquirer for deposit 
into the merchant’s account
*Payment Card Industry - Data Security Standard (PCI- DSS)

![alt text](assets\IMG157.PNG)

> - RHS, highly secured banking network
> - Card network is the organisation that gave you the credit card
> - Doing transactions over the itnernet

### E-business: The Online Transaction (1)

![alt text](assets\IMG158.PNG)

1. The CARD HOLDER initiates the ONLINE PURCHASE (e.g. via a ‘shopping cart’). The ACCOUNT DETAILS and PRODUCT DETAILS are passed VERY SECURELY to the MERCHANT (i.e. web site)
2. The MERCHANT then sends all these details very securely to the PAYMENT GATEWAY (the entrance to the FINANCIAL NETWORK)
3. The PAYMENT GATEWAY sends the secured transaction to the ACQUIRING BANK.
4. The ACQUIRING BANK sends the secured transaction to the CREDIT PROVIDER.
5. The CREDIT PROVIDER sends the secured transaction to the ISSUING BANK which performs debit/credit checks and issues APPROVAL/REJECTION

> - Just an overview, not how it is implemented
> - Software uses an API - contacts the gateway
> - check the card network as to whether the transaction should succeed

### E-business: The Online Transaction (2)

![alt text](assets\IMG159.PNG)

- The ISSUING BANK – sends back a response to CREDIT PROVIIDER, and then to the ACQUIRING BANK with a response 
code (approved/denied). Response code also defines the reason for failure (e.g. insufficient funds).
- The ISSUING BANK holds an authorization associated with that merchant and consumer for the approved amount
- ACQUIRING BANK forwards the authorization response to the PAYMENT GATEWAY, which forwards it to the 
BUSINESS/MERCHANT - this is known as the Authorization or “Auth”. Entire process typically takes 1 – 3 seconds
- MERCHANT then fulfils the order. The process is repeated but this time to “Clear” the authorization by consummating the 
transaction.
- The MERCHANT submits all approved transactions in a “batch” to their ACQUIRING BANK.
- The entire process from authorization to settlement to funding typically takes 3 days.

> - Yellow arrow back
>   - Discuss in more detail later

![alt text](assets\IMG160.PNG)

> - Red box is not in gateway, and prone to hacking

### Merchant Account Fees
- Authorization Fee
  - Really an ‘authorization request fee – is charged each time a transaction is sent to the card  -issuing bank to be authorized – applies 
regardless of whether the request is approved 
  - NOT the same as Transaction fee
- Transaction Fee
  - Is charged when you accept your authorization – only applies to an authorization that is accepted without error
- Statement Fee
  - Monthly fee associated with the monthly statement that is sent to the merchant at the end of each month processing cycle
- Monthly Minimum Fee
  - To ensure that merchants pay a minimum amount in fees each month to cover costs from the provider to maintain the account
- Batch Fee
  - AKA a batch header fee, when the merchant sends their completed transactions for the day to their acquiring bank for payment – 
important to close a batch every 24 hours or a higher rate is assessed by Visa / MasterCard / Discover
- Customer Service Fee
  - AKA a maintenance fee, merchant support fee, customer support fee, service fee
- Annual Fee
  - Levied by some providers – levied quarterly in most cases
- Early Termination Fee
  - If the merchant ends the contract before the end of the contract term

> - Authorisation fee, whether is bounces or not
>   - Business has to pay a lot of money
> - Marchant sometimes charges, which you don't if you pay with cash
> - Hidden fees if using credit cards

### Merchant Account Fees (Continued)
Chargeback Fee
- Exists for consumer protection
- Originated in U.S. when consumers were afforded ‘reversal rights’ in legislation – now extended globally.
- A consumer initiates a chargeback – contacts issuing bank and files a substantiated complaint regarding one or 
more debit items on statement
- Reversal of funds aims to:
- Provide incentive to merchants for quality products, helpful customer service, and timely refunds as appropriate
- Provide a means to counter unauthorized transfers due to identity theft.
- Chargeback rules should always be available publicly for consumers
- Chargeback is the largest risk that is presented to banks and providers – not to be confused with a refund
- In Visa, Discover, and MasterCard rules, the merchant’s processing bank is 100% responsible for all the transactions that 
the merchant performs. Leaves the provider open to large potential losses if the merchant operates in an illegal or risky 
manner
- Providers pass this cost on to the merchant – if the merchant can pay
- If a chargeback occurs, merchant may be assessed a fee by their acquiring bank
- Currently both Visa and MasterCard require all merchants to maintain no more  than 1% of dollar volume processed to be 
chargebacks – if above: (high) fines  to the merchant’s processing bank – ultimately passed onto merchant

> - Good for business if buying online
>   - is credit card secure
>   - Afraid on new system
> - Government instituted a rule, if you were charged and didn't receive the good, the merchant has to give you your money back


### PCI DSS – Overview #1

- Rationale: An information security standard – targeting merchants and service provides – protects  
credit/debit card data during storage, transmission, processing – not aimed directly at customers
- Origins:
  - 2001 – Visa mandated adoption of CISP (a security program) – 12 security requirements
  - Other brands developed their own:
    - American Express – Data Security Operating Policies (DSOP)
    - Discover – Information Security Compliance (DISC)
    - MasterCard – Site Data Protection Program (SDP)
    - JCP – Data Security Program (DSP)
  - 2004 – Visa & MasterCard merged their security programs into a single standard – PCI DSS.
  - 2006 – Visa, MasterCard, Am Express, Discover Financial Services & JCB International formed the 
PCI Security Standards Council to manage the evolution of the  PCI DSS. 
  - 2022 – most recent version PCI-DSS 4.0
- The PCI-DSS is not law and compliance enforcement and non-compliance penalties are set by an individual 
brand through contractual penalties or sanctions. E.g. Visa & MasterCard transactions are enforced by the 
merchant’s acquirer. American Express deals directly with its merchants for compliance.

> - Council to manage the evolution of this standard
>   - New hacking methods, e.g.
> - supported by credit card companies, to be PCI-DSS compliant


Capstone: The PCI-DSS forms a capstone standard:
- PCI-DSS is the top-level standard.
- PCI PA-DSS (Payment Application DSS) is for software developers/integrators of applications that store, process or transmit 
cardholder data as part of the authorization of settlement.
- PCI PTS (PIN Transaction Security) applies to manufacturers of personal identification number (PIN) entry terminals used for 
payment card financial transactions.
- PCI Point-to-Point Encryption Standard (P2PE). As the payment card is swiped through a merchant’s card reading device 
(the point of interaction (POI) device), the data is immediately encrypted. The encrypted data is then sent immediately to the 
payment processor (i.e. the banking network). The keys for encryption/decryption are never available to the merchant 
making card data entirely invisible to the retailer.
- 2 other standards:
  - PCI Card Production Logical Security Requirements and Physical Security Requirements (card manufacturing, chip personalization, PIN distribution, etc.
  - PCI Token Service Provider Security Requirements

> - Make EFTPOS machines
>   - terminals have to be made to a given standard
>   - Certain things you can/can't store

![alt text](assets\IMG161.PNG)


### PCI DSS – Overview #3

• High level overview
• PCI DSS applies to all entities involved in payment card processing – including merchants, processors, 
acquirers, issuers, and service providers. PCI DSS applies to all other entities that store, process or transmit 
cardholder data (CHD) and/or sensitive authentication data (SAD).

> - Create a separate segment for PCI DSS
> - database for card holders, etc.
> - want an IDS if something goes past, alarms will be raised straight away

![alt text](assets\IMG162.PNG)

### PCI DSS – Overview #4

![alt text](assets\IMG163.PNG)

Cardholder data and sensitive authentication data
- PCI DSS goal – to protect cardholder data and sensitive authentication data wherever it is processed, stored or transmitted.
- PAN – the primary account number printed on the front of the card
- Merchants, service providers, and other entities involved in payment card  processing must never store sensitive
authentication data after authorization. This includes:
  - The 3 or 4 digit security code printed on the front or back of the card
  - The data stored on the card’s magnetic stripe or chip (the “Full Track Data”)
  - The personal identification numbers (PIN) entered by the cardholder

> - must never store sensitive authentication data

### PCI DSS – Overview #5

Cardholder data and sensitive authentication data are defined as follows:

![alt text](assets\IMG164.PNG)

• The primary account number (PAN) is the defining factor for cardholder data. If cardholder name, service code, 
and/or expiration date are stored, processed or transmitted with the PAN, or are otherwise present in the 
cardholder data environment (CDE), they must be protected in accordance with applicable PCI DSS 
requirements.
• Organizations that outsource their CDE or payment operations to third parties are responsible for ensuring that 
the account data is protected by the third party as per the applicable PCI DSS requirements
• Cardholder data environment is that vital area of the business hardware, software, network links and people 
that are involved in the processing, storage or transmission of cardholder data.

> - Two different types of data, treated differently

### PCI DSS – Overview #6

![alt text](assets\IMG165.PNG)

> - None of the sensitive data can be stored
> - Even after the pin number worked

### PCI DSS – Cardholder Data Environment

(p.10 PCI DSS v3.2.1)
The PCI DSS security requirements apply to all system components included in or connected to the cardholder 
data environment. The cardholder data environment (CDE) is comprised of people, processes and technologies 
that store, process, or transmit cardholder data or sensitive authentication data. “System components” include 
network devices, servers, computing devices, and applications. Examples of system components include but are 
not limited to the following:
• Systems that provide security services (for example, authentication servers), facilitate segmentation (for 
example, internal firewalls), or may impact the security of (for example, name resolution or web redirection 
servers) the CDE.
• Virtualization components such as virtual machines, virtual switches/routers, virtual appliances, virtual 
applications/desktops, and hypervisors (Beyond our scope)
• Network components including but not limited to firewalls, switches, routers, wireless  access points, 
network appliances, and other security appliances.
• Server types including but not limited to web, application, database, authentication, mail, proxy, Network 
Time Protocol (NTP), and Domain Name System (DNS).
• Applications including all purchased and custom applications, including internal and external (for example, 
Internet) applications.
• Any other component or device located within or connected to the CDE.


> - Network segment in computer architecture
> - Must be checked by an auditor and approved


Network segmentation of, or isolating (segmenting), the cardholder data environment from the remainder of an entity’s 
network is not a PCI DSS requirement. However, it is strongly recommended as a method that may reduce:
• The scope of the PCI DSS assessment
• The cost of the PCI DSS assessment
• The cost and difficulty of implementing and maintaining PCI DSS controls
• The risk to an organization (reduced by consolidating cardholder data into fewer, more controlled locations)
Without adequate network segmentation (sometimes called a "flat network") the entire network is in scope of 
the PCI DSS assessment

> - Scope is reduced by making the segment small
> - Less costly for the assessment
> Difficult to implement the PC's ideas as over a wider network

### PCI DSS – CDE Scope - Network Segmentation vs “Flat Network”

![alt text](assets\IMG166.PNG)

> - Even if you have an N DS in there, that's
not recommended because somebody coming from the Internet can go
straight into your card holder environment.
And Wi Fi Access Point is not screened off with,
uh, a, uh, firewall.


### PCI DSS – a ‘typical’ scoping exercise

![alt text](assets\IMG167.PNG)

> - Software and hardware device is implemented
> - Go through the whole process and see if it is still secure

### PCI DSS – E-commerce implementations
#### (PCI SSC reference: “best_practices-securing_ecommerce.pdf”)

Payment Service Provider (PSP): A PSP offers a service that directly facilitates e-commerce 
transactions online via its relationship with acquiring member banks of  payment card brands. This 
category includes online payment processors, payment “gateway” service providers, virtual terminal 
services, and certain e-wallet or prepaid services that also process credit card payment for non-account 
holders at the point of sale.



**Common e-commerce implementations:**
1. Wholly outsourced e-commerce implementations.
2. Shared-management (merchant & PSP)
  - URL redirection to a PSP
  - An Inline Frame (or “iFrame” – embedding a payment form hosted by a third party within the 
merchant’s web page(s)
1. Merchant-managed e-commerce implementation (commercial shopping cart/payment 
application fully managed by the merchant)

> - Payment page, everyone goes somewhere else
> - the only thing you need coming back, is the information saying the money has been taken out of the account
> - Shared management
> - moving between sites, not a nice experience for the user
>   - use an iframe to display the content of another website inside main page

### PCI DSS – (1) Wholly outsourced e-commerce solutions 
- Many e-commerce solutions exist that provide most or the entire merchant’s online shopping 
functionality and experience. These solutions provide more than just transaction processing 
capability, often including customer-facing features such as product search, cart capability, checkout, 
and account  management; and back-office features such as product management, customer 
relationship management, order management, and appearance customizations.
- A hosted shopping cart is an e-commerce system that is hosted entirely on the service provider’s 
technological infrastructure. The e-commerce is not seamlessly integrated into the merchant’s 
website and the consumer is often directed off-site to select product and complete checkout.

**MERCHANT IMPACT**: The use of such a solution can alleviate many but not all of the merchant’s PCI 
DSS responsibilities. All merchants have a responsibility to implement policies and procedures that 
govern safe handling of cardholder data even if they never expect to encounter credit cards. Furthermore, 
it is the  responsibility of the merchant to vet the service provider and monitor its compliance to PCI DSS. 
Number of questions under PCI-DSS: 22.

### PCI DSS – (2) URL redirected e-commerce solutions
#### (PCI SSC reference: “best_practices-securing_ecommerce.pdf” – page 19)

> - page 19 in the handout, explains in more detail


In the URL redirection model, the cardholder is redirected from the merchant’s website to a third-party 
page. The cardholder then enters their account data into a payment page hosted by the third-party 
payment service provider (PSP). That is, customers of the merchant are sent to a PSP’s web pages. This is 
generally noticeable to the customer as the merchant’s website URL— e.g., http://www.merchant.example.com — changes to that of the PSP—e.g., https://www.psp.example.com


MERCHANT IMPACT: As account data is not collected, stored, processed, or transmitted by the 
merchant’s system, fewer systems need security controls - used by small and medium business 
organizations with lower-than-average cardholder data volume.
This e-commerce option provides an easier way for merchants to provide security for cardholder data, as 
most of the cardholder data security is performed by the PSP. It is strongly recommended that a merchant 
ensure the PSP is validated as a PCI DSS compliant service provider. Number of questions under PCI-
DSS - as few  as: 22
Let’s conceptualize this ‘redirection’ strategy

### PCI DSS – (2a) URL redirected e-commerce solutions

![alt text](assets\IMG168.PNG)


1. Merchant website sends a redirect command to the customer’s browser.
2. The customer’s browser then requests a payment form from the PSP.
3. The PSP creates the payment form and sends to the customer’s browser.
4. The customer’s browser displays the PSP’s payment form.
5. The customer enters account data and sends to the PSP.
6. The PSP receives the account data and sends it to the payment system for authorization – PSP sends the result (‘approved’ or otherwise) to the merchant – merchant advises customer.

> - Difference between 2a and 2b, is the link

### PCI DSS – (3) Merchant managed e-commerce implementation
#### (PCI SSC reference: “best_practices-securing_ecommerce.pdf” – page 17 – 19 inclusive)


This approach is via an Application Programming Interface (API) – it principally for ‘big-business’. In this context, an 
application-programming interface (API) is a method of system-to-system data transmission in which the merchant 
principally controls the progress of the payment transaction.
Customer cardholder data is sent from the customer browser back to the merchant website before being sent to the 
PSP. The payment page and form are hosted and supplied by the merchant website with all cardholder data 
processed by the merchant web server (and possibly other system components) before being sent to the PSP.
PCI DSS – (3) Merchant managed e-commerce implementation
28 (PCI SSC reference: “best_practices-securing_ecommerce.pdf” – page 17 – 19 inclusive)


MERCHANT IMPACT:
This architecture carries a high risk for merchants as their systems will receive and transmit, and may also store and 
process, cardholder data.
Hackers target websites using this payment method because there is a greater chance of larger amounts of valuable 
cardholder data being available, and the attack can be easier due to varying levels of security controls among merchants.
Due to the higher risk of compromise to merchant systems, the level of security responsibly for the merchant is high. 
Number of questions under PCI-DSS - approximately: 250
Let’s conceptualize this ‘API’ strategy

### PCI DSS – (3) Merchant managed e-commerce implementation

![alt text](assets\IMG169.PNG)

1. Merchant creates payment page.
2. Customer’s browser displays the payment form.
3. The customer enters cardholder data into the payment form and the data is sent to merchant web server.
4. The merchant web server transmits cardholder data to the PSP.
5. The PSP receives cardholder data and sends it to the payment system for authorization.

![alt text](assets\IMG170.PNG)

> - similar to other diagram, top, middle and bottom floor

### The Cardholder Data Environment
Any part of an organisation or merchant where its people, processes, and technologies store, process, or transmit payment card data, will be in scope for PCI DSS.  This data will be classed as part of their Cardholder Data Environment (CDE).

As most data breaches involve a compromise of the CDE, PCI DSS requirements require a wide variety of 
security controls to be maintained to help protect this data.

In summary, the CDE consists of:
- All system components that store, process, or transmit Cardholder Data (CHD) or Sensitive Authentication Data (SAD).
- Any component that directly connects to CHD systems.
- Any component that supports CHD systems (such as anti-virus, authentication servers).

Clearly, PCI DSS auditing costs and data breach risk are both lowered by reducing the CDE to its bare minimum