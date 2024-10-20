# Lecture 6

### Introductions
- Encryption: converting original message into a form unreadable by unauthorised individuals – a 
confidentiality strategy. Does it physically protect the data from access?
- Cryptography: the science of making and using codes to secure transmission of information
- Cryptanalysis: process of obtaining original message from encrypted message without knowing 
algorithms
- Cryptology: an area of science (mathematics, language theory, engineering); combines cryptography 
and cryptanalysis - the science of encryption

> - Hashing - storing passwords, sort it, add to it and store the hash
> - Hashes are not reversible
>
> Encryption:
> - to some gibberish
> - can't do anything unless you have the decryption key
>
> Cryptoanalysis
> - 'Hacking' to an extent

- Algorithm – a procedural description of an activity
- Cipher: an algorithm for performing encryption or decryption
- Plain text – the message/data/information we apply the encryption algorithm to
- Cipher text – the result after we encrypted the plain text
- Key – the mapping instrument used within the cipher
- Key space – the complexity of the key
- Stream cipher - each plain text bit transformed into cipher bit one bit at a time
- Block cipher - message divided into blocks (e.g., sets of 8- or 16-bit blocks) and each is transformed into encrypted block of cipher bits using algorithm and key

Certain encryption approaches can also be used for authentication

> Cipher
> - A word for an algorithm, specifically for encrypting or decrypting
>
> Plain text
> - anything that needs to be encrypted - could be audio, video, etc.
>
> Key space
> - the longer the key space, the better
>
> Stream cipher
> - information coming down the line, encrypt it as it comes down the line
> - For a whole block of bits, encrypt one at a time

### Some important trends in cryptography
- With emergence of technology, need for encryption in information technology environment greatly increased
- The Internet (i.e., the original protocols) initially did not have any security focus for transmission of data – we shall talk about this more in a few weeks.
- All popular Web browsers and email user agents use built-in encryption features for security (i.e. certain security protocols are built into the user applications). 
  - We look at S/MIME (email) and TLS (web) in significant business detail next week
- Restrictions on the export of cryptosystems began after WWII. (The Clipper chip was a chipset that was developed and promoted by the United States National Security Agency (NSA) as an encryption device (combating “going dark”), with a built-in backdoor, intended to be adopted by telecommunications companies for voice transmission. It was announced in 1993 and by 1996 was entirely defunct).

> - No one thought about encryption (the purpose was for information sharing)
> - When used for commerce, passwords and other information had to be encrypted
> - handshake protocol which gives the key, built in to browser

> Going dark problem - great for privacy
> - don't know what is going on
> - NSA introduced clipper chip, with backdoor to decrypt data
> - Abandoned implementation of clipper chip in 1996

### Cryptography

Two main paradigms (both heavily used): Private key (symmetric) and Public key (asymmetric)

![alt text](assets\IMG72.PNG)

> - Public key encryption (also known as asymmetric)
>
> Symmetric key (private key)
> - use the same key used to decrypt and encrypt
> - has been done for a long time
>   - Called private because it has to be kept secret
> - No point in encrypting and sending a private key
>   - still implement and is very fast
>
> Public key (asymmetric encryption)
> - Two different keys
> - Can generate mathematically
>   - Used in connection with each other
> - Each of the keys enables be to encrypt and decrypt the message
>   - cannot reverse with the same key
> 
> Take plain text, and encrypt with private key
> - not very valuable
> - Want to send a message to them, have to encrypt with their public key
>
> Other way around (rightmost)
> - encrypt using private key
> - can all read my message (not confidential anymore)
> - Achieve authentication - can only be encrypted with my private key
>   - message has not been tampered

### The Caesar cipher

The Caesar cipher (100 BC) is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on.

![alt text](assets\IMG73.PNG)

**How to create**

The basic idea behind a stream cipher is to generate a keystream – a sequence of bits or bytes – that is then combined with the plaintext to produce the ciphertext. The keystream is generated based on an initial key and, often, an additional value called an Initialization Vector (IV).

![alt text](assets\IMG74.PNG)

