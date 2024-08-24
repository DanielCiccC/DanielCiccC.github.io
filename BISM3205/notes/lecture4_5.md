# Lecture 4 and 5

In the realm of cybersecurity, Governance, Risk Management, and Compliance (GRC) serves as a fundamental 
framework. It guides organizations in implementing robust security measures by integrating critical elements:
- **Governance**: This encompasses policies, rules, and frameworks that align with business goals. It defines 
responsibilities for key stakeholders, such as the board of directors and senior management. Good corporate 
governance includes ethics, accountability, transparent information sharing, conflict resolution policies, and 
resource management.
- **Risk Management**: Businesses face various risks—financial, legal, strategic, and security-related. Proper risk 
management involves identifying these risks and finding ways to mitigate them. For instance, risk assessments 
help uncover security vulnerabilities in computer systems.
- **Compliance**: Compliance involves adhering to rules, laws, and regulations. It applies to both external 
regulations set by industry bodies and internal corporate policies.

**Why is GRC important?** Implementing GRC programs allows businesses to make better decisions in a risk-
aware environment. An effective GRC strategy helps stakeholders set policies, comply with regulations, and 
align the entire company around shared values and actions. Benefits include data-driven decision-making and 
responsible operations.


**Imagine your next professional interview, you have a business degree and the committee asks you:**
**“How would you approach risk management?”**

> - How would you appraoch risk management iff someone approached you in an interview

### Introduction – Overview (1)

Organisations must design and create safe environments in which business processes and procedures can 
function.

**Risk management**: process of identifying and controlling risks facing an organisation – comprises three 
major undertakings:
1. **Risk identification**: process of examining an organisation’s current IT security situation
2. **Risk assessment**: determining the extent to which the assets are exposed or at risk
3. **Risk control**: applying controls to reduce risks to an organisation’s data and information systems

![alt text](assets\IMG51.PNG)

> - Identify assets, laborious process
>   - computers, databases, servers, people
>
> Identify threats
> - What are the attack vectors?
> - large spreadsheets and/or specialised software
>
> Assess the risk
> - is the impact little or big?
> - Likelihood can be put into a risk matrix
> - Frequency and the impact (severity)
>
> Develop mitigation strategies
> - Identify which risk is most important
>
> Implement controls
> - business constantly changing, have to develop mitigation strategies

- Know yourself: identify, examine, and understand the information and systems currently in place
- Know the ‘threats’: identify, examine, and understand the threats facing the organisation
- Responsibility of each community of interest within an organisation to manage the risks that are encountered

![alt text](assets\IMG52.PNG)

> - In general a process business people can perform
> - Work with IT people, because the controls will be IT controls
>
> Risk Identification
> - Classify, value them, prioritise them, etc.
> - might need to work with other peopemin the team
>
> Risk Assessment
> - determine the loss frequency and severity (impact)
> - Create a risk matrix, which will calculate the risk
>   - Prioritise the risk the assets to the highest risk needed to be fixed first
>
> Risk Control
> - Document if a part of the asset cannot be protected
> - monitor

### Risk management discussion point!

- Organisation must define level of risk it can live with (most probably it will never be zero) – Why?
- Risk appetite (aka risk tolerance): Defines quantity and nature of risk that organisations are willing to 
accept as trade-offs between perfect security and unlimited accessibility
- Residual risk: Risk that has not been completely removed, shifted, or planned for

![alt text](assets\IMG53.PNG)

> - Residual risk, that the company is comfortable with
>  - cost too much, not important enough etc.

### Risk identification (we now discuss the overall process)

- Risk management involves identifying, classifying, and prioritising an organisation’s assets
- In risk management, the principle of mutually exclusive and collectively exhaustive (MECE) is 
often applied. This principle ensures that all possible risks are identified (collectively exhaustive) 
and that there is no overlap between the risks (mutually exclusive)
- A threat assessment process identifies and quantifies the risks facing each asset
- Components of risk identification
  - People
  - Procedures
  - Data
  - Software
  - Hardware

> - MECE, only cover the asset once even if used throughout the organisation

### Risk identification – a "project management" approach

![alt text](assets\IMG54.PNG)

- First step in the Risk Identification process is to follow your project management principles
- Begin by organising a team with representation across all affected groups
- The process must then be planned out
  - Periodic deliverables
  - Reviews
  - Presentations to management
- Tasks laid out, assignments made and timetables discussed
- Iterative process!

> - Put a team together
>   - Project controls implemented
>   - Whatever you do is sanctioned by management
> - At milestones, present what you have done to management
>   - Back arrows indicate an iterative process

- Iterative process; begins with identification of assets, including all elements of an organisation’s system 
- Assets are then classified and categorized

![alt text](assets\IMG55.PNG)

