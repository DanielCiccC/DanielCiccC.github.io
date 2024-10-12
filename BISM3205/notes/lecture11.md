# Lecture 11
# Blockchain and cryptocurrencies

![alt text](assets\IMG171.PNG)

> - central ledger
> - Bank maintains a central ledger
> - LHS, have a blockchain, no one is keeping a central record of anything

### What is a Blockchain?

A  digital  database  containing  information  (such  as  records  of  financial transactions) that can be simultaneously used and shared within a large decentralized, publicly accessible network. also : the technology used to create such a database.


A blockchain is a digital record of transactions. The name comes from its structure, in which individual records, called blocks, are linked together in  a  single  list,  called  a  chain.  Blockchains  are  used  for  recording transactions  made  with  cryptocurrencies,  such  as  Bitcoin,  and  have many other applications.

> - Webster definition

### Stuart Haber Co-Inventor of Blockchain
#### Bitcoin: A Peer-to-Peer Electronic Cash System

Abstract. A purely peer-to-peer version of electronic cash would allow 
online payments to be sent directly from one party to another without 
going through a financial institution. Digital signatures provide part of 
the solution, but the main benefits are lost if a trusted third party is still 
required to prevent double-spending. We propose a solution to the 
double-spending problem using a peer-to-peer network. The network 
timestamps transactions by hashing them into an ongoing chain of hash-
based proof-of-work, forming a record that cannot be changed without 
redoing the proof-of-work. The longest chain not only serves as proof of 
the sequence of events witnessed, but proof that it came from the largest 
pool of CPU power. As long as a majority of CPU power is controlled by 
nodes that are not cooperating to attack the network, they'll generate the 
longest chain and outpace attackers. The network itself requires minimal 
structure. Messages are broadcast on a best effort basis, and nodes can 
leave and rejoin the network at will, accepting the longest proof-of-work 
chain as proof of what happened while they were gone.

![alt text](assets\IMG172.PNG)

> - Add new transactions, but can't reverse them
> - all the data is open in the blockchain
> - encrypted data is available to anybody in the blockchain
> - Blockchains have to be mined, takes time
>   - SQL database, blockchains take multiple minutes


![alt text](assets\IMG173.PNG)


> - each computer contains a copy of the ledger
> - decentralised technology
> - enhanced security
> - agreement between all the nodes
> - can settle things faster - moving bitcoin overseas, exchanged, e.g.


### Double spend problem

Ann has $100 and she wants to buy a lamp and a table.
They each cost $100, so she should only be able to buy one item.
No problem in day-to-day transaction since goods and money
are exchanged together.

In case of distributed systems Alice broadcasts the transaction 
on the network so that every node on the network is made 
aware that “Alice has used up $100 to buy a lamp”.


> - No double spending possible under traditional system
> - with a distributed system, a little bit different
>   - Have to publicize you have purchased, latency between nodes
>   - nodes will find out about purchase/payment
> - fraud may also say you have bought something else

### Trust the data
“The truth isn’t a thing of fact or reason. It is simply what everyone agrees on.”
> Gregory Maguire, Wicked: The Life and Times of the Wicked Witch of the West


### Two General's Problem
- not the same as byzantines generals' problem
  - used in distributed system, fault tolerance and blockchain

- Inconsistent state between two machines
  - TCP uses a four way handshake to terminate a connection

- cost vs speed
  - Practical ways to mitigate risk of two generals problem


### Proof of work

Cryptography Mailing List
Bitcoin P2P e-cash paper
2008-11-13 22:56:55 UTC
James A. Donald wrote:
> It is not sufficient that everyone knows X. We also
> need everyone to know that everyone knows X, and that
> everyone knows that everyone knows that everyone knows X
> - which, as in the Byzantine Generals problem, is the
> classic hard problem of distributed data processing.
https://satoshi.nakamotoinstitute.org/emails/cryptography/11/

Proof of Work like proposed by Satoshi doesn't solve the Two 
Generals Problem or the more generic Byzantine Generals Problem. 
It's a probabilistic solution to the Byzantine Generals Problem, 
which means the confidence that a consensus is reached is growing 
with every block added to the chain, but it never reaches 100%.
https://ethereum.stackexchange.com/questions/40213/how-is-the-two-generals-
problem-solved-with-proof-of-work