> - have a key, 8 bits
> - maintain the key in secrecy
> - initialisation vector
>   - make the cipher look different, even if the same image
> - use the XOR function
>
> Perform the XOR cipher a second time

### Stream cipher - Application

**RC4:** One of the most well-known stream ciphers, RC4, was widely used in protocols like SSL/TLS and WEP. However, RC4 is now considered insecure due to several vulnerabilities and should be avoided.

**Salsa20/ChaCha20**: These are modern stream ciphers that are designed to be secure, fast, and efficient. ChaCha20, for example, is used in the HTTPS protocol for securing web traffic.

![alt text](assets\IMG75.PNG)

> - checksum (fingerprint function)
>   - hash function


### Block cipher (operates on fixed length groups of bits called blocks)

A block cipher is a type of symmetric encryption algorithm that encrypts data in fixed-size blocks, typically 64 or 128 bits at a time. It is one of the fundamental building blocks of modern cryptography, widely used to secure data in various applications, including SSL/TLS for internet security, disk encryption, and more.

Two widely used block cipher algorithms: AES (Advanced Encryption Standard) and DES (Data Encryption 
Standard).

**DES (Data Encryption Standard)**

DES is one of the earlier block cipher algorithms developed in the 1970s. It operates on 64-bit blocks and uses a 56-bit key. DES uses a 16-round Feistel structure†, a common design pattern for block ciphers, where each round involves substitution, permutation, and mixing with the key.

**AES (Advanced Encryption Standard)**

AES is the current standard for block ciphers, designed to be secure and efficient. It supports key sizes of 128, 192, or 256 bits and operates on 128-bit blocks.

> - substitution, permutation, and mixing with the key
>
> AES
> - longer and variable depending on the application

AES Encryption Process
1. Key Expansion: The original key is expanded into multiple round keys using a 
key schedule algorithm.
2. Initial Round:
1. AddRoundKey: The plaintext block is XORed with the first round key.
3. Main Rounds (9, 11, or 13 rounds, depending on the key size):
1. SubBytes: Each byte of the block is replaced with a corresponding 
byte from an S-box (substitution box) for non-linear substitution.
2. ShiftRows: Rows of the block are shifted cyclically to the left to 
introduce diffusion.
3. MixColumns: Columns of the block are mixed using linear 
transformation to further spread the plaintext information across the 
block.
4. AddRoundKey: The block is XORed with a round key derived from the 
original key.
4. Final Round: The last round omits the MixColumns step and consists of 
SubBytes, ShiftRows, and AddRoundKey operations.
Decryption Process
AES decryption is performed using the inverse operations of encryption, with the 
round keys applied in reverse order.


![alt text](assets\IMG76.PNG)

> - to decrypt the information, do this in reverse order

### Symmetric key algorithms
Symmetric key cryptography is the oldest form but still heavily used. Simple definition: 
- “A single key is used to encrypt and decrypt”
These two ciphers are the basis for most/all symmetric key ciphers:
- Substitution cipher: substitutes or exchanges one value for another
- Transposition cipher: rearranging the values within a block based on an established pattern.

Note: We are not discussing the details of the variations on these two ciphers, the Vigenere cipher (1553) or Vernam cipher (1917). However, some interactive tools exist to encrypt and decrypt the Vigenere cipher and others on the Internet:
- https://cryptii.com/pipes/vigenere-cipher
- https://www.dcode.fr/vigenere-cipher 
- https://www.guballa.de/vigenere-solver 


### Substitution Example
Decrypt the following line of cipher text (a simple substitution cipher with a three character key has been used). Use the underscore character (_) to represent the space character.

$$ehtwrmsrohsrmtnsy$$

The key used in the above encryption strategy is
space => r
e => s
o => t

c) The algorithm for the above encryption and decryption strategy
Starting with the first character, consider each letter of the cipher/plain text in turn. If the letter appears in the key, make the substitution – else leave  the letter unchanged.  Move to the next letter.

Answer: show_me_the_money

> - Always need the key and the algorithm

### Cryptanalysis of substitution

The most frequently occurring letters in the English language, in order of decreasing frequency, are:
\<space\>, E, T, A, O, I, N, S, H, R, D, L, U, C, M, F, Y, W, G, P, B, V, K, X, J, Q, Z

