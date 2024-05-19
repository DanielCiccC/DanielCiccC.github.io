# Module 5: Database Security

![alt text](assets\IMG111.PNG)

### Access control mechanisms
Database access control is a method of allowing access to sensitive data only to users who are authorised to access such data and to restrict access to unauthorized persons. It includes two main 
components:

- Authentication: verifying the identity of a person who is accessing 
your database
- Authorization: determining whether a user should be allowed to 
execute the transaction they are attempting.


**User Accounts**
- User must log in using assigned username and password

**Login session**
- Sequence of database operations by a certain user
- Recorded in system log (also used for recovery and other control functions, not just security)

**Database audit**
- Reviewing log to examine all accesses and operations applied during a certain time period

## Access Control Mechanisms

Authorization: determining whether a user should be allowed to execute the transaction they are attempting.

1. **Discretionary Access Control (DAC)**
  - Used to grant privileges to users
2. **Mandatory Access Control (MAC)**
  - Classify data and users into various security classes
  - Implement security policy
3. **Role-based Access Control (RBAC)**
  - Users can be assigned with roles, and then DAC or MAC can be applied


### Discretionary Access Control

Based on Granting and Revoking privileges

![alt text](assets\IMG112.PNG)

**Account level**: privileges specified for each account, independent of relations in the account
- Create schema, create table, create view; alter/drop tables; modify 
(insert, delete, update tuples) and select privileges

### **Relation level**: 
privileges for each relation or view
- Can be specified at attribute level too
- Select (retrieval or read) privilege 
- Modification (insert, deleted and update) privilege 
- References privilege

- Each relation R is assigned an owner account
- Owners can grant (select, modification and references) privileges to other users on any owned relation

![alt text](assets\IMG113.PNG)

### Mandatory Access Control (MAC)
- Classify data and users into various security classes
- Implement security policy

Data and users are associated with security classes
- Typical security classes
  - Top secret (TS)
  - Secret (S)
  - Confidential (C)
  - Unclassified (U)

![alt text](assets\IMG114.PNG)


**Simple Security Property**
- A subject can’t read information from an object that has a higher sensitivity label than the subject 
- Also known as: no read up, or **NRU**

> Example:
> - Database user Cody with access level Unclassified cannot view Smith’s salary which requires Confidential level access
> 
> ![alt text](assets\IMG115.PNG)


- A subject can’t write information to an object that has a lower 
sensitivity label than the subject 
- Also known as: no write down, or **NWD**
- This is to prevent information from flowing from higher to lower 
classifications

> Example:
> - Database user Tanya with access level Secret cannot insert a new tuple with information about Smith with Confidential level access
>
> ![alt text](assets\IMG116.PNG)

### SQL Injection

- The client’s input is directly used in the SQL query
- The SQL query needs to return a tuple in the User table for the client to be authenticated
![alt text](assets\IMG117.PNG)

### Protection Techniques
SQL injection attacks can occur when SQL statements are used in programs

**Bind variables (using parameterized statements)**
- Protects against injection attacks
- Improves performance

**Filtering input (input validation)**
- Remove escape characters from input strings
- Escape characters can be used to inject manipulation attacks

**Function security**
- Standard and custom functions should be restricted

