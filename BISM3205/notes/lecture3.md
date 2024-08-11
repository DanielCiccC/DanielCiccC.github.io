# Lecture 3
- Policy is the fundamental start in information security
- It is the domain of senior management
- Senior management obviously has the power within the organisation, the capacity to apply proper resourcing, numbers of people, dollars invested in programmes etc.

![alt text](assets\IMG26.PNG)

> Create a 'law' in your country be defining a company
> - cannot create a policy that is against the law
> - policy is like a global statement

### Information Security Planning and Governance
- Corporate governance is the set of processes, 
customs, laws and institutions which affect the 
way an organisation is directed, administered and 
controlled
- IT Governance is an integral part of CG and 
ensures the effective and efficient use of IT in 
enabling an organisation to achieve its goals. 
- Security governance is the system by which 
security-related activities are directed and 
controlled
- IT governance and security governance are part 
of the higher corporate governance and security 
governance is not only part of IT governance but 
also corporate governance. The reason is that 
legal/regulatory dimensions also fall into the area 
of the broader corporate Governance
- Security is not just an IT issue. It affects every 
aspect of an organisation

![alt text](assets\IMG27.PNG)

### Five goals of Information Security Governance
- Strategic alignment – Information Systems Security should coordinate with business strategy, it needts to fit within it and support it
- Risk management – manage and mitigate risks (lecture next week)
- Resource management – using Information Systems Security knowledge and infrastructure effectively (personnel, time and money) 
- Performance measurement – The enterprise needs metric against which to judge security policy to ensure that organisational objectives are achieved
- Value delivery – Resources expended on security should be constrained within overall enterprise resource objectives and security investments need to be managed to achieve optimum value

> - five rules of information security governance

### 1. Strategic planning
Enterprise strategic planning
- Defining long-term goals for the organisation
- Development of strategic plan to achieve those goals IT strategic planning
- Alignment of IT management and operation with enterprise strategic planning
- IT management guided by strategic planning to meet challenges (e.g., new technologies introducing new risks) 

Security strategic planning
- Alignment of security management and operation with both
- IT‘s delivery of value to organisation includes risk mitigation

> IT strategic planning
> - beyond IT management
> - new technology, zero-day exploits
> - incorporate into our plan


![alt text](assets\IMG28.PNG)

### Example: Elements of a strategic plan document

![alt text](assets\IMG29.PNG)

> - Approved by the appropriate executives and committees
> - reviewed at defined intervals
>
> Definition of a security program
> - review plan, feedback loop to relevant stakeholders

### 2. Organisational structure

![alt text](assets\IMG30.PNG)

> - auditors, important part
>   - need someone else not familiar with systems to audit/direct it
>   - beforehand make sure everything is up to scratch

### 3. Establishment of roles and responsibilities

![alt text](assets\IMG31.PNG)

- The responsibility for information security should also be placed at the manager level that is responsible for the business process.
- The responsibility for information security should not be placed at the Information and Communications Technology (ICT) department as they typically do not know all characteristics of the business processes!
- The security officer is not responsible for information security but making sure that others take on their responsibility

> - routine carve up of responsibilities
>
> Security offier's responsibility is that others take on their responsibilities
> - everyone's responsibility

4. Integration with the enterprise architecture:
Information security policies, standards, and practices

- Communities of interest must consider policies as the basis for all information security efforts
- Policies direct how issues should be addressed and technologies used
- Policies should never contradict law
- Security policies are the least expensive controls to execute but most difficult to implement properly
- Shaping policy is difficult

- Policy: course of action used by organisation to convey instructions from management to those who perform duties
- Standards: more detailed statements of what must be done to comply with policy 
- Practices, procedures, and guidelines effectively explain how to comply with policy
- For a policy to be effective, it must be properly disseminated, read, understood, and agreed to by all members in the organisation and uniformly enforced

> - translated to practises
> - how to comply with end user management
>   - have to enforce policies

### Information security policies, standards, guidelines and procedures

![alt text](assets\IMG32.PNG)

> Each are document at different levels of the enforcement
> - Can put an ACL on each control list
> - different users can login to the same control list
> - Can also do the same inside a database

