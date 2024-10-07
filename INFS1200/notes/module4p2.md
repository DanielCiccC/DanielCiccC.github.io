# Normalisation

### Key concepts
**Superkey**: a set of attributes such that no two tuples have the same values
for these attributes
- That is, its closure contains all attributes in the relation

**(Candidate) key:** a minimal superkey where non of the attributes can be
removed to create another superkey.
- Minimal ≠ shortest
- There can be many candidate keys for one relation
- Any superkey must contain at least one candidate key

**Primary key:** one of the selected candidate keys
- There can be only one primary key for a relation

**Prime attribute:** an attribute in any candidate key
- Not necessarily a member of the primary key!

**Non-prime attribute:** An attribute that is not a member of any candidate key

### Normalization: the process of identifying redundancy from data

Normalization is a process that aims at achieving better designed relational database schemas using
- Functional Dependencies
- Primary Keys
The normalization process takes a relational schema through a series of tests to certify whether it satisfies certain conditions
- The schemas that satisfy certain conditions are said to be in a given Normal Form
- Unsatisfactory schemas are decomposed by breaking up their attributes into smaller relations that possess desirable properties (e.g., no anomalies) 


Normalisation Overview
**Form** | **Description** |
| --- | --- |
|**1NF** | **Outcome**: Identifying non-atomic values from relations. <br> **Test**: Relation should have no multivalued attributes or nested relations.
| **2NF** | **Outcome**: Identifying partial dependencies, which helps remove some anomalies. **Test**: LHS of any non-trivial FD in F+ is not a proper subset of a candidate key, or RHS is a prime attribute
| **3NF** | **Outcome**: Identifying partial and transitive dependencies, which helps remove most anomalies **Test**: LHS of any non-trivial FD in F+ is a superkey, or RHS is a prime attribute. |
| **BCNF** | **Outcome**: Identifying all anomalies at the cost of not preserving all FDs**Test**: LHS of any non-trivial FD in F+ is a superkey.

### 1NF

- The value of an attribute is a single value from the domain of that attribute
- 1NF disallows having a set of values, a tuple of values (nested attributes), or a combination of both

**Non-1NF relations** | **Normalised to 1NF**
| --- | --- | 
![alt text](assets\IMG97.PNG) | ![alt text](assets\IMG98.PNG)


### 2NF
A relation schema R is in 2NF if every non-prime attribute A in R is fully functionally dependent on the primary key of R.
- 2NF can be said informally to have no partial dependency 

![alt text](assets\IMG99.PNG)


**More Formally**

![alt text](assets\IMG100.PNG)

### 3NF

![alt text](assets\IMG101.PNG)

![alt text](assets\IMG102.PNG)

In other words, a relation is in 3NF iff for any non-trivial FD X $\rightarrow$ A, where A is a non-prime attribute, X must be a superkey


### BCNF (Boyce-Codd Normal Form)

![alt text](assets\IMG103.PNG)

**Informally**: Whenever a set of attributes of R determine another attribute, it should determine all the attributes of R.


![alt text](assets\IMG104.PNG)

## Relational Database Schema Design

![alt text](assets\IMG105.PNG)

---

### BCNF synthesis

![alt text](assets\IMG106.PNG)


### 3NF synthesis

![alt text](assets\IMG107.PNG)


**Finding minimal cover:**
![alt text](assets\IMG108.PNG)

![alt text](assets\IMG109.PNG)

**Synthesis**
![alt text](assets\IMG110.PNG)