### 1. People, procedures, and data asset identification
- Human resources, documentation, and data information assets are more difficult to identify
- Important asset attributes:
  - People: position name/number/ID; supervisor; security clearance level; special skills
  - Procedures: description; intended purpose; what elements it is tied to; storage location for reference; storage location for update
  - Data: classification; owner/creator/ manager; data structure size; data structure used; online/offline; location; backup procedures employed

> - People is more difficult
>   - Logging in, changing password (procedures)
>   - Data that the company owns
>     - Where is it kept, backup procedures in place


### 2. Hardware, software, and network asset identification
- What information attributes to track depends on:
  - Needs of organisation/risk management efforts
  - Preferences/needs of the security and information technology communities
- Asset attributes to be considered are: name; IP address; element type; serial number; manufacturer name; model/part number; software version; physical or logical location; controlling entity
- Automated tools can identify system elements for hardware, software, and network components

### Information asset valuation

So we‘ve succeeded in identifying and we‘re confident we‘ve identified a comprehensive, mutually exlusive list of assets across the various functional areas. Now we have to value each of those assets.

Questions below (and others) help develop criteria for asset valuation 

Which information asset:
- Is most critical to organisation’s success?
- Generates the most revenue/profitability?
- Would be most expensive to replace or protect?
- Would be the most embarrassing or cause greatest liability if revealed?

![alt text](assets\IMG56.PNG)

> - DMZ - demilitarised zone
> - Between the internet and highly secured network

Information asset prioritisation (most likely to have multiple valuation criteria – why? Who makes these criteria?)
- Create weighting for each category based on the answers to questions
- Calculate relative importance of each asset using weighted factor analysis
- List the assets in order of importance using a weighted factor analysis worksheet

![alt text](assets\IMG57.PNG)

> - asset is likely to be attacked
>   - give it high weighting
> The values that the project team, using senior management policy, have allocated to the asset.

### Next step is: Identifying and prioritising threats
-  Realistic threats need investigation; unimportant threats are set aside

- Threat assessment:
  - Which threats present danger to assets?
  - Which threats represent the most danger to information?
  - How much would it cost to recover from attack?
  - Which threat requires greatest expenditure to prevent?

![alt text](assets\IMG58.PNG)


### Then we need to analyse our vulnerabilities and prioritise them: Vulnerability analysis
- Vulnerabilities: specific avenues threat agents can exploit to attack an information asset.
- Examine how each threat could be perpetrated and list organisation’s assets and 
vulnerabilities.
- Process works best when people with diverse backgrounds within organisation work 
iteratively in a series of brainstorming sessions.
- How can we prioritise vulnerabilites?


> - Need people with backgrounds in the area where the assets are used


### Prioritising vulnerabilities

- The Common Vulnerability Scoring System (CVSS) is a free, open industry standard for assessing the severity of computer system security vulnerabilities. 
- CVSS aims to assign severity scores to vulnerabilities, allowing flexibility for responders to prioritize responses and resources according to threat. 
- Scores are calculated based on a formula that depends on several metrics that approximate ease of exploit and the impact of exploit. 
- Scores range from 0 to 10, with 10 being the most severe. 
- Some of the metrics are described in overview below:
- The CVSS describes 6 base metrics: **attack vector** (how exploited), **attack complexity** (easy or difficult), **authentication** (the levels of authentication for the exploit), **confidentiality** (impact on confidentiality of data), **integrity** (of system), **availability** (of system).
- These six metrics are then used to produce a CVSS vector for the vulnerability.

CVSS v4.0: https://www.first.org/cvss/v4.0/specification-document

> - Have a vulnerability score calculator
> - Standard scoring system for vulnerabilities

![alt text](assets\IMG59.PNG)

### TVA worksheet (a simple summary)

At end of risk identification process, 
there should be two lists: 
- list of assets and their vulnerabilities.
- List of threats facing the organisation 
Combination of these two lists into a Threats ‐ Vulnerabilities ‐ Assets (TVA) worksheet

![alt text](assets\IMG60.PNG)

> - Most important asset at the left
> - vulnerability in each cell
> - find measures that reduce the threats

## Risk Assessment

- Risk assessment evaluates the relative risk for each vulnerability
- Assigns a risk rating or score to each information asset(a ‘relative’ meaning – not absolute)
- We must be CONSISTENT whichever approach we use!
- The goal at this point: create a method for evaluating the relative risk of each listed vulnerability
- We shall consider several approaches: (text book, NIST, one selected from industry)


> - Be consistent with the approach

### Risk calculation – a ‘project’ approach (flow, feedback, control)

For the purpose of a simplistic relative risk assessment:
- Risk = Loss frequency * loss magnitude + an element of uncertainty (5-10%)

> - Add a 'fudge' factor

![alt text](assets\IMG61.PNG)

### Calculating risk (text book approach – page 283)