$$ehtwrmsrohsrmtnsy$$

So cryptoanalysis of the cypher text would quickly see that R is the most commonly occuring character.
In English language the most commonly occuring character in a block of text is the space.
So immediately, if we were using cryptanalysis to try and hack, this we would quickly try R being replaced by the space.
$$ehtw ms ohs mtnsy$$
And immediately we would break the cypher text into words. 
And by simple trial and error approach, we would quickly deduce that {space => r, e => s, o => t} is the 
encryption/decryption key.
$$show me the money$$
So, the point is that this type of encryption can be vulnerable to what we call frequency distribution in the 
underlying language, that means that cryptanalysis of this cypher text is easily produced.

> - Each language has their most frequent characters in text

### Transposition Example

f) Decrypt the following line of cipher text (a simple transposition cipher with a four character key has been used). The underscore character (_) represents the space character.
$$_isheamn_is_nohj$$ 

g) The key used in the above encryption strategy is {1234 becomes 4231}
  That is, within each block of four characters, the first and fourth characters are swapped.
$$_ish    eamn    _is_    nohj$$

Is the cipher used above block or stream and is it symmetric or asymmetric?
$$his_    name    _is_    john$$

> - block versus stream
>   - stream, 
>
> - Symmetric, same key for encoding and decoding

### Cryptographic Algorithms
**Symmetric encryption**
Uses same “secret key” (also known as private key) for encoding and decoding
- Encryption methods can be extremely efficient, requiring minimal processing
- Both sender and receiver must possess this key
- If either copy of key is compromised, an intermediate can decrypt and read messages
- Major difficulty: ‘the key distribution’, how do you get this key secretly to the other party?
- This is often done ‘out of band’ 

Consider how your access to the UQ network was initially set up
> - encryption method can be efficient
> - sender and receiver must receive this key
> - key distribution is a problem

### The ‘key distribution’ problem
- Simply stated:
  - How to get a key from Bob to Alice – maintaining the secrecy of the key and 
  - ensuring the key is only used by Alice for the appropriate time period
- Key distribution becomes very much harder as the cryptosystem scales up in size (i.e., more 
participants - one key for each?)
- Key distribution is a very significant issue in designing modern security protocols

Consider your access to the UQ computing infrastructure – what is the ‘key’, how is key granting and key 
distribution administered – the significance (difficulty/cost) of ‘out of band’ solutions

> - Each person must have a different password
> 

### Symmetric key cryptography

![alt text](assets\IMG77.PNG)

### Encrypting binary data
- All alpha-numeric data (whether stored, processed, transmitted) is represented in binary format (i.e., as a number consisting of digits 0 and 1 only)
- This binary data is converted back to the appropriate ‘human type’ when we need it
- We already talked about how to convert data like this using the ASCII, extended ASCII, and Unicode tables last week
- All encryption/decryption is performed on binary data (not alpha-numeric data). That is, all data (text, numbers, graphics, everything) is represented at the memory/processor level as series of digits 0 and 1

![alt text](assets\IMG78.PNG)

To encrypt this we select an encryption key that will also be stored in binary format – so we end up with all binary data!

> - binary doesn't know whether it is a 1 or x, e.g.
> - binary to character text in screen
> - Use hexadecimal beacuse each four numbers is one hexadecimal number

### Full ASCII Table

![alt text](assets\IMG79.PNG)

![alt text](assets\IMG80.PNG)


### Encryption algorithm

- Start with plain text
- Generate an ‘encryption key’
- Encrypt using XOR, bit shifting, substitution, transposition, modular arithmetic
- Very simple, very fast and very efficiently – implemented in hardware, not software
- This introduces the concept of algorithm efficiency and effectiveness.

### Encrypting CAT as VVV

![alt text](assets\IMG81.PNG)

### Cipher strength
- The inherent weaknesses of ‘simple’ substitution and transposition ciphers is that they are open to analysis via frequency and statistical studies
- The strength of a cipher (regardless of whether it is symmetric or asymmetric) is dependent upon:
  - Key length (e.g. modern symmetric key is 128 bit)
  - Algorithm correctness (are there any ‘bugs’ in the algorithm)
