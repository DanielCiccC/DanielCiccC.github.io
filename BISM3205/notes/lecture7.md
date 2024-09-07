# Lecture 7 

- Certificate Authority (CA) - distribution of public keys with trust
- Two important protocols in business
  - SSL/TLS (for the web)
  - S/MIME (for email)

### Symmetric key
Has been around a long time (Caesar cipher).

![alt text](assets\IMG93.PNG)

### Asymmetric key
Theory evolved in late 70s, the first major change in cryptography in a long time.

![alt text](assets\IMG94.PNG)

> - encrypt and decrypt with either key
> - difference between encrypting with private versus public key

### Difference Between Hashing and Encryption

![alt text](assets\IMG95.PNG)

- Hashing is a one-way function that changes a plain text to a unique digest† that is irreversible.
- Encryption is a two-way function that includes encryption and decryption.

> - Hashing is not reversible
> - hash and encrypt message to check it has not been tampered

### Apply RSA Cryptography
1. Goto https://tinyurl.com/UQEncryptionKey  (https://www.devglan.com/online-tools/rsa-encryption-decryption)
2. Create a public/private key pair† with the default number of bits. 
3. Have a look at n, e of your public key https://report-uri.com/home/pem_decoder
How many hex digits in n? How many bits in n?
4. Create a secret message using your private key (keep this secret!)
5. Goto https://tinyurl.com/UQCyberSecurity  (https://docs.google.com/document/d/1zqlYZrOUyh-oYaE2cMQFGRf9U5rxMxy8ZND4ytsvGIM/edit?usp=sharing)
6. Enter your secret message and your public key into the table
7. Decode the message of another student using their public key and enter the decoded message into the 
table
8. Try decoding a message with a different public key
9. Confidentiality or Authentication and Integrity?

![alt text](assets\IMG96.PNG)

> - has 64 encoding

### Third-Party Trust (Simplified)
![alt text](assets\IMG97.PNG)


### Public key infrastructures (PKI) 
-  The use of public keys requires a framework of trust (why?) 
-  Trust defined as the firm belief in the reliability, truth, or ability of someone or something 
-  This is what a PKI is – it is a framework for the practical operation of public key cryptography – more 
specifically, a framework for the trusted (i.e. authenticated) distribution of public keys.
-  A PKI contains/provides:
  -  Standards (important to us)
  -  Certification Authorities (important to us)
  -  Certificates (important to us)
  -  Operational protocols (important to us)
  -  Interoperable tools
  -  Legislation (e.g. are digital signatures legally enforceable?) – we do not treat this.

> - like a digital passport
> - have a certificate for email, correspondence and other things


- Integrated system of software, encryption methodologies, protocols, legal agreements, and third- party services 
enabling users to communicate securely
- PKI systems are based on public-key cryptosystems
- PKI protects information assets in several ways:
  - Authentication: Digital certificates in a PKI system permit individuals, organizations, and Web servers to authenticate the 
identity of each of the parties in an Internet transaction
  - Integrity: A digital certificate demonstrates that the content signed by the certificate has not been altered while in transit
  - Confidentiality: PKI keeps information confidential by ensuring that it is not intercepted during transmission over the Internet
  - Authorization: Digital certificates issued in a PKI environment can replace user IDs and passwords, enhance security, and 
reduce some of the overhead required for authorization processes and controlling access privileges for specific transactions
  - Nonrepudiation: Digital certificates can validate actions, making it less likely that customers or partners can later repudiate a 
digitally signed transaction, such as an online purchase.

> - based on public and private keys
> - you can authenticate yourself,

### Certificate authorities (CA’s) 
- Certificate Authority – a business – central within PKIs
- Trusted organization (a business, or a section within a corporation – e.g. the UQ CA) that:
  -  Accepts applications for certificates (an entity for the distribution of public keys – we talk about these in detail shortly)
  -  Authenticates applications – trust is the issue
  -  Issues certificates
  -  Maintains status information about certificates
  -  Revokes certificates
  -  Provides an historical audit trail of certificates
  -  On some scale of operation (e.g. global)

> - CA's can revoke certificates

Certificate authorities (CA’s) 
- CA must confirm the information the subject has provided. 
  - Remember TRUST is the essential goal. 
  - This level of information is therefore variable and depends on the level of trust indicated by the certificate.