### Information security policies, standards, and practices (examples)
- Employees must use strong passwords on their accounts. Passwords must be changed
regularly and protected against disclosure
- Standard: (Provides specifics to help employees comply with policy) Password length – must
include at least 1 lowercase, 1 upper case, one digit, one special character – not written down –
changed every 90 days – not held on insecure media.
- Practice: US ‐ CERT* recommends: 15 characters for admin accounts; use alphanumeric
passwords and symbols; cannot reuse previous passwords; no personal information; minimum
password length of 8 characters for standard users;  ‐ and more
- Guidelines (provide examples/recommendations): In order to create strong yet easy ‐ to ‐ remember passwords (NIST SP 800 ‐ 118): Mnemonic Method; altered passphrases

> CERT - computer emergency Response Team
>  - Offer best practise advise for the broader community

### 5. Documentation of security objectives in policies and guidance
- Sets strategic direction, scope, and tone for all security efforts within the organisation
- Executive-level document, usually drafted by or with CIO of the organisation
- Typically addresses compliance in two areas:
  - Ensure meeting requirements to establish program and responsibilities assigned therein to various organisational components
  - Use of specified penalties and disciplinary action for non-compliance
- EISP elements:
  - An overview of the corporate philosophy on security
  - Information on the structure of the information security organisation and individuals who fulfill the information security role
  - Fully articulated responsibilities for security that are shared by all members of the organisation (employees, contractors, consultants, partners, and visitors)
  - Fully articulated responsibilities for security that are unique to each role within the organisation

> ERM - enterprise risk management
> - negative influences in to organisation

![alt text](assets\IMG33.PNG)

> - policies are never set in stone, changing environment, attack vectors, etc.

### Issue-Specific Security Policy (ISSP) (1/2)

- Addresses specific areas of technology (e.g., e ‐ mail, Internet use, anti ‐ malware configuration of 
computers)
- Requires frequent updates
- Contains statement on organisation’s position on specific issue
Three approaches when creating and managing ISSPs:
- Create a number of independent ISSP documents
- Create a single comprehensive ISSP document
- Create a modular ISSP document

> Last assignment - write an issue-specific policy
> - Only passwords, only emails etc.
>
> If you are not compliant, what are the repercussions
> - many issues in a company
>   - modular document, independent and comprehensive security policy

### Issue-Specific Security Policy (ISSP) (2/2)
Components of the policy
- Statement of Purpose (scope, technology addressed, responsibilities)
- Authorized Access and Usage of Equipment (user access, fair/responsible use)
- Prohibited Use of Equipment (misuse, criminal, copyright, etc.)
- Systems Management (e.g. monitoring of employees – virus protection)
- Violations of Policy (procedures for reporting violations, penalties)
- Policy Review and Modification
- Limitations of Liability (cannot protect employees – may assist in prosecution)

### Example

![alt text](assets\IMG34.PNG)

> Acceptable use policy at UQ
> - how you can use information and communication at UQ
> - Not debbie anymore, is now CIO (one level down, more specific)

### Systems-Specific Security Policy (SysSP)
- SysSPs frequently function as standards and procedures used when configuring or maintaining systems
- Systems ‐ specific policies fall into two groups
  - Managerial guidance (most often lead to "technical specs")
  - Technical specifications
- Example (Access Control Lists or ACLs)
  - ACLs can restrict access for a particular user, computer, time, duration—even a particular file
  - ACLs focus on the organisational asset. Capability tables focus on users
    - Who can access the system (individual identity or group membership)
    - What authorized users can do (Read, Write, Create, Modify, Delete)
    - When authorized users can access the system
    - Where authorized users can access the system from (local/remote)

> Access control lists before
> - particular program

### Local security policy on Windows

![alt text](assets\IMG35.PNG)

> - Create a policy at somewhere like UQ, create an image, test it, and dump it onto all PC's in computer labs

### Policy Management
- Policies must be managed as they constantly change
- To remain viable, security policies must have:
  - Individual responsible for the policy (policy administrator)
  - A schedule of reviews
  - Method for making recommendations for reviews
  - Specific policy issuance and revision date
Have a look at one of UQ‘s policies: can you identify who is responsible? The revision dates?

> - Mechanisms for making suggestions for improvement
>   - How can I tell these people to improve this policy?

### Security education, training, and awareness program (SETA)

- Once general security policies exist, implement a security education, training, and awareness (SETA) program.
- SETA is a control measure designed to reduce accidental security breaches.
- Security education and training builds on the general knowledge the employees must possess to do
their jobs, familiarizing them with the way to do their jobs securely
- The SETA program consists of: security education; security training; and security awareness

> Control security culture in company 
> - Control that focuses on internal threats


### Comparative Framework of SETA

![alt text](assets\IMG36.PNG)

> Training - staff have to do cyber security awareness training

