# Lecture 2

### Clickjacking - How it is done

- The real web site is embedded in the hacker's web site with the ``<iframe>`` tag.
- An iframe is normally used to include another web page such as a YouTube video in one's own web 
page as demonstrated here:
  - https://www.youtube.com/embed/tgbNymZ7vqY (original video)
  - ://www.w3schools.com/html/tryit.asp?filename=tryhtml_youtubeiframe (video embedded in page)

![alt text](assets\IMG13.PNG)

- Clickjacking attacks can be prevented by including this directive in a web page's HTTP return 

header:
``header("X-Frame-Options: DENY");``
or
``header("Content-Security-Policy: frame-ancestors 'none'", false);``

- You can test a site for the presence of this protection here: 
    - https://geekflare.com/tools/x-frame-options-test
If you find this line in the returned message:
- ``X-Frame-Options: DENY``

it will force the browser NOT to render the page in an iframe!

- This is another trick that was once exploited by registering the malicious site http://www.pаypal.com in 2005 
- (the first a character in "pаypal" is replaced by a Cyrillic а).

It is called a homoglyph attack.
- The attacker uses letters from another alphabet (like Cyrillic) that look like Roman letters and registers this text as a URL.
- Here is a website that demonstrates how you can form such a URL
  - https://www.irongeek.com/homoglyph-attack-generator.php