- Level of trust is related to the level of assurance sought by possession (and use of) the certificate
- A Local Registration Authority (RA) may be involved – an agent acting on behalf of the CA. 
  - A CA is a business model!
- The CA issues a Digital Certificate to a suitably assessed client (i.e. individual or business)
- The issued certificate (aka as a digital ID by Verisign) can be for a variety of purposes: 
  - an TLS digital certificate (used by just about all businesses for secure Web transactions), 
  - an email certificate, 
  - a code  -signing certificate, 
  - a VPN certificate 
  - (most of these further discussed next week)

> - software you download from the internet, can make sure it has not been altered
> - VPN certificates

### Digital certificates

- A certificate is a binding between an entity’s public key and identifying characteristics of the entity. That is, a certificate contains the public key and other identifying information for some entity. 
- Similar to a ‘digital passport’ or ‘digital driver’s license.
- Also Known As: digital ID, certificate.
- Issued to an entity (person, software, hardware item, etc) For example – issued to a person for securing email, or a web server program to secure ecommerce transactions.
- Are used for authentication, key exchange, non-repudiation
- Aim to achieve TRUST

![alt text](assets\IMG98.PNG)


- We need strong authentication – we must further support the digital signature model (public key itself does not verify the ID of sender)
- The solution is a digital certificate – it verifies the owner of the certificate AND verifies the owner of the public key
- Digital certificates must be readily available and readily exchangeable (without heavy security restricting exchange)

- Bob obtains a digital certificate – which also contains his public key – from a trusted organization (the 
Certificate Authority or CA)
- Bob creates the message, signs it (using hashing and his private key) – then sends this with a copy of his digital certificate to Alice
- How have we controlled this message (integrity, authentication, non-repudiation) – explain your 
reasoning. Is Bob's key authentic? Has it been changed?

### Digital certificates #4
- Not very useful if individuals issue their own certificate (why? It must be based on trust)
- Certificates must be verifiable – forgeries must be readily detected. Therefore we must control for authentication/integrity
- Certificates must be readily available and readily exchangeable (without heavy security restricting exchange)
- Must be scalable – grow with demand (number of users and the evolution of the types of use)
- Must conform to an open standard (for future focus and individual domain needs)
- We need a Certificate Authority (CA) for certificate distribution. We also need an international standard for the content/design of a digital certificate

![alt text](assets\IMG99.PNG)

> - Domain validation can be done by authority by asking you to put text on your website
> - Organisation validation with ABN
> - To get onto google maps e.g. will send you a postcard with a number to authenticate address
> - CA does all that
>
> Certificate created
> - hash with their own private key
> - digital signature, 
> - decrpyt the 


### Digital certificates #5
- X.509 is an ITU and ISO certificate format standard (a framework or high level standard)
  - First published in 1988 – part of the X.500 Directory recommendations. Latest version is Version 3 issued in 1996.
  - An X.509v3 certificate contains a set of basic, predefined fields and zero or more extension fields. This is the standard that business should use when a digital certificate is required (and it frequently is) – it is very widely recognised.
- Each certificate contains the public key of a user and is signed with the private key of a CA 
  - (does the certificate contain the PRIVATE KEY?)
- Is used in S/MIME, IP Security, SSL/TLS and other protocols

![alt text](assets\IMG100.PNG)

![alt text](assets\IMG101.PNG)

> - Hash of plain text is encrypted with their private key

### Root and user-level certificates
- Characteristics of certificates generated by CA:
  - Any user with access to the public key of the CA can verify the user public key that was certified – this introduces the concept of a root certificate – the trusted distribution of the CA’s public key
  - No party other than the CA can modify the certificate without this modification being detected – this 
is because of the inbuilt digital signature control (i.e. contained within the digital certificate)
- Therefore we end up with (at least) two levels of certificates: 
  - (1) root certificates (i.e. the certificate of a CA containing the public key of the CA), and
  - (2) user-level certificates (containing the public key of the user and issued by the CA using its 
public key)

> - Does not have a valid certificate, will tell us not to log on

### Digital certificates (continued)
- A primary responsibility of a CA is to revoke certificates (they have an expiry date – but sometimes 
it is necessary to ‘remove’ the  certificate from general circulation before this date is reached)
  - Certificate Revocation Lists (CRL)
  - Revocation status is the most prominent information a CA maintains about the  status of a certificate
  - Revocation reasons: key compromise, change in the subject’s affiliation, CAs  certificate has been 