![alt text](assets\IMG62.PNG)

> - Loss - loss magnitude (asset value) * probable loss (how much will you lose)


### Step 1: Loss frequency

First, we need to determine how probable it is that an attack is successful.

**Loss frequency** describes an assessment of the likelihood of an attack combined with expected probability of success given the current level of controls in place
- Likelihood: Use external references for values that have been reviewed/adjusted for your circumstances AND ‘risk actuals’ of your organisation; value subject to uncertainty
  - Assign numeric value to likelihood, typically annual value
  - Targeted by hackers once every five years – annualized likelihood of attack: 1/5, 20 percent
  - Web defacement two times each year – annualized likelihood of attack 200 percent
  - See next slide also
- Success probability: Estimate a quantitative value (e.g., 10 percent) for the likelihood of a successful attack; value subject to uncertainty.  This also involves consideration of the current level of protection – this further complicates the calculation.

> - Come back to a common base line for each asset
> - how many times per year expressed as a %

- The probability that a specific vulnerability will be the object of a successful attack
- NIST SP 800‐30: Assign numeric value: number between 0.1 (low) and 1.0 (high), or a number between 1 and 100
- Zero not used since vulnerabilities with zero likelihood are removed from asset/vulnerability list
- Use selected rating model (whichever is selected) consistently
- Use external references for values that have been reviewed/adjusted for your circumstances – remember our reference to ‘risk actuals’ Likelihood (part of step 1)

> - NIST SP = National Institute of Standards and Technology , SP = Special Publications (on Blackboard)

### Step 2: Loss Magnitude

We need to determine how much of an information asset could be lost in a successful attack

**Loss magnitude** (sometimes asset exposure)

Combines two components: (1) the value of information asset with (2) the percentage of asset lost in the 
event of a successful attack

Difficulties involve:
- Valuing an information asset (e.g. a database server for sales transactions from customers and one for 
employee salary)
- Estimating the percentage of information asset lost during best ‐ case, worst ‐ case, and most likely scenarios

Clearly this step is also subject to possible error/uncertainty

> - Don't put the dollar value of how much this thing costs
>   - How much value it is to the company

**Example in textbook**

Information asset A is on online e ‐ commerce database. 10% chance of attack this year (1 attack every 10 
years). 50% chance of success based on current asset vulnerabilities and protection mechanisms. Asset 
value is 50 (how is this derived) and 100% of the asset would be compromised by a successful attack. 
Assumption: data 90% accurate.

![alt text](assets\IMG63.PNG)

Information asset B is an internal personnel database behind a firewall. 1% chance of attack this year.  10% 
chance of success based on current asset vulnerabilities and protection mechanisms.  Asset value is 25 on a 
scale of 1 to 100 and 50% of the asset would be compromised by a successful attack. Assumption: data 90% 
accurate.

![alt text](assets\IMG64.PNG)

### Risk Assessment (2) - NIST
- NIST SP (Special Publication) 800 ‐ 30 r1 (on Blackboard)
- Definitive document for RISK ASSESSMENT
- RISK = LIKELIHOOD * LEVEL OF IMPACT (appendix I)
- SP800 ‐ 30 contains qualitative and quantitative strategies
- SP800 ‐ 30 is on Blackboard (week 4 material)
- How can risk be ‘so simply’ described (in contrast with the text book)?

### Risk assessment (3) – another approach

- For the purpose of relative risk assessment:
  - Risk EQUALS
  - Likelihood of vulnerability occurrence
  - TIMES value (or impact)
  - MINUS percentage risk already controlled
  - PLUS an element of uncertainty

![alt text](assets\IMG65.PNG)

## Vulnerability Discovery and Recording
> - Reports it to the company
> - Vulnerability code starting with 'CVE-...'

## Identify possible controls

- For each threat and associated vulnerabilities that have residual risk, create preliminary list of 
control ideas
- Residual risk is risk that remains to information asset even after existing control has been 
applied
- There are three general categories of controls:
  - Policies
  - Programs (training, education, security awareness)
  - Technologies (authentication, PW, 2FA)

![alt text](assets\IMG66.PNG)

### Documenting the results of the risk assessment
- Final summary comprised in ranked vulnerability risk worksheet
- Worksheet details asset, asset impact, vulnerability, vulnerability likelihood, and risk ‐ rating factor.

![alt text](assets\IMG67.PNG)

- What is the relative risk of an E-Mail disruption due to hardware failure of a ‘Customer service request (email)’?
- Explain the asset values.

### Risk control strategies (5 of these)
Once ranked vulnerability risk worksheet complete, must choose one of five strategies to control each 
risk:
1. Defend
- Attempts to prevent exploitation of the vulnerability
- Preferred approach
- Accomplished through countering threats, removing asset vulnerabilities, limiting asset access, and 
adding protective safeguards
- Three common methods:
  - Application of policy
  - Training and education
  - Applying technology

