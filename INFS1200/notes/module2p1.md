# Module 2 part 1: The Relational Data Model

## The relational model

### Relations:
- is a set of records
- is similar to a table with columns and rows

**Relations are not tables**
- Every relation is a table
- Not every table is a relation!

Relations have specific properties, based on the mathematical set theory

![alt text](assets\IMG29.PNG)


### Relation Components:
![alt text](assets\IMG30.PNG)

|**Component type** | **Example and description**
| --- | ---
| **Domain Types** | A domain D is a set of atomic values. An atomic value is indivisible (as far as the relational data model is concerned) <br> <br> Examples: <br> <br> - Integers <br> - Numbers and currency <br> - Fixed or variable length character strings <br> - Date, timestamp <br> - Sub-range from a data type  <br>  - e.g.,1 £ grade £ 7 <br> - Enumerated data type  <br> - e.g.  Gender in {‘Male’, ‘Female’, ‘Other’} <br> - Australian telephone numbers <br> - Format: the digits “61” followed by 9 digits 0 - 9 <br> - Car registration numbers <br>  - Format: 6 characters (either alpha or digits but no ‘Q’s allowed)
|**Attributes** | Each attribute $A$ is the name of a role played by some domain $D$ in the relation named $R$. <br> The number of attributes in a relation $R$ is called the degree of $R$ <br> <br>  Example: salary is an attribute name <br> ![alt text](assets\IMG31.PNG)
|**Tuples** | Each tuple t is an ordered list of n values: <br>$t = <v_{1}, v_{2}, ... v_{n}>$ <br> where each value $v_{i}(1\le i \le n)$ is an element of the corresponding domain of attribute A i or a special value called “NULL”

### Domain attribute restrictions:
- Same attribute name does not necessarily imply same domain
- Different attribute name does not necessarily imply different domain


### Relation Schema and Instance
#### Relation Schema
- Denoted by $R[A_{1}, A_{2}, ..., A_{n}]$, includes a relation name $R$ and list of 
attributes $A_{1}, A_{2}, ..., A_{n}$
- Integer n is termed “degree of the relation” 
- A relation schema of degree 5
  - Employee [ <ins>id</ins>, name, sex, salary, department]
#### Relation Instance
- A relation instance r of the relation schema $R$, denoted by $r(R)$, is a set 
of n-tuples $r = t_{1}, t_{2}, ..., t_{m}$

**Relation Schema** | **Relation Instance**
| --- | --- 
| ![alt text](assets\IMG32.PNG) | ![alt text](assets\IMG33.PNG)


### Primary Keys
- A key is a minimal set of attributes that uniquely identify tuples in a relation. 
  - The term minimal does not mean the smallest set of attributes but instead a set of attributes without any redundant attributes.

A schema may have more than one key
- Each is called a candidate key
- A primary key is candidate key chosen as main key for relation, which would be underlined.

### Foreign Keys
To preserve relationships, you may need to create a foreign key (FK). A foreign key is a primary key from one table placed into another table. 
- This can be viewed graphically or textually.

![alt text](assets\IMG34.PNG)

**Example**
- Let $FK$ be a set of attributes in $R1$ and let $PK$ be the primary attributes in $R2$
- $FK$ in $R1$ is a foreign key referencing $PK$ in $R2$ if
  - $FK$ and $PK$ have the same domain, and 
  - For any tuple $t_{1}$ in $R1$, either $t_{1} [FK]$ is null; or there exists a tuple $t_{2}$ in $R2$, 
such that $t_{1}[FK] = t_{2}[PK]$

THIS MEANS
- The attributes from the foreign key have the same domain as the primary key
- the values from the foriegn key exist in the primary key, **or IT IS NULL**

![alt text](assets\IMG35.PNG)

---

## Integrity Constraints

### Domain constraint
- A domain constraint violation occurs when an attribute’s value does not appear in the corresponding domain.
![alt text](assets\IMG36.PNG)

### Key constraint
- A key constraint violation occurs when a tuple is inserted or modified such that it has the same key value as another tuple.

![alt text](assets\IMG37.PNG)

### Entity Integrity Constraint
An entity integrity constraint violation occurs when a tuple is inserted or modified such that part of its primary key contains the value NULL.

For primary keys that consists of multiple attributes, no part of the primary key can be null.

![alt text](assets\IMG38.PNG)

### Referential Integrity Constraint
A referential integrity constraint can be utilised to guarantee that a department with department number 2 exists before the “Grace Mills” tuple is stored.

![alt text](assets\IMG39.PNG)

### Semantic Integrity Constraint
Semantic integrity constraints are generally defined by the business or organization during client consultation.

Semantic constraints can be used to enforce organisation policies such as:
- “The salary of an employee should not exceed the employee’s supervisor’s salary”

![alt text](assets\IMG40.PNG)

---

### Constraints and Operations
Enforcement of integrity constraints ensures that the database remains consistent.

Changes to the database such as **insert**, **modification** and **deletion** must not violate integrity constraints (leave the database in an inconsistent state).

If a database update is submitted to the DBMS that would violate integrity, **it must be rejected**.