compromised
  - CRLs must be publicized by CAs
  - Distribution method – polled or pushed by certificate using software (e.g., web  browser – certificates 
are used heavily by Web browsers – e.g. Firefox, IE,  etc. – more on this next week)
  - X.509 specifies a CRL format – the format is not examinable, included here for completeness.


![alt text](assets\IMG102.PNG)

# Security Topic – Cryptography (2) 
## SSL/TLS (web), S/MIME (for email)

Firstly, communication protocols – some important characteristics
- Know what a protocol is …
- Know basic telecommunications terminology.
- Understand the nature of processing in a layered communications protocol – how the protocols combine 
to get the whole job done.
- Know the purpose of the five layers of the TCP/IP ‐ OSI protocol/model/framework
- Appreciate that protocols construct the content of network packets (which are comprised of control 
headers and data)

> - communicate data across devices

Communication protocols – consider ‘snail-mail’ addressing
![alt text](assets\IMG103.PNG)


### Internet
![alt text](assets\IMG104.PNG)

### OSI vs. TCP/IP Model 7 vs 5 layers

![alt text](assets\IMG105.PNG)

Some abbreviations:
OSI: Open Systems Interconnection
TCP: Transmission Control Protocol
IP: Internet Protocol
UDP: User Datagram Protocol.

> - IP address
> - MAC address is a particular identifier for a hardware
>   - two digits separated by hyphens
>   - first six are the manufacturer
>   - other six digits are for a device
>   - hex digits, large address space
>   - uniquely identifying hardware
>
> - FTP - file transfer protocol
> - first part of URL

![alt text](assets\IMG106.PNG)

![alt text](assets\IMG107.PNG)

Conceptual data flow in a simple network topology of two hosts (A and B) connected 
by a link between their respective routers. The application on each host executes 
read and write operations as if the processes were directly connected to each other 
by some kind of data pipe. After establishment of this pipe, most details of the 
communication are hidden from each process, as the underlying principles of 
communication are implemented in the lower protocol layers. In analogy, at the 
transport layer the communication appears as host-to-host, without knowledge of the 
application data structures and the connecting routers, while at the internetworking 
layer, individual network boundaries are traversed at each router.

> - always has to travel this path


### Communication protocols – a series of ‘layers’
We have (from the ISO) a ‘layered’ communication model. This will be very helpful for our 
work with other security topics (e.g. firewalls). We show an adapted version of this below.

![alt text](assets\IMG108.PNG)


![alt text](assets\IMG109.PNG)

### Network & computer address (IP Addresses)
- The Internet uses addresses, which are also called IP addresses, for example, 192.168.2.28. 
- An IP address comprises a network identifier component and a host identifier component. 
- Layer 3 (network layer) is concerned with IP addresses. 
- So 192.168.2.28 has a network identifier component (i.e. part of the address) AND a computer identifier 
component (i.e. the other part of the address) - learn which is which next week!

#### Application address (Port Address or simply: port)
- The concept of a port number (a simple integer) is used to identify the identity of the application sending 
the communication and also the identity of the application receiving the communication. 
- Ports are extremely relevant in IS security. 
- Layer 4 and 5 (transport & application) are concerned with port addresses.
-  As an example, a ‘web server’ always has port 80, you write port numbers like this 192.168.2.28:80


> - two components, network and computer
> - in home network, last two numbers will change
> - Use of port number to identify the application sending the communication

### Communication protocols in action – email (SMTP)

![alt text](assets\IMG110.PNG)

### Communication protocols in action – web (HTTP)
![alt text](assets\IMG111.PNG)

### Security protocols – important characteristics
- We must differentiate between Offline and Online Encryption Systems
- Secure communication protocols
- Offline communication protocol (**email**) – take a message, encrypt it and either store the 
message or transmit it to another user (**S/MIME**)
- Online communication (**web**) – require real time interaction between participants (**TLS**)

> - S/MIME: Secure/Multipurpose Internet Mail Extensions. 
> - TLS: Transport Layer Security.
> - TLS is the successor to Secure Sockets Layer (SSL) and is often referred to as SSL/TLS.