### The Information Security Blueprint
- After policy/standard development – then develop blueprint (what is a ‘blueprint’ ‐ what are we talking about here?)
- Should specify tasks to be accomplished and the order in which they are to be realized
- Should also serve as scalable, upgradeable, and comprehensive plan for information security needs for coming years
- We should look to recognised standards to assist! 

> Template
> - Operationalise the policy
> - software, hardware, entities
> 
> We need to know what we have, all the assets we have

### The ISO 27000 Series
1. One of the most widely referenced and often discussed security models
2. ISO27002 provides a common basis for developing organisational security:
- Via a list of 14 control areas, addresses 39 control objectives and more than 110 individual controls
3. ISO27002 is a (long) list of IS controls – experience shows that ‘just’ implementing controls is not 
enough – we need very good ‘security management’
4. Therefore, the ISO27002 is complemented with ISO27001 which describes ‘security management’. 
- It is fundamental that ISO27001 considers that IS Security is seen as a continual improvement 
process – and not as implementing a security product.
5. ISO 27001/27002 together function as a framework for information security:
- Organisational security policy is needed to provide management direction and support – its purpose is to give recommendations for IS security management.

> REMEMBER: ISO 27001 provides information on how to implement ISO 27002 and how to set up an information security management system (ISMS).
> - Policy is trickled down into a procedure to implement in the company (page 11)

- Based on the ideas of quality management systems (ISO 9001).
  - ISO 9001 has become the most widely used and implemented quality management
system in the world.
- Many such management systems exist, e.g.:
  - Information Security management (ISO 27001)
  - Digital certificate management (ETSI TS 101 456)
  - Environment management (ISO 14001)
  - Occupational Health & Safety management (BSI OHSAS 18001)
- As with all management systems also an organisation’s ISO 27001 implementation can be formally certified.

#### All the standards
- ISO/IEC 27000 - Information security management systems; overview and vocabulary
- ISO/IEC 27001 - Information technology; security techniques; information security management
systems – 27001 focuses on processes for security!
- ISO/IEC 27002 - Code of practice (controls) for information security management - 27002 focuses on
the controls for security!
- ISO/IEC 27003 - Information security management system implementation guidance
The ISO 27000 Series (cont‘d)
- ISO/IEC 27004—Information security management; measurement
- ISO/IEC 27005—Information security risk management
- ISO/IEC 27006—Requirements for bodies providing audit and certification of information security 
management systems
- ISO/IEC 27007—Guidelines for information security management systems auditing (focused on the management system)

### The ISO 27001 & 27002 – a framework
In the later parts of the seminar we consider a standard for information security for any business processing MasterCard, Visa Card etc. And this standard is termed PCI-DSS. 

If a business is going to do credit card transactions, debit cart transactions with Visa MasterCard and the like, they must comply with the PCI-DSS. 

If a security breach occurs and the auditors find the business was not in compliance with the standard, the credit card companies will sue that business, and they will sue the business very savagely. 

So this would be a standard. You sign a contract, if you breach the contract, you pay the penalty for non-compliance. 

The approach of the ISO is a framework. There is no signing up to it. There‘s no penalties for non-compliance. They are literally issued to try and help improve information security. 

> - they are frameworks
> - Considered best practise in the industry

### The ISO 27001: The Plan Do Check Act (PDCA) model applied to Information Security Management System (ISMS) processes

![alt text](assets\IMG37.PNG)

> SCRUM - 2-4 weeks
> - last thing at the end of the sprint, quality control processes implemented
>
> ISMS - information security management system


### The ISO 27001: 2013 (more detailed view)

![alt text](assets\IMG38.PNG)

### The ISO 27001: 2013 – major process steps

![alt text](assets\IMG39.PNG)

This is project management 101.
1. We establish the project, we 
identify the requirements, we 
define the scope.
2. We design the process of risk 
assessment and treatment.
3. We implement all required 
controls that come from that (this 
is the part where 27001 links 
across to 27002)

### The ISO 27002: 2013 – content (1)

![alt text](assets\IMG40.PNG)

![alt text](assets\IMG41.PNG)

> Provides us with the security blueprint that we can implement
> - standard so that we don't forget this