- Perhaps paradoxically, we get ‘more’ algorithm correctness by publicizing the details of the cipher. The best algorithms are public – why? How can this ensure/enhance security?

> - Strength comes with the key and how you handle the information with the key
> - Even with encryption standard, cannot crack it

AES, a sample of symmetric encryption, is very strong. 
The use of 128- and 256-bit keys makes it impervious to cracking.
Contrary to movies and TV, the only way to get unauthorised access to AES encrypted information is to steal or guess the key.

Guessing is impractical due to the number of possible keys. 
A 128-bit key has 2^128 =  
340,282,366,920,938,463,463,374,607,431,768,211,456 
possible keys.

An n-bit key has 2^n possible keys because for each of the n bits, we have 2 options (0 or 1).


### Cipher/key-length strength

- When using ciphers, the size of the key is very important. 
  -  Symmetric key and public key systems should be equally secure – they are not equal in computational 
efficiency (i.e. time to encrypt, memory usage, etc.)
- Strength of many encryption applications and cryptosystems measured by key size 
  - E.g., 128 bit length for symmetric, 1024 bit length for asymmetric
  - Cracking a 128-bit key with modern hardware is going to take around 500 billion years. However, quantum computers would be able to do it faster (~185 years atm).
- For cryptosystems, security of encrypted data is not dependent on keeping the encryption algorithm secret 
  - Cryptosystem security depends on keeping some or all of the elements of crypto-variable(s) or key(s) secret

![alt text](assets\IMG82.PNG)

- Data Encryption Standard (DES): one of most popular symmetric encryption 
cryptosystems – no longer in use
  - 64 ‐ bit block size; multiple ‐ rounds of encryption, 56 ‐ bit key
  -  Published in 1977 – standardized in 1979 as federal standard for encrypting non ‐ classified 
information
- Remember – the current safe symmetric key length is 128 bits

> - 56 bits were too short

### Data Encryption Standard (DES)
64 bit block size, 56 bit key size (fixed), multiple rounds, key is changed with each round,
output from one round forms the input to the next – uses SUBSTITUTION and transposition

![alt text](assets\IMG83.PNG)

### Symmetric key algorithmns

- Triple DES (3DES): created to provide security far beyond DES
  - applies DES three times to each data block (FIPS approved in 1999, withdrawn in 2005) – key length 
168 bits (three 56 bit DES keys) – deprecated by NIST in 2017 (unsafe)
- Advanced Encryption Standard (AES): developed to replace both DES and 3DES 
  - also known by its original (Dutch) name Rijndael Block Cipher.
  - Rijndael is a grouping of ciphers with different key and block sizes. 
  - For AES, NIST selected three Rijndael members, each with a block size of 128 bits but three different key lengths 128, 192, and 256 bits.

### Summary: Symmetric Key Cryptography
- Cryptography is used to secure most aspects of Internet and Web uses that require it, drawing on extensive set of protocols and tools designed for that purpose
- Symmetric key crypto uses one secret key to both encrypt and decrypt a message
- Data Encryption Standard (DES): was one of most popular symmetric encryption cryptosystems.
  - 64-bit block size; multiple-rounds of encryption, 56-bit key
  - Adopted by NIST in 1976 as federal standard for encrypting non-classified information
- Triple DES (3DES): created to provide security beyond DES
- Advanced Encryption Standard (AES): developed to replace both DES and 3DES – the main cipher is Rijndael Block Cipher
- Current safe symmetric key length is 128 bits

### Hashing (cryptographic hash functions)
Generates fixed length fingerprints of arbitrarily large messages.

![alt text](assets\IMG84.PNG)

> - take variable length message into a fixed-length hash
>   - finger print, hash will be different if only one aspect changes

### Difference Between Hashing and Encryption

![alt text](assets\IMG85.PNG)

- Hashing is a one-way function that changes a plain text to a unique digest† that is irreversible.
- Encryption is a two-way function that includes encryption and decryption.


### Hash functions

