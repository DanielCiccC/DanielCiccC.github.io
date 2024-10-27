# Lecture 12

### Security Audit and testing
- A security audit is a crucial type of evaluation to avoid a data breach
- Auditing a computer system involves checking to see how its operation has met security goals
- Audit tests may be manual or automated
  -  Manual tests include interviewing your staff, performing vulnerability scans, reviewing application 
and OS access controls, analyzing physical access to the systems etc. 
  -  With automated tests the auditing software creates a report of any changes to important files and 
settings. 
- Before you can determine whether something has worked, you must first define how it‘s supposed to 
work, you need to create the policies and procedures that establish the rules and requirements of the 
system
  -  Known as assessing a system

> - compare system to baseline expectations

## Security Auditing

Are security policies sound and appropriate for the business or activity? 
Are there controls supporting your policies? 

Is there effective implementation and  upkeep of controls?

> - Conduct an audit, asking the question are you policies understood and followed?
> - Cannot justify a control/policy, should probably remove it
>   - As the organisation evolve/threat mature, make sure controls are ready to face the risks today


![alt text](assets\IMG184.PNG)

> - Make sure not hindering staff and jobs
> - monitoring review and measuring controls, auditing logs for independent analysis later
> - Complaints surfaces, or incidents, check the log
>   - Auditor will check logs for activity
> - Pauses to check security program
> - Auditor Summarises findings

### Determining What is Acceptable
- Define acceptable and unacceptable actions in security policies
- Create standards based on those developed or endorsed by standards bodies
- Communications and other actions permitted by a policy document are acceptable
- Communications and other actions specifically banned in your security policy are unacceptable
- Any action that may reveal confidential information, cause damage to a system‘s integrity, or make the system 
unavailable is also unacceptable, even if the policy does not specifically ban it


**Permission Levels**
- Promiscuous — Everything is allowed (home users)
- Permissive — Anything not specifically prohibited is allowed (public Internet sites, some schools and 
libraries, and many training centers)
- Prudent — A reasonable list of things is permitted; all others are prohibited (most businesses)
- Paranoid — Very few things are permitted; all others are prohibited and carefully monitored (secure facilities)


> - Might create standards 
> - User's might bypass security levels if they are unnecessary

### Types of Security Audits
![alt text](assets\IMG185.PNG)

- Large in scope and cover entire departments or business functions
- Narrow and address only one specific system or control

> - Can have a one-time assessment
>   - Might be triggered by something in operations
>   - new application released, new risks you might expose yourself to
>
> Tollgate
> - Audit will pass or fail
> - go or no-go, new procedure can be imtrduced to your environment
>
> Portfolio
> - 

### Purpose of Security Audits
An audit gives you the opportunity to review your risk management program and to confirm that the program 
has correctly identified and reduced (or otherwise addressed) the risks to your organisation.

Appropriateness of controls
- Is the level of security control suitable for the risk it addresses?

Correct installation of controls
- Is the security control in the right place and working well?

Address purpose of controls
- Is the security control effective in addressing the risk it was designed to address?


### Service Organisational Control (SOC) Reports
The American Institute of Certified Public Accountants has recognized the increased complexities of service 
organisations (such as cloud service providers) and created three different levels of audit reporting for service 
organisations. The Service Organisation Control (SOC) framework defines the scope and contents of three 
levels of audit reports.

![alt text](assets\IMG187.PNG)

> - Important tools for an organisation's auditor
> - Type or report is used to prepare financial statements 
> - SOC2 and 3 are security-related controls
>   - audience is the main difference between these two

### Planning the Audit

![alt text](assets\IMG188.PNG)

> - Who will participate in the audit?
> - Need help to access the documents
> - people will gather/put together the information that the auditor needs
>   - Auditors look at previous audits, to get familar with past issues
>     - might not to be unbiased

### Defining the Scope of the Plan

- Survey the site(s)
- Review documentation
- Review risk analysis output
- Review server and application logs
- Review incident logs
- Review results of penetration tests

> Review risk analysis
> - Risk criticality ratings
> - finish final report, rank systems order
> 
> Review the server and application 
> - Changes in configurations, etc.
>
> Pen test
> - make sure the vulnerabilities in the report are properly addressed
> - NMAP - might find somethng that is hanging off your network

### Benchmarks for Audits

Benchmark – The standard to which your system is
compared to determine whether it is securely configured
- ISO 27002
- NIST Cybersecurity Framework (CSF)
- ITIL
- COBIT
- COSO