- Some browsers are now displaying those URLs in Punycode to warn the user (see 
  - https://en.wikipedia.org/wiki/Punycode).

### When security needs and business needs collide, business wins

Information security performs four important functions for an organization:
1. Protects ability to function
2. Enables safe operation of applications implemented on its IT systems
3. Protects data (stored and transmitted) that the organization collects and uses
4. Safeguards technology assets in use

> - 'we need secure implemented, but there is a business need'
>   - business needs always trump the security needs
>   - can't make money, business halts

### Protecting the functionality of an organization
Decision makers in organizations must set policy and operate their organizations in compliance with the complex, shifting legislation that controls the use of technology.

> - IT people need to be on top of legislation
>   - e.g. new legislation obtain user consent to use cookies
>   - Law, make you liable

### Some definitions – we encountered these in week 1:
- Threat
- Attack
- Exploit
- Vulnerability
- Risk

### Threat: a potential risk to an asset, a loss of value, usually targeting a weakness/vulnerability in an asset

![alt text](assets\IMG14.PNG)

> - Spear fishing - targeting a specific person in the organisation - CEO, e.g.
> - Man in the middle - someone going to the website, SSL vunerability, hacker could pretend that they are the end website and listen to their conversation
> - DDOS/DOS - bombard a website with lots of requests, server unable to handle regular traffic
>   - DDOS - distributed - hacker has many IoT devices around the world. Malware controlling IoT devices are used as slaves to send DOS attacks
> - SQL injection 
> - Zero-day exploit - vunerability that no one knows about yet
>   - FBI harvest to break into computers
> - Advanced persistent threats - target someone for an extended period of time - hackers of countries to have the resources/manpower to hack a high-target individual
> - Ransomware - download and files are encrypted - Need to pay bitcoin etc to unlock 
> - DNS attack - can poison the DNS and direct them to the wrong site
>  - normally your computer stores it in a file instead of asking it each time

### Attack: 
- An intentional or unintentional act that can damage or otherwise compromise information and/or the systems that support it

### Exploit: 
- A technique used to compromise a system, we also speak of an attack vector (e.g. a phishing email)

### Vulnerability: 
- A (potential) weakness in an asset or its defensive control system(s)


> - need to discern how big your risk profile is
>   - need to determine the correct countermeasures for your risk profile

### Threat #1: Deviations in Quality of Service
- Includes situations where products or services are not delivered as expected.
- Internet service, communications, and power irregularities dramatically affect availability of information and systems.
- **Internet service issues**
  - Internet service provider (ISP) failures can considerably undermine availability of information
  - Outsourced Web hosting provider assumes responsibility for all Internet services as well as hardware and Web site operating system software
- **Communications and other service provider issues**
  - Other utility services affect organizations: telephone, water, wastewater, trash pickup, etc.
- **Power irregularities**
  - Commonplace, organizations with inadequately conditioned power are susceptible, controls can be applied to manage power quality, fluctuations (short or prolonged)

> - power irregularities
>   - power conditioner before going into the computer

### Threat #2: Espionage or Trespass
- Access of protected information by unauthorized individuals
- Competitive intelligence (legal) vs. industrial espionage (illegal)
- Shoulder surfing can occur anywhere a person accesses confidential information
- Controls let trespassers know they are encroaching on organization’s cyberspace
- Hackers use skill, guile, or fraud to bypass controls protecting others’ information

### Threat #3: Forces of Nature
- Forces of nature are among the most dangerous threats
- Disrupt not only individual lives, but also storage, transmission, and use of information
- Organizations must implement controls to limit damage and prepare contingency
plans for continued operations

### Threat #4: Human Error or Failure
- Includes acts performed without malicious intent
- Causes include:
  - Inexperience
  - Improper training
  - Incorrect assumptions
- *Employees are among the greatest threats to an organization’s data*
- Again, we need to consider the appropriate controls

> *“People are the weakest link. You can have the best technology; firewalls, intrusion-detection systems, biometric devices ... and somebody can call an unsuspecting employee. That's all she wrote, baby. They got everything.”* — Kevin Mitnick

- *Social engineering:* using social skills to convince people to reveal access credentials or other valuable information to an attacker.
- *Phishing*: attempt to gain personal/confidential information; apparent legitimate communication hides embedded code that redirects user to third-party site
- Other types:
  - Business e-mail compromise
  - Advance-fee fraud

Information Security Statistics & Phishing
- By the end of 2024, cybercrime is expected to cost the world $6 trillion.
- The global information security market is forecasted to grow to $170.4 billion in 2022. 
- The average annual cost of a phishing scam in 2021 is $14.8 million for a 9,600-employee organization.

![alt text](assets\IMG15.PNG)

### Threat #5: Denial of Service

- Denial ‐ of ‐ service (DoS): attacker sends large number of connection or information requests to a target
  - Target system cannot handle successfully along with other, legitimate service requests
  - May result in system crash or inability to perform ordinary functions
- Distributed denial ‐ of ‐ service (DDoS): coordinated stream of requests is launched against target from many locations (zombies or bots – compromised machines) simultaneously

### Threat #6: Deliberate Software Attacks
- Malicious software (malware) designed to damage, destroy, or deny service to target systems
- Includes the following malware attack vectors:
  - Viruses & Worms (self-replicating)
  - Trojan horses & backdoors (non-replicating)
  - Logic bombs
  - Polymorphic threats
  - Worm hoaxes

> - install software, inside the software is malware inserted by a hacker
>  - time bomb into 
> - polymorphic threats
>   - software constantly changing bit pattern and virus scanners cannot find it
> - worm hoaxes
>   - 'click here to remove the virus' actually gives you a virus

### Malware Control Strategy

![alt text](assets\IMG16.PNG)

- This is essentially ‘pattern matching’ – there are obvious conclusions!
- If a virus comprises NEW CODE, it cannot be ‘caught’ in the above model until it has been included in the SIGNATURE DATABASE
- If the SIGNATURE DATABASE is not kept up to date, the control strategy quickly degrades.

> - Small part of the virus is isolated, scanners will look for it
> - If virus is zero-day, won't be able to find it
>   - new virus in the database

![alt text](assets\IMG17.PNG)

- We shall look later in the course at ‘Intrusion Detection Systems’ or IDS
- There is one type of IDS that can monitor files systems – especially ‘critically important’ files within those systems
- Any changes in those critical files – the IDS reports the ‘anomaly’ and this should then be investigated.

> Check whether it is the same length as it should be
>  - what an IDS does

### Threat #7: IP Spoofing
Technique used to gain unauthorized access by replacing real IP address with a trusted IP 
address

![alt text](assets\IMG18.PNG)

> - Packets of data will have a source and destination 
> - Hacker takes the valid IP address out and swaps it for an invalid IP address
>   - can do whatever they want with the data

### GPS position spoofing
- Scenario 1. Exiting the highway at the wrong location
- Scenario 2. Enforcing an incorrect speed limit
- Scenario 3. Turning into incoming traffic

### Threat #8: Man-in-the-middle
Attacker monitors network packets, modifies them, and inserts them back into network
Example: Apple’s SSL Bug: Another Man-in-the-Middle Attack (February 22, 2014) 

![alt text](assets\IMG19.PNG)

### Threat #9: Spam
Unsolicited commercial e ‐ mail; more a nuisance than an attack, though is emerging as a vector for some 
attacks

### Threat #10: Sniffer
Program or device that monitors data packets traveling over a network; can be used both for legitimate 
diagnostic purposes and for stealing information from a network
Download Network Sniffer Wireshark from here: https://www.wireshark.org/download.html 

![alt text](assets\IMG20.PNG)

### Global reports (1): 2021 SANS Cyber Threat Intelligence (CTI) survey

From Executive Summary of report – key takeaways:
- The way CTI analysts operate has changed due in large part to the coronavirus
  - Analysts disseminate information more asynchronously (emails, dashboards) rather than in  -person
  - Analysts work more on their own (home office!)
- CTI is not just for the top 1% of organizations
  - Increase of small organizations with CTI programs
  - CTI provides improved support for security at all levels and benefits organizations of all sizes
- CTI tools are becoming more automated
  - Analysts more time for higher  -level analytic activities rather than repetitive collection and processing tasks
  - More information from government security bulletins and media reporting in analysis

> SANS = System Administration, Networking and Security Institute

## Summary (Part 1)
- Information security performs four important functions to ensure information assets remain safe and 
useful
- Management must be informed about threats to its people, applications, data, and information 
systems, and the attacks they face. 
  - Threats: any events or circumstances that have the potential to adversely affect operations and 
assets. 
  - Attack: an intentional or unintentional act that can damage or otherwise compromise information and 
the systems that support it. 
  - Vulnerability: a potential weakness in an asset or its defensive controls.
- Threats can fall into 10 categories (Note: we did not cover all of them today, see also textbook)
  - Important to remember: internal/external origin; malicious/accidental origin

# Ethics

### Moral vs. Ethical
Morals define personal character, while ethics stress a social system in which those morals are applied.
In other words, ethics point to standards or codes of behaviour expected by the group to which the 
individual belongs (national ethics, social ethics, company ethics, professional ethics, family ethics). So while a person’s moral code is usually unchanging, the ethics he or she practices can be other-dependent.

### Legal vs. Ethical
Legality is a society's application of ethics to the structure of society.
An act is legal if it complies to governing laws and regulations whereas an act is also ethical if it complies to ethical policies of an organisation and it is also moral if it is correct in your opinion.

> Example:
> Abortion is legal* and therefore medically ethical, while many people find it personally immoral.

![alt text](assets\IMG21.PNG)

### Why do we talk about “Ethics”?
Most of us, day to day, have a firm ethical compass So why talk about ethics at all?
- Essentially, it’s not always clear, particularly in technology work, what is ‘right’ or ‘wrong’ in a particular situation 
- Professional ethics provides frameworks to support ethical decisions in uncertain scenarios


### The Australian Computer Society (ACS)
- “The ACS was established in 1966 as a result of the merger of then existing State based computer societies. It has become the recognised association for IT professionals, attracting a large and active membership from all levels of the IT industry, and providing a wide range of services and opportunities for networking and career enhancement.
- It is the public voice of the IT professional; the guardian of professional ethics and standards in IT; with a commitment to the wider community to ensure the beneficial use of IT.”

### ACS Code of Ethics
- It is a standard of behaviour
- Not exhaustive
- Is meant to be illustrative
- Written in terms of specific behaviour
- May conflict with standards from other sources
- The delineation between ethical and unethical has some element of subjectivity
- Members are expected to take into consideration the spirit of the code in resolving contentious issues

> - Room for interpretation; often differences in opinions

### Policy, Law and Ethics in Information Security
- Policies: Most organizations develop and formalize a body of management views/expectations called policy. Policies serve as organizational laws – the view of management.
- To be enforceable, policy must be distributed, readily available, easily understood, and acknowledged by employees – and assessed from a legal viewpoint. 
- The **Code of Ethics** provides a framework for ethical decision-making, while **policies provide specific guidance** on how to implement that framework in practice.

> Policies become 'law' in your business
> - Publicise the policies and check they are doing it
> - We are in charge of policies

### Privacy
- One of the hottest topics in information security:
- Privacy is a “state of being free from unsanctioned intrusion”
- Ability to aggregate data from multiple sources allows creation of information databases previously 
unheard of
- Many types of privacy issues: spamming, fraud, government intrusion.
- Information Privacy: ”the claim of individuals, groups, or institutions to determine for themselves 
when, how and to what extent information about them is communicated to others”. 
(Alan Westin – Columbia University 1967)
- Is privacy the same as confidentiality? 

### iPhone Privacy

In 2016, the Federal Bureau of Investigation (FBI) asked Apple to help them unlock the iPhone of one of the San Bernardino shooters, who had killed 14 people in a terrorist attack. The FBI was unable to access the phone's data due to its strong encryption and the passcode protection. The agency requested that Apple create a new version of its iOS software that would bypass the iPhone's security features and allow the FBI to access the data.

Apple refused to comply with the request, stating that creating such a software would undermine the security and privacy of all iPhone users. The company argued that once such a tool was created, it would be nearly impossible to keep it from falling into the wrong hands and being used for malicious purposes.
The case quickly became a highly publicized legal battle between Apple and the US government. The FBI 
eventually dropped the case after finding a third-party solution to access the iPhone's data, but the incident sparked a wider debate over the balance between national security and individual privacy.
Apple's refusal to create a backdoor to the iPhone's security features has since been hailed by privacy 
advocates as a victory for digital rights, while some law enforcement officials have criticized the move as hindering their ability to prevent and investigate criminal activities.

> Created lots of waves in the industry
> - hindering criminal activities

### In comparison: TOLA Act in Australia

In 2018, the Australian government passed the Telecommunications and Other Legislation Amendment (TOLA) Act, which requires technology companies to provide law enforcement and security agencies with access to encrypted communications when requested. The law has been criticized by privacy advocates, who argue that it undermines the security and privacy of users and could potentially weaken overall cybersecurity.
- See GOING-DARK-Kopsias.pdf on Blackboard.

> Criminals 

### Australian IT/Privacy Law
- Prohibits breaches of privacy in telecoms traffic. Exemptions made for police – with judicial approval – obligations on internet service 
providers (ISPs)
- Cybercrime Act 2001:
  - Unauthorised access, modification or impairment with intent to commit a serious offence (Section 477), Possession or control of data with
intent to commit a computer offence (Section 478), Producing, supplying or obtaining data with intent to commit a computer offence (Section 
478)
- Spam Act 2003:
  - Three steps (Consent, Identity, Unsubscription)
- Privacy Act 1988:
  - 10 principles: Collection, Use and disclosure, Data quality, Data Security, Openness, Access and correction, Identifiers, Anonymity,
Transborder data flows, Sensitive information.
  - Targets public sector. Private sector coverage introduced in 2001.
- Privacy Amendment (Notifiable Data Breaches) Act 2017: 
  - Established the NDB scheme in Australia   - applies to all agencies and organisations with existing personal information security obligations 
under the Australian Privacy Act 1988 (Privacy Act) from 22 February 2018.
- **TOLA (Access and Assistance) Bill 2018**
  - “Going dark” – see next slides
- **Surveillance Legislation Amendment (Identify and Disrupt) Bill 2021**
  - Extends TOLA bill – “Unprecedented powers for online surveillance, data interception and altering data” passed both houses of the Australian Parliament on 25 August 2021 and is now known as the Surveillance Legislation Amendment (Identify and Disrupt) Act 2021.

> CIA got hacked and all their tools used to hack devices were put onto the dark web


### “Going Dark” #1

- Traditional ‘person-to-person’ communications – who could access the communicated ‘information’?
- Traditionally, these (telephone) communications (telephone and ‘snail mail’) have allowed police/law enforcement to ‘listen-in’ (subject to judicial approval)

![alt text](assets\IMG22.PNG)

- Modern unsecured ‘person-to-person’ communications – who can access the communicated ‘information’?
- Email – can be copied at work or in private (with judicial approval). Work calls can be monitored (at work) and can be monitored in private (with judicial approval)

> Can still use sniffers

![alt text](assets\IMG23.PNG)

- Modern secured ‘person-to-person’ communications – who can access the communicated ‘information’?
- Secure email, secure digital apps (e.g. WhatsApp) cannot (in theory) be copied at any intermediate point (‘end-to-
end’ communication). This is quite different to routine ‘secured’ digital communications (e.g. between me and my 
bank – this is explained later in the course in some detail)

![alt text](assets\IMG24.PNG)

> - can't read with sniffer anymore
>   - everything is encrypted
>
> FBI put a chat program onto google
> - made a very secure chat application
> - used by criminals
> - as FBI made the app, listened to everything

- Modern secured ‘person-to-person’ communications – who can access the communicated ‘information’?
- Secure telephony cannot (in theory) be copied at any intermediate point (‘end-to- end’ communication)

![alt text](assets\IMG25.PNG)

### ‘Going dark’ – a term first introduced by the FBI (US)
- Short paper: ‘Going dark’: the unprecedented government measures to access encrypted data – Arthur 
Kopsias – Feb, 2019 (On course Blackboard site)
“The greatest benefit of encryption also creates the biggest problem. Secure, encrypted communications 
are being used by terrorist groups and organised criminals to avoid detection, and the inability of law
enforcement agencies to read or even partially understand encrypted communications has presented real 
challenges for these agencies worldwide.”
- The trust created by secure communications is essential for digital business.
- ‘End-to-end’ encryption – incorporated into email two decades ago
- ‘End-to-end’ encryption – since approximately 2015 incorporated into mobile telephony services and various apps.
This has been developed into a very powerful marketing concept by corporate communication companies (see video
from Apple on next slide)
- Over 90 percent of telecommunications information being lawfully intercepted by the Australian Federal Police now
uses some form of encryption.
- End to end security (i.e. digital privacy) now a very significant marketing discourse for the corporate telcos

> - Australian government response to going dark - TOLA act
> - Communication providers (IP, clouds storage) have to give data.
>   - Also have the right to change the data

### TOLAAct – overview – it is designed to be ‘cooperative’
- Schedule 1 of the TOLA Act inserts a new ‘Industry Assistance’ section into the Telecommunications Act 1997. 
  - A new operational protocol by which Carriers/Carriage Service Providers (‘CSPs’) will provide assistance to law enforcement and security agencies.
- This ‘Industry Assistance’ framework contains three distinct new powers which allow an agency
head to issue:
- **‘technical assistance request’** (TAR) for voluntary assistance from the CSP
- **‘technical assistance notice’** (TAN) for compulsory assistance from the CSP – this power is 
used in cases where the CSP is already capable of providing the assistance.
- **‘technical capability notice’** (TCN) for new capabilities. This notice can only be used by the 
Australian Attorney-General and requires a CSP to create a specific capability where the CSP is 
not currently able to assist.

> CSP - carrier service provider
> - Three levels, less friendly than the last
> - TAN is compulsory
> - If encrypted, and cannot do it, issue a TCN.
>   - make software to make it possible to get the information
>   - Free from liability - have to make the software to make it happen


- The term ‘Carriers/Carriage service providers (CSPs)’ is broadly defined in the Act so that it includes the wide range of entities integral to the 21 st century Australian communications operational environment.
The main descriptors are as follows:
  - CSPs that are based in Australia, and those providers based offshore who operate or supply communications services, devices or products for use within Australia.
  - Anyone who facilitates the services of CSPs.
  - Electronic service providers (with at least one end-user in Australia) and anyone who facilitates the services of electronic service providers, e.g. Facebook, Google, and Amazon Web Services;
  and
  - Manufacturers of electronic equipment and anyone who facilitates the manufacture of electronic equipment used in Australia, e.g. Samsung, Apple.

### TOLA Act - overview - what kind of assistance?
- Section 317E sets out, in some detail, the types of assistance that may be specified. These types
include (but not limited to):
- Providing technical information.
- Facilitating access to services and equipment.
- Removing one or more forms of electronic protection.
- Modifying technology.
- Concealing that the company has done any of the above.
- Example: The assistance may require the issue (to a specific criminal suspect) of a notice to update 
messaging software – when in fact the ‘update’ will then allow access to the messages of that suspect.
- No introduction of systemic weaknesses and vulnerabilities (also know as ‘backdoors’ for
encryption mechanisms)
- Civil immunity is available for CSPs acting in good faith to ensure that they are protected from any legal risk.

### Other details
- **Organisations**: The use of the powers has been restricted to the Australian Federal Police, the
Australian Criminal Intelligence Commission, the Australian Security Intelligence Organisation, the 
Australian Secret Intelligence Service, the Australian Signals Directorate, and State and Territory Police 
forces.
- **Responsible officer**: ATAR or a TAN may be issued by the head (or delegate) of each agency above.
A TCN may only be issued by the Attorney-General
- b: The use of the powers is connected to the safeguarding of national security or
(for State/Territory/Commonwealth Police) the enforcing of criminal law so far as it relates to serious 
Australian or foreign offences (defined as punishable by a maximum term of 3 years imprisonment, 
or more, or for life’.
- **Enforcement**: The framework is not intended to be adversarial – it intends to engender a spirit of 
cooperation. However – civil penalty for contravention is $10 million for corporate entities and
$50,000 for private individuals.
- **Oversighting and reporting**: The Commonwealth Ombudsman or Inspector- General of Intelligence
and Security. The use of industry assistance powers is subject to annual reports to the Home Affairs
Minister.

The TOLA Bill was introduced to the Australian Parliament on 20 September 2018.
- The Bill created significant interest (here and abroad) – the main concerns were:
  - Perceived privacy implications
  - Withdrawal of international corporate investment in Australia, 
  - Loss of public confidence in Internet trust levels.
- The Bill was subsequently referred to the Parliamentary Joint Committee on Intelligence and Security (PJCIS) 
for inquiry and report.
- The PJCIS then received a very large number of submissions expressing concerns with the Bill (from the Law 
Society of NSW, the Law Council of Australia, carrier industry providers, law enforcement/security agencies, and a 
large number of other commercial and private legal institutions.
- The Bill became law on 8 December 2018. The reason given for the rapid passage of these complex reforms: a 
heightened risk of terrorist incidents over the Christmas and New Year period (2018)


- Updates Surveillance Devices Act 2004 and Telecommuications Act 1979/1997

Three new powers:
1. “data disruption warrants”: allow authorities to “disrupt data” by copying, deleting or modifying data 
as they see fit
2. “network activity warrants”: permit the collection of intelligence from devices or networks that are 
used, or likely to be used, by subject of the warrant
3. “account takeover warrants”: let agencies take control of an online account (such as a social 
media account) to gather information for an investigation.

What’s different to previous laws?

- Telecommunications Act 1997: only permits to intercept or access communications and data under certain circumstance.
- Identity and Disrupt Bill 2021: unprecedented interception or “hacking” powers (access can be gained to encrypted data which could be copied, deleted, modified, and analysed even before its relevance can be determined).

--- REST NOT EXAMINABLE