- Computationally inexpensive mathematical algorithms that generate fixed length message summary/digest to confirm message identity and confirm no content has changed provides integrity control 
- What is a hash collision? Two different inputs producing same hash – very bad!
- Irreversible unique output
- Hash algorithms: publicly known functions that create hash value:
- SHA group (SHA-1, SHA-256, SHA-384, SHA-512),
- MD family (MD2, MD4, MD5, MD6), 
- RIPEND family, Tiger, Whirlpool, …
MD4, MD5, SHA-1 are no longer considered secure due to possible hash collisions
- Also heavily used with public key cryptography to deliver digital signatures, also used in Blockchain applications


![alt text](assets\IMG86.PNG)

> - 128 / 2 = 28 hex digits
> - are not reversible 
>   - SHA1 is considered insecure due to possible hash collisions


![alt text](assets\IMG87.PNG)

> - SHA256, 256 bits longs

### Summary: Hash functions

- Mathematical algorithms that generate message summary/digest to confirm message identity and confirm 
no content has changed, i.e. provide an integrity control.
- One way – unique output (fingerprint) – computationally inexpensive
- Hash algorithms: publicly known functions that create hash value – e.g. the SHA and the MD families
- Hashing is NOT encryption
- Hashing is also heavily used with public key cryptography to deliver digital signatures.

## Public key cryptography (asymmetric cryptography) and digital signatures

### Overview
- Public key crypto - completing the theory discussion of last part – focus public key cryptography
- Digital Signatures (this concept builds on the hash strategy)

- Next week:
- Digital Certificates (for distribution of public keys with trust – a certificate contains a digital signature)
- Public Key Infrastructure (PKI) – for distribution of public keys with trust
- We look at the two important protocols in business: SSL/TLS, S/MIME

### Asymmetric cryptography – the theory
- A new approach (from the 70’s – exact date/place unknown)
- Two keys – one strictly private, one distributed to the world (public)! 
  - Both keys are generated simultaneously and are mathematically related
  - Either key can encrypt – whichever one is used, the other (matched) key must decrypt
Example: I have a public key A and a matched private key B. If I generate a message, say M, 
what happens as per the following:
- **Encrypting with the public key delivers confidentiality (why?)**
- **Encrypting with the private key delivers authentication (why?)**
Two types of security: confidentiality and authentication!

### Asymmetric cryptography – the practice (1)
![alt text](assets\IMG88.PNG)

![alt text](assets\IMG89.PNG)

2. Next, Alice creates a sensitive document, encrypts it with Bob’s public key, and sends it to Bob. Once 
she has encrypted this document, Alice cannot decrypt it (why?).
3. Upon receipt of the encrypted document, Bob uses his private key to decrypt it.

![alt text](assets\IMG90.PNG)

### Digital signatures are using asymmetric cryptography
- Created in response to rising need to verify the integrity AND authenticity of information transferred via 
electronic systems. It is an electronic/digital verification of the sender/owner of the signature.
- Hashing PLUS asymmetric encryption processes are used to create digital signatures
- Integrity, authentication and non-repudiation: the process that verifies the message was sent by the 
sender, has not been altered since the signature was added, and thus cannot be refuted/repudiated
- Commonly used for software distribution (e.g. updates), financial transactions, important digital 
communications (e.g. email), and other cases where it is vital to detect forgery/unauthorized alterations
- Digital Signature Standard (DSS) is the NIST standard for digital signature algorithm usage by federal 
information systems

### How to create a digital signature

- A digital signature is produced via a two-stage process: (1) hashing, and (2) private key signing (i.e. 
public key encryption). 
- RSA is a main encryption algorithm in producing digital signatures. The process is shown below. This 
process is supported in law by many countries.
- The Electronic Transactions Act was enacted in 1999 and established electronic signatures in 
Australia. Under Australian law, contracts are held enforceable whether it’s verbal, or the parties have 
signed the document with a wet-ink (physical) or electronic signature.

![alt text](assets\IMG91.PNG)


> - compare the hash of the message with the hash of the decrypted message

![alt text](assets\IMG92.PNG)
> - Digest

> Question: how does ‘integrity’, ‘authentication’ and ‘non-repudiation’ apply in the above example? Do we have confidentiality?