> - Satoshi implemented a way to implement the two general's problem using a probabilistic solution 

![alt text](assets\IMG174.PNG)

> - independent of the length, always get 256 hash

### Hashing vs Encryption

![alt text](assets\IMG175.PNG)


### Merkle Trees

Merkle trees are named after Ralph Merkle, who 
proposed them in a 1987 paper titled "A Digital 
Signature Based on a Conventional Encryption 
Function." Merkle also invented cryptographic 
hashing.

In order to verify the inclusion of data [K], in the 
merkle tree root, we use a one way function to 
hash [K] to obtain H(K).
In order to validate the inclusivity of K, K doesn’t 
have to be revealed, similarly the hash of data L 
can be revealed without any implicit security 
repercussions and so on.

![alt text](assets\IMG176.PNG)

> - Merkle trees are implemented in blockchain
> - hash each item of data - whole thing is called the merkle tree
> - Merkle root at the top
> - Item and hash it
>   - K 

- H(K) when hashed with the hash of the unknown dataset L, yields H(KL)
- H(KL) hashed with H(IJ) leads to H(IJKL)
- H(IJKL) hashed with H(MNOP) leads to H(IJKLMNOP)
- H(IJKLMNOP) when hashed with H(ABCDEFGH) yields H(ABCDEFHGIJKLMNOP) - which happens to be our publically available merkle root

> - change any one single data value, in any leaf node, the hash will be different
> - contains the hashes of all the data
> - anything changes, the root will be different
> - Nothing changes without you knowing about it

### The golden nounce

A nonce (“number used once”) is a 32-bit (4-byte) unsigned integer (0 to 2^32-1 = 4,294,967,295) 

> - positive whole number from 0 to 4 billion

![alt text](assets\IMG177.PNG)

> - Head has certain elements
> - change the block data to create the new hash 
> - change the nounce until the hashed number begins with 32 zeros
> - keep on changed until you find a hash with 32 leading 0's
> - You have 'mined' this block
> - simple calculation that proves to other computers that the block has been mined
>   - Is taken into blockchain
> - Every two weeks, the number of zeros is updated to make it easy or more difficult to mine the hash
> - Time to mine the block should always be around 10 mins
> - A block is full when it has reach 1MB
>   - thousands of transactions in the block
> - Computers trying to mine the block get bitcoin as a reward
>
> - number has to be 'smaller than' - not necessary num of zeros

### Try it yourself

Use the website https://passwordsgenerator.net/sha256-hash-generator/ to create a SHA256 hash that has
4 zeroes at the beginning for the following block: "Hello, Cryptos!" by inserting a nonce before the text inside the block.

So, in different words, find a number that, followed by the text "Hello, Cryptos!" results in a hash that starts with "0000"

![alt text](assets\IMG178.PNG)

Now imagine doing this with 32 leading zeros!
That's why it's sometimes referred to as a "mathematical puzzle" and
this is The Proof of Work!


### Proof Of Work

The essence of the proof of work consensus mechanism is to provide evidence that the majority of nodes agree and do not lie.
A proof of work verification is difficult, costly, and time-consuming to create, but easy to verify. Bitcoin 
is secure because it is computationally infeasible to attack the network. Requiring Proof of Work for participation is central to this property. Hence Bitcoin relies on computational work on cryptographic challenges as the basis for trust.

![alt text](assets\IMG179.PNG)

### Increase of Difficulty over Time

CPU (central processing unit)
GPU (graphics processor)
FPGA (Field Programmable Gate Arrays)
ASIC (specialized hardware)

> - ASIC, specialised hardware to create 256-bit hashes
> - Have different chip sizes


### ASIC vs GPU miners

![alt text](assets\IMG180.PNG)

### Why you can't cheat a bitcoin

![alt text](assets\IMG181.PNG)

> - you would have to mine the chains before everyone else

### What is the reward?

The winning miner claims a block reward by adding it as a first transaction on the block. At inception, each bitcoin block reward was worth 50 BTC. The block reward is halved after the discovery of every 210,000 blocks, which takes around four years to complete. As of February 2019, one block reward was worth 12.5 BTC. 