ITIL: Information Technology Infrastructure Library
COBIT: Control Objectives for Information and related Technology
COSO: Committee of Sponsoring Organizations of the Treadway Commission

- ISO 27002 — We have run into this one before. ISO 27002 is a best-practices document that gives good 
guidelines for information security management. For an organisation to claim compliance, it must perform an 
audit to verify that all provisions are satisfied. ISO 27002 is part of a growing suite of standards, the ISO 27000 
series, that defines information security standards.

- NIST Cybersecurity Framework (CSF) —NIST CSF, first released in 2014, is a response to a U.S. 
Presidential Executive Order calling for increased cybersecurity. It focuses on critical infrastructure components 
but is applicable to many general systems. The road map provides a structured method to securing systems 
that can help auditors align business drivers and security requirements. NIST also publishes a series of special 
publications that cover many aspects of information systems. For example, NIST SP 800-37 is a standard that 
describes best practices, including auditing, for U.S. government information systems.

- ITIL (Information Technology Infrastructure Library) —This is a set of concepts and policies for managing 
IT infrastructure, development, and operations. ITIL is published in a series of books, each covering a separate 
IT management topic. ITIL gives a detailed description of a number of important IT practices, with 
comprehensive checklists, tasks, and procedures that any IT organisation can tailor to its needs. 


> NIST
> - response to executive order for more cybersecurity
> - Generally applicable to many systems

### The COSO ERM Framework

![alt text](assets\IMG189.PNG)

- a Control Environment — Does the board understand the organisation’s cyber 
risk profile and are they informed of how the organisation is managing the 
evolving cyber risks management faces? 
- b Risk Assessment — Has the organisation and its critical stakeholders evaluated 
its operations, reporting and compliance objectives, and gathered information to 
understand how cyber risk could impact such objectives? 
- c Control Activities — Has the entity developed control activities, including 
general control activities over technology that enable the organisation to manage 
cyber risk within the acceptable level of tolerance to the organisation? Have such 
control activities been deployed through formalized policies and procedures? 
- d Information and Communication — Has the organisation identified information 
requirements to manage internal control over cyber risk? Has the organisation 
defined internal and external communication channels and protocols that support 
the functioning of internal control? How will the organisation respond to, manage, 
and communicate a cyber risk event?
- e Monitoring Activities — How will the organisation select, develop, and perform 
evaluations to ascertain the design and operating effectiveness of internal 
controls that address cyber risks? When deficiencies are identified how are these 
deficiencies communicated and prioritized for corrective action? What is the 
organisation doing to monitor their cyber risk profile?

Summary: The COSO Enterprise risk management (ERM) framework calls on the Internal Audit Function to assist management 
and the board of directors and its audit committee by examining, evaluating, reporting on and recommending improvements to 
the adequacy and effectiveness of the entity’s ERM process. 

> How does it help an internal audit?
> - guide the internal audit approach
>   - Better communicate business objectives

### Audit Data Collection Methods
- Questionnaires Interviews Observation
- Checklists
- Reviewing  documentation
- Reviewing configurations
- Reviewing policy
- Performance security testing


> - Before you can analyse the data, identify and collect the data
> - By observing people, you find you whether you are doing it as prescribed or not
> - do pen testing yourself as an auditor
>   - find out vulnerabilities in the system

### Areas included in Audit Plan

![alt text](assets\IMG190.PNG)
![alt text](assets\IMG191.PNG)

> - IDS - host and network
>   - can check for malicious/modified files
>   - Check if the OS is the same as it always was
> - Check for open ports
>   - NMAP
> - need to see where keys are held
> - where to put the keys securely on computer
> - Something bad happens, data breach or security attack
> - Physical locking of data
> 

### Control Checks and Identity Management

It is important to ensure that your security controls are effective, reliable, and functioning as you intended. Without monitoring and reviewing, you have no assurance that your information security program is effective or that personnel are exercising due diligence. When auditing an identity management system, you should focus on these key areas: 

- Approval process: who grants approval for access requests?
- Authentication mechanisms: What mechanisms are used for specific security requirements?
- Password policy and enforcement: Is there an effective password policy and is it uniformly enforced?
- Monitoring: does the organisation have sufficient monitoring systems to detect unauthorized access?
- Remote access systems: are all systems properly secured with strong authentication?


### Post-Audit activities
- Exit interview
- Data analysis
- Generation of audit report
  - Findings
  - Recommendations
  - Timeline for implementation
  - Level of risk
  - Management response
  - Follow-up