> - Training education
> - Apply technology (cannot change pwd to 12345 e.g.)

2. Transfer
- Control approach that attempts to shift risk to other assets, processes, or organisations
- If lacking, organisation should hire individuals/firms that provide security management and administration 
expertise
- Organisation may then transfer risk associated with management of complex systems to another organisation 
experienced in dealing with those risks

> - Transfer the risk to someone else
> - Penalise the company if something goes wrong

3. Mitigate
- Attempts to reduce impact of vulnerability exploitation through planning and preparation
- Approach includes three types of plans
  - Incident response plan (IRP): define the actions to take while incident is in progress
  - Disaster recovery plan (DRP): most common mitigation procedure
  - Business continuity plan (BCP): encompasses continuation of business activities if catastrophic event occurs

4. Accept
- Doing nothing to protect a vulnerability and accepting the outcome of its exploitation
- Valid only when the particular function, service, information, or asset does not justify cost of protection

5. Terminate
- Directs the organisation to avoid those business activities that introduce uncontrollable risks
- May seek an alternate mechanism to meet customer needs

> - Don't do this anymore
> - Kill the area of your business because it is too unsecure

![alt text](assets\IMG68.PNG)


## Selecting a risk control strategy
- Level of threat and value of asset play major role in selection of strategy
- Rules of thumb on strategy selection can be applied:
  - When a vulnerability exists
  - When a vulnerability can be exploited
  - **When attacker’s cost is less than potential gain**
  - When potential loss is substantial

### Justifying controls

- Before implementing one of the control strategies for a specific vulnerability, 
the organisation must explore all consequences of vulnerability to information 
asset.
- There are several ways to determine the advantages/disadvantages of a 
specific control:

> - With some sort of analysis, is it worthwhile implementing this control

### Cost Benefit Analysis

- Sums the benefits of an action THEN subtracts the costs of that action
- Formal process to document this is called cost benefit analysis or economic feasibility study 
- Items that affect cost of a control or safeguard include: cost of development or acquisition; 
training fees; implementation cost; service costs; cost of maintenance
- Benefit: value an organisation realises using controls to prevent losses from a vulnerability
- Asset valuation: process of assigning financial value or worth to each information asset
- Once asset valuation is performed, an organisation can begin to estimate the potential loss that could 
occur from an exploited vulnerability or threat occurrence.

Several questions must be asked:
- What damage would occur from an exploited vulnerability or threat occurrence
- What would it cost to recover from the attack – as well as the financial damage
- What is the single loss expectancy (SLE) for each risk? 
  - SLE = asset value × exposure factor (EF)
  - Example: if a Web site has an estimated value of $1 million, and a hacker defacement could damage 10% of 
the Web site, the SLE is $1 million * 0.10.

Once asset valuation is completed, we can calculate how much loss is expected from a single attack and how 
often these attacks occur. We can use the annualized loss expectancy (ALE) for this:

ALE = single loss expectancy (SLE) × annualized rate of occurrence (ARO)

In our previous Web site example, the ARO could be 0.50 ( how often is this?).  This gives us ALE = $100,000 * 0.50 = $50,000

Consequently, this business can expect to lose $50,000 every year – this gives us a basis for expenditure

> - Hacker could deface 10% of a website


- CBA determines if alternative being evaluated is worth cost incurred to control vulnerability
  - CBA  most  easily  calculated  using  Annualized  Loss  Expectancy  (ALE)  from  earlier 
assessments, before implementation of proposed control:

CBA = ALE(prior) – ALE(post) – ACS 

- ALE(prior) is annualized loss expectancy of 
risk before implementation of control
- ALE(post) is estimated ALE based on control 
being in place for a period of time
- ACS is the annualized cost of the safeguard

### Evaluation, assessment, and maintenance of risk controls
- Selection and implementation of control strategy is not end of process
- Strategy and accompanying controls must be monitored/reevaluated on ongoing basis to determine effectiveness and to calculate more accurately the estimated residual risk
- Process continues as long as organisation continues to function

![alt text](assets\IMG69.PNG)

### Qualitative versus quantitative risk control practices

- Performing the previous steps using actual values or estimates is known as quantitative assessment
- Possible to complete steps using evaluation process based on characteristics using non ‐ numerical measures; called qualitative assessment (low, medium, high, very high)
- Utilizing scales rather than specific estimates relieves organisation from difficulty of determining exact values

![alt text](assets\IMG70.PNG)

> - Can also do this with words, low, medium, high
> - NIST in appendix of likelihood vs impact

### Quantitative methods: Example

FAIR (Factor Analysis of Information Risks)

![alt text](assets\IMG71.PNG)

> - reduce the risk by making the 'rectangle' smaller