### Web is online – therefore TLS is online
(communicating with each other in ‘real-time’)

![alt text](assets\IMG112.PNG)

### Email is offline – therefor S/MIME is offline 
(not communicating in ‘real-time’)

![alt text](assets\IMG113.PNG)

### The web requires an online security protocol
![alt text](assets\IMG114.PNG)

HTTP is the communication protocol between a web browser and a web server – it is a very simple ‘language’designed to enable 
a ‘discussion’between the two entities – this defines the Web. Originally, the Web had NO SECURITY – it has now been added –
we shall now discuss this security protocol!


### Web security – historically via Secure Sockets Layer (SSL)
![alt text](assets\IMG115.PNG)

- For over 20 years Secure Sockets Layer (SSL) has been in the market as one of the most widely ‐ used encryption protocols 
ever released and remains in widespread use today despite various security vulnerabilities exposed in the protocol.
- SSL v3.0 was superseded in 1999 by TLS v1.0, which has since been superseded by TLS v1.1 and v1.2. To date, SSL and 
early TLS no longer meet minimum security standards due to security vulnerabilities in the protocol for which there are no 
fixes. It is critically important that entities upgrade to a secure alternative as soon as possible and disable any fallback to 
both SSL and early TLS.
- The SSL protocol (all versions) cannot be fixed. SSL and early TLS (1.1) no longer meet the security needs of entities 
implementing strong cryptography to protect payment data over public or untrusted communications channels. Additionally, 
modern web browsers have begun prohibiting SSL connections, preventing users of these browsers from accessing web 
servers that have not migrated to a more modern protocol.


- SSL  ‐  was extremely successful – widely deployed – no longer to be used. Directly dependent upon 
digital certificate ownership  ‐  Devised by Netscape
- TLS (transport layer security)  ‐  an Internet standard (TLS) managed by the Internet Engineering 
Taskforce (IETF). Latest version: TLS 1.3 (August 2018) TLS now to be used.
- A general purpose security protocol – not a specialized secure payment protocol. What does this mean
  - Not just for the Web  ‐  secures any content that will be carried by TCP (explained next week)
  - Does not provide transaction accountability, i.e. does not check if credit card is valid
  - Secures data during transmission only – not whilst resident on client or server machines

> - just making the transport over the internet secure

### Web secure communication: TLS
- Transport layer security (TLS) protocol: an Internet standard (TLS) managed by the IETF. 
- TLS now to be used
- HTTPS
  - The HTTP protocol with the data encryption using TLS

![alt text](assets\IMG116.PNG)

> - standard is everything should be encypted

### Transport Layer Security (TLS)
- TLS working group was formed within IETF
- First version of TLS can be viewed as an updated version of SSLv3.1
- We must consider:
  - Levels of authentication (partial or full   - implications)
  - Paradigms of security (it is hybrid, symmetric key and public key)
  - Key distribution problem
  - Certificate usage   - private key usage to confirm ownership of certificate.
  - Root certificates   - where must they be located  ‐  implications

![alt text](assets\IMG117.PNG)

> - encrypt a generated private key with the web-server's public key
> - can communicate using the private (symmetric) key

### TLS – How it works – (a business conceptual view)

![alt text](assets\IMG118.PNG)

### Does TLS do everything? NO!

- TLS transmits data securely – does not check transaction integrity/correctness!
  - Does not check card number
  - Does not check customer status
  - Does not complete the transaction
  - Does not separate information on a ‘need to know’ basis
- Frequently leads to design solutions where credit card numbers are stored on the merchant’s server
- Does not separate our merchant and bank data

Now let's look at:
- Levels of authentication (partial or full - implications)
- Paradigms of security (it is hybrid, symmetric key and public key)
- Key distribution problem
- Certificate usage - private key usage to confirm ownership of certificate

### TLS: Levels of authentication – server (always) – client (rarely)
![alt text](assets\IMG119.PNG)

3. Validate server’s certificate: signature 
via root certificate, URL matches name 
on certificate, validity from-to current. 
If not valid, user is warned. Generate 
symmetric session key

5. Server uses its private key to decrypt session
key. Now both sides use this session key to
exchange secured data. Session key typically
128 bits long. Server’s public key typically 
1024 bits long.

### Email secure communication