### Variations on ISO2700x for the medical sector (IS)
- There is also an ISO standard (27799) variant on the ISO 27002 for the medical sector ‘Health informatics - Information security management in health using ISO/IEC 27002 
(https://www.iso.org/standard/62777.html)
- It applies to health information in all its aspects, whatever form the information takes (words and numbers, sound recordings, drawings, video, and medical images), whatever means are used to store it (printing or writing on paper or storage electronically), and whatever means are used to transmit it (by hand, through fax, over computer networks, or by post), as the information is always appropriately protected.
- By implementing ISO 27799:2016, healthcare organisations and other custodians of health information will be able to ensure a minimum requisite level of security that is appropriate to their organisation's circumstances and that will maintain the confidentiality, integrity and availability of personal health information in their care.

> - Medical data, security standards need to be higher
> - tips and hints on how you can secure your medical instrument
>   - they get forgotten about when software upgrades happen
>
> Zero-day hacks available on websites

### NIST security models (very important also)

- Documents available from Computer Security Resource Center of the National Institute of
Standards and Technology (NIST)
  - SP 800‐12, The Computer Security Handbook
  - SP 800‐14, Generally Accepted Principles and Practices for Securing IT Systems
  - SP 800‐18, The Guide for Developing Security Plans for IT Systems
  - SP 800‐26, Security Self‐Assessment Guide for Information Technology Systems
  - SP 800‐30 (Revision 1), Risk Management Guide for Information Technology Systems
- All these standards are freely available (in PDF) from https://www.nist.gov/
… and there are many more standards for IS security (https://csrc.nist.gov)!

> - Comparable to ISO

### Design of security Architecture

Once we have decided to use a particular standard, we have to set the foundation of the security framework

**Levels of controls**
- Management controls cover security processes designed by strategic planners and performed by security 
administration
- Operational controls deal with operational functionality of security in organisation (personnel/physical security,
education, equipment maintenance)
- Technical controls address technical implementations related to designing and implementing security

![alt text](assets\IMG42.PNG)

> - spheres of use (LHS) and spheres of protection (RHS)
>
> Information sits in the middle
> - systems embedded in networks, embedded in the internet

### Design of security architecture (continued)
- Defense in depth
  - Implementation of security in layers
  - Requires that organisations establish multiple layers of security controls and safeguards
- Security perimeter
  - Border of security protecting internal systems from outside threats
  - Does not protect against internal attacks from employee threats or on-site physical threats

**Diagrams and concepts explored later in course – introduced here**
- Firewall: device that selectively discriminates against information flowing in or out of organisation
- DMZs: no ‐ man’s land between inside and outside networks where some place Web servers
- Proxy servers: performs actions on behalf of another system
- Intrusion detection systems (IDSs): An effort to detect unauthorized activity within inner network,
or on individual machines, organisation may wish to implement an IDS

> Defense in depth:
> - several layers of security - not just a lock on the front door, login/password
> - applied to networks
> 
> ![alt text](assets\IMG43.PNG)
>
> - piece of network in between, 
> - protective area
> - website will sit in the DMZ
> - Want to access company data, have to go through a proxy server
> email will go thru proxy server


![alt text](assets\IMG44.PNG)

> - internet, wild west
> - DMZ - proxy server and firewall
> - data server when you are working within the company
> - VPN
>   - VPN server in the DMZ that will create a secure encrypted tunnel to act as a computed on a trusted network

## Part 2: Three Lines of Defense vs. Five Lines of Assurance 

- Sometimes they are legislated


> Why do we care about governance frameworks?
> - I dont care, I don't have money or time
>
> They are legislated
> - it is the law
> - Authority (APRA) makes sure there is compliance

### 3LoD for Cyber Security

![alt text](assets\IMG45.PNG)

First LoD is the function that owns and manages
risk. Within the first LoD, businesses can set up 
control functions (e.g., IT control, which reports to 
the IT department) to faciliate the management of 
risk. 

Second LoD is the independent 
control function (e.g., IT risk, IT 
compliance) that oversees risk and 
monitors the first LoD controls. 
They can challenge the 
effectiveness of controls and 
management of risk across the 
organisation. 

Third LoD is internal audit, which provides 
independent assurance. It provides the well-
informed sense of assurance that the risks and 
controls are in balance. It provides evidence, that 
risks and controls are in balance. They evaluate 
how effective the other two lines of defense are. 
How effective are our controls, how effective is our 
risk management.

> First line of defense
> - the function that owns and manages the risk
> - IT control, reporting to IT department
>
> Second line of defense
> - independent control function
> - challenge the effectiveness and controls across the organisation
>
> Third line
> - internal audit checking at regular intervals

### Owners and key activities of the First Line of Defense

- Operational managers that own and manage risks and controls
- Implement corrective actions to address process and control deficiencies
*Common first line of defense activities:*
- Administer security procedures, training, and testing
- Maintain secure device configurations, up-to-date software, and security patches
- Deploy intrusion detection systems and conduct penetration testing
- Securely configure the network to adequately manage and protect network traffic flow
- Inventory information assets, technology devices, and related software
- Deploy data protection and loss prevention programs with related monitoring
- Restrict least-privilege access roles
- Encrypt data where feasible
- Implement vulnerability management with internal and external scans
- Recruit and retain certified IT, IT risk, and information security talent


### Owners and key activities of the Second Line of Defense
- IT risk management and IT compliance functions
- Play key role in an organisation‘s security posture and program design
- Responsible for:
  - Cybersecurity-related risk assessment and alignment with organisation‘s risk appetite
  - Monitoring risks and changes to laws and regulations
  - Collaborating with the first-line functions to ensure appropriate control design

> - controls are covering the risk
> - risk that is not covered is the residual risk
>   - large risk appetite, residual risk will be bigger
>   - very risky to do something, but very beneficial
>   - risk a lot for a big benefit


*Common Second Line of Defense Activities:*
- Design cybersecurity policies, training, and testing
- Conduct cyber risk assessments
- Gather cyber threat intelligence
- Classify data and design least-privilege access roles
- Monitor incidents, key risk indicators, and remediation
- Recruit and retain certified IT risk talent
- Assess relationships with third parties, suppliers, and service providers
- Plan/test business continuity and participate in disaster recovery exercises

> Have a procedure, somebody has to do it
> - cyberthreat intelligence


### Owners and Key Activities of the Third Line of Defense
- Internal audit function assesses whether IT governance supports organisation‘s strategies and objectives
- Coordinates with second LoD, particularly cybersecurity function
- Can be consulted regarding:
  - The relationship between cybersecurity and organisational risk
  - Prioritizing responses and control activities
  - Auditing for cybersecurity risk mitigation across all relevant facets (e.g., privileged access)
  - Assurance in remediation activities
  - Raising risk awareness and coordinating with cybersecurity risk management
  - Validating that cybersecurity provisions are included in the organisation‘s business continuity plans

> EY, KPMG etc. do internal audits
> - remediation, come into check you have followed process correctly

### Common Third Line of Defense Activities
- Provide independent ongoing evaluations of preventive/detective measures related to cybersecurity
- Evaluate IT assets of users with privileged access for standard security configurations
- Track diligence of remediation
- Conduct cyber risk assessments of service organisations, third parties, and suppliers

### General 3LoD

![alt text](assets\IMG46.PNG)

Problem: Senior management and board of directors are not considered to be a part of a defense line

> Come up with 5 lines of assurance model

### Overview of Five Lines of Assurance Model (5LoA)

![alt text](assets\IMG47.PNG)

> defense has changed to 'assurance'
> - defense has a negative stereotype
>   - often seen as the office of 'no'
>
>  Board also has the responsibility of assessing the risk status

### Overview of Five Lines of Assurance Model (5LoA)
- The word "defense" has a sort of negative feel to it. Risk managers are often seen as the "office of 
no" but risk avoidance as we will see is only one form of treating risk
- So moving away from this negative stereotype the people who promoted this model, wanted the risk 
management unit to be seen as a function that has potential to help management to increase the 
certainty that key objectives in an organisations will be obtained, while still operating within an 
acceptable level of risk. So here it is about assurance, about value-creation objectives rather than 
preventing value erosion
- How to make sure value is created with appropriate risk levels rather than focusing on avoiding risks 
at all costs
So, the 5LoA model significantly elevates two roles. The role of CEOs and the 
role of the Boards of Directors in risk governance - the C-Suite (everyone with a 
C or Chief in the title, e.g. CIO, CISO, CRO etc.

### Core Elements of 5LoA
- Uses an "objectives register" as a foundation (see figure below)
- Clear accountability on who is responsible for reporting on residual risk status
- Risk assessment rigour and independent assurance requirements defined by C-suite and the board

![alt text](assets\IMG48.PNG)

> - some companies use a risk register


### Core elements of 4LoA
Active board/senior management involvement and clarity around 
their responsibility as the “ultimate line of defence“

- Requires the full range of risk treatments* be identified and 
assessed not just “internal controls“

![alt text](assets\IMG49.PNG)

> - put the penalty is they don't perform

- Primary focus is on the acceptability of residual risk status
- Specific consideration whether risk treatments are optimized

![alt text](assets\IMG50.PNG)