- Presentation of findings
  - Might lead to changes based on regulatory requirements or available budget.

> - still more to do for the auditor
>   - Generation of the audit report
>   - done by the auditor by key personnel
> - Should alert big risks immediately
>
> Each recommendation should have a recommended deadline
> - No point of having a task without a deadline
> - Timeline for implementation of recommendations
> - Level of risk from each finding
>   - Reputation, money loss
>
> Give management an opportunity to respond to audit
> - include action plans for completing the report
>   - should have a follow-up audit
>
> Present findings
> - Someone in the organisation has to read the report


### Example Security Audit Report: Passwords

![alt text](assets\IMG192.PNG)

## Part 2: Security Testing

![alt text](assets\IMG193.PNG)

> - Securing the environment is difficult
> - Two of the most common risk
>   - Attackers who come in from the outside
>   - People who come in from the inside with passwords using social engineering


![alt text](assets\IMG194.PNG)

> - point of testing is to identify new vulnerabilities
> - Policy and regulation also mandate tests
>   - When should a test automatically be triggered?
> - PCI DSS
> - New threats that become more common

### Security testing road map

![alt text](assets\IMG195.PNG)

> - Public resources for the job 
>
> Network Mapping
> - Using of Proxies and VPN's - hide as much as possible to the outside of your network
> - 

### Establishing Testing Goals and Reconnaissance Methods
- Establish testing goals
  - Identify vulnerabilities and rank them according to how critical they are to your systems
  - Document a point-in-time (snapshot) test for comparison to other time periods
  - Prepare for auditor review
  - Find the gaps in your security
- Reconnaissance methods
  - Social engineering
  - Whois service
  - Zone transfer

> - Are the controls addressing the vulnerabilities
>   - Rank them according to how critical they are
> - Security controls are working properly
> - Auditor review
>   - Enables IT staff to tune and test their own procedures, using their own vulnerability analysis and preparation for the real audit
>
> Whois service
> - names and phone numbers of administrators

![alt text](assets\IMG196.PNG)

> - IP address as well as other details, DNS

**Social Engineering**

- free websites to use to see if employees are clicking on websites


![alt text](assets\IMG197.PNG)

### Reconnaissance method: Social engineering

![alt text](assets\IMG198.PNG)

> - Click on a link or download an attachment
>   - strategies that are more likely to get a victim to click on a link

### Which influence Technique was used?

![alt text](assets\IMG199.PNG)

![alt text](assets\IMG200.PNG)

![alt text](assets\IMG201.PNG)

![alt text](assets\IMG202.PNG)

![alt text](assets\IMG203.PNG)

![alt text](assets\IMG204.PNG)

### Testing methods

Black-box testing
- Uses test methods that aren‘t based directly on 
knowlege of a program‘s architecture or design

White-box testing
- Is based on knowledge of the application‘s
design and source code

Grey-box testing
- Lies somewhere between black-box testing
and white-box testing

> - need someone else to test it
> 

![alt text](assets\IMG205.PNG)

> - Covert tester - authorised but IT doesn't know
>   - Doing under instruction of management
>   - Like Mystery customers


## Pentest software 
> - to analyse software

![alt text](assets\IMG206.PNG)

![alt text](assets\IMG207.PNG)

> - Report created looks like above

### Security Metrics (measuring performance)

![alt text](assets\IMG208.PNG)

> - Systems and internal control, continuously monitor

### Examples of Security Performance Metrics
- Percentage (%) of system users/security personnel that have received basic awareness training 
- Average frequency of audit records review and analyses for inappropriate activity
- Percentage of systems using automated mechanisms to conduct analysis and reporting of inappropriate 
activities 
- Percentage (%) of systems that are compliant with the baseline configuration 
- Percentage (%) of systems successfully addressed in the testing of the contingency plan
- Percentage of accounts not associated with specific users 
- Percentage (%) of system components that undergo maintenance on schedule 
- Cost of information security incidents of unauthorized access to information systems, due to physical 
security failures
- Percentage (%) of employees who signed acknowledgement that they have read and understood rules 
of behavior, before being authorized access to the information system 


### Example: Deloitte‘s Cyber Risk Assessment Approach

![alt text](assets\IMG209.PNG)

> - Risk assessment - covered in seminars is being used in practise

![alt text](assets\IMG210.PNG)

![alt text](assets\IMG211.PNG)

> - Scorecards can support the overall maturity assessment with details cyber risks for people process and technology