- S/MIME (Secure/Multipurpose Internet Mail Extensions) – Enables end to end encryption 
(confidentiality) and also authentication + integrity (user to user)
- PGP (Pretty Good Privacy) – Also enables end ‐ to ‐ end.
- Unlike TLS, we can have either confidentiality OR authentication/integrity OR all three together
- Both protocols (S/MIME PGP) work in a very similar fashion.
- Both protocols are offline.
- Our focus is on S/MIME 
  - this protocol is attracting most corporate support (adopted by Microsoft)

### Email is offline – therefor S/MIME is offline (not communicating in ‘real-time’)

![alt text](assets\IMG120.PNG)

![alt text](assets\IMG121.PNG)

So if we want a digitally signed email, an authenticated and integrity-controlled email, all we need is our own certificate. 
If we want to send an email controlled for confidentiality, we need the receiver‘s certificate.

> - session key, only valid for one time
> - take receiver's public key, and encrypt session key with receiver's public
> - hash all of the above
>
> Receiver:
> - have their session key by decrypting with private key
> - decrypt the hash, and verify the email by hashing the email

### Secure Email options for our use (1)
Standard Gmail uses TLS for securing email. TLS is an open security protocol (very good) and it is the 
successor to SSL. But TLS only secures data between the sending client (usually a browser) and the 
receiving server (we stressed this in our course – TLS is very secure it is totally a ‘transmission’ security 
protocol). The data (in our case, an email) is not stored securely on the sending client – and it is not 
secured whilst on the receiving server. You could call this ‘point to point’. It is certainly not ‘end to end’. It 
does not, for example, guarantee that the message will remain private or available only to the intended 
recipient once it reaches the destination mail server. Google itself can see messages associated with your 
account, which is what allows it to scan your email for potential spam and phishing attacks (and show you 
related ads).
Beyond that basic form of encryption, Gmail supports an enhanced standard known as S/MIME — or 
Secure/Multipurpose Internet Mail Extensions (explained next paragraph). You have to supply a certificate 
that may cost money. S/MIME allows emails to be encrypted with user-specific keys so that they remain 
protected during delivery and can be decrypted only by the intended recipient. This is the meaning of ‘end 
to end’ – the sender (e.g. you/me) is one end. The receiver (i.e. the person – not the email server) is the 
other end.


**S/MIME** is very secure – it actually ‘triple wraps’ email data. When we use S/MIME we have the option to 
secure our email for integrity/authentication (digital signing) or for confidentiality (via encryption) OR 
BOTH. If we want to secure our email for confidentiality, we do the following: (1) compose the email; (2) 
our email agent (e.g. Outlook) then generates a symmetric session (one time) key and uses this key to 
encrypt our email; (3) our email agent then uses the public key of the intended recipient to encrypt the 
session key – and this encrypted result is added to the email. This is then sent to the recipient who will 
then use her/his private key to decrypt the session key – and then use the session key to decrypt the 
actual email.
This ‘end to end’ encryption ensures nobody (in transit) can view the actual email content. (Actually the 
‘triple wrap’ does a little more – but that is not important here). S/MIME is now very popular within 
corporates and government departments. However S/MIME does present ‘key management’ challenges 
(because nobody – other that sender/receiver) can access the emails – and because the sender needs the 
public key (via the digital certificate) of the intended receiver.


**PGP** has been around since the early 1990s and it has always been highly respected. At a high level of 
analysis, it is similar to S/MIME (or probably better to say S/MIME is similar to PGP). The message is 
encrypted via a symmetric (session) key generated by the sender. The message and its session key are 
sent to the receiver. The session key is protected during transmission because it is encrypted with the 
receiver's public key. PGP is an excellent email security system – however it seems to have ‘lost out’ to 
S/MIME (especially when Microsoft adopted S/MIME for its email system Outlook).

**ProtonMail** is a relative newcomer. It is very well designed at many levels to achieve high security. It also 
uses ‘end to end’ security for its email content – achieved via a combination of public and symmetric key 
crypto (like S/MIME and PGP). It also offers high level of security for user authentication (i.e. logging onto 
email accounts).  Possibly the only area of criticism of ProtonMail is that it has (in the past years) been 
subject to concentrated distributed denial of service attacks that have been designed to ‘complicate’ user 
access to email and accounts.