In November of 2019, the price of Bitcoin was about $9,300 per bitcoin, which means you'd earn
12.5BTC * $9,300/BTC = $116,250 for completing a block.
In May 2020, the number of bitcoins (BTC) entering circulation every 10 minutes dropped by half again from 12.5 to 6.25. 

The next halving will likely occur in 2024.
The maximum and total amount of bitcoins that can ever exist is 21 million.
There are 2,512,225.0 bitcoins left to be mined.

When all 21 million bitcoins are mined, there won't be a block reward to pay to miners.
When a Bitcoin user sends a BTC transaction, a small fee is attached. These fees go to miners and this is what will be used to pay miners instead of the block reward. 

> - Still continue with bitcoin mining, a transaction charged for any bitcoin transaction
> - This will become the reward for the miners


### CSIRO IT contractor spared jail for mining Monero on supercomputer


Intensive correction order imposed for 15 months.
A former CSIRO IT contractor has escaped jail time for using the country’s peak science and research organisation’s supercomputer to mine cryptocurrency.
Jonathon Khoo was sentenced to a 15-month intensive correction order at Sydney’s Downing Centre Local Court on Friday after pleading guilty to the 
charges.
Khoo was charged by the Australian Federal Police in May 2019 for modifying the computer systems of CSIRO without authorisation to access the 
processing power.
The charges included unauthorised modification of data to cause impairment and unauthorised modification of restricted data. Magistrate Erin Kennedy on 
Friday said Khoo had installed and run 2903 command scripts into CSIRO’s two high performance computers (HPC) and the Claymore Dual Miner software.
In doing so, Khoo generated $9,422 worth of cryptocurrency mining proceeds in the form of Ethereum and Monero.
While there was no “impairment to the CSIROs” operations, Kennedy said the use of the systems for period of just over a month in duration reduced the 
performance of the HPC. She said the HPC was also used by the Royal Australian Navy and Victor Chang Cardiac Research Institute.
CSIRO put the total cost of the HPCs reduced capacity at $76,668, including hardware and software.
Kennedy described the offence as "reckless" with "some level of planning", but acknowledged Khoo's remorse. She also noted that Khoo had admitted his 
guilt to police almost immediately after a search warrant was executed in 2019.
Khoo was handed a 15-month intensive correction order - a custodial sentence served in the community - with 300 hours of community service.
By Justin Hendry
Sep 18 2020 1:15PM 

## Physical Bitcoins?

Mike Caldwell and his Casascius coin. Caldwell 
started minting his coins a couple of years ago, 
but late last year he was banned from selling 
pre-funded coins.

The US Financial Crimes Enforcement Network 
(FinCEN) classified his activities as ‘money 
transmitting’ and Caldwell was forced to start 
selling empty coins. Sales resumed earlier this 
year and Casascius is currently listing three 
coins, along with a gold-plated savings bar. 
However, none of them are priced and it is 
unclear whether or not Casascius simply ran 
out of stock or stopped selling them directly 
altogether.

In addition to these silver, brass and gold-plated 
products, Casascius also sells aluminium promo 
coins. A bag of 500 costs 0.39 BTC.


### Some additional Facts
- Bitcoin’s blockchain began in January 2009, when the mysterious Satoshi Nakamoto mined the first block of 
bitcoins (known as the “genesis block”). 

- Currently, Bitcoin has the capacity to handle between 4-7 transactions per second (tps), which pales in 
comparison to systems like VISA and Paypal. VISA can handle on average around 1,700 tps and PayPal an 
average of 193 tps.

- Currently, each block on the Bitcoin blockchain is able to contain 1mb of data, meaning that the block size of bitcoin is 1 megabyte. 

- If you become a full node for the Bitcoin blockchain, meaning you help validate ongoing transactions, you 
basically have to download the entire database first. The Bitcoin blockchain is currently 5450 GB (2024). 
This represents “the total size of all block headers and transactions” since January 2009.

- The difficulty is adjusted every 2016 blocks (every 2 weeks approximately) so that the average time between each block remains 10 minutes. The difficulty comes directly from the confirmed blocks data in the Bitcoin network.

