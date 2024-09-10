# Module 3 - Multiple relation SQL queries

### Renaming
- SQL provides the facility to rename attribute and/or table names.
- Renaming assists in removing ambiguity and specifying self-joins.
Two options:
1. Qualifying attribute names
2. Declaring an alias

![alt text](assets\IMG68.PNG)

### Cartesian Product

**Also known as a CROSS JOIN**
- R1 X R2: every row in R1 is combined with every row in R2 to form tuples in the result relation
- The schema of R1 X R2 is the concatenation of all the columns from R1 and all the columns from R2

![alt text](assets\IMG69.PNG)

### Joins
- A join is used to combine related tuples from two relations into a single tuple in a new (result) relation

**Example**

A few weeks ago we had an Example ER model like this:

Focus on ``EMPLOYEE`` and ``DEPARTMENT``, and the ``MANAGES`` relationship


![alt text](assets\IMG67.PNG)

There two relationships were mapped as such:


- EMPLOYEE {<u>SSN</u>, Address, Fname, MIt, Lname, Sex, Salary, DOB, SupervisorSSN}
- DEPARTMENT {<u>DNumber</u>, DName, ManagementStartDate, mgrSSN}
  - DEPARTMENT mgrSSN references EMPLOYEE.SSN

I know:
  - For every Department, there is exactly one Employee that manages it

How can I connect both of these relations (tables) into one long table so that I can see the department and its respective Employee?


### Equi-joins in SQL - Examples

```SQL
-- Equi-join using WHERE
SELECT E.name, D.dName
FROM Department AS D, Employee AS E
WHERE D.mgrSSN = E.ssn;

-- Equi-join using JOIN
SELECT E.name, D.dName
FROM  Department AS D
JOIN Employee AS E ON  D.mgrSSN = E.ssn
```

---
### Theta join 

- We join two tables together my satisfying some logical condition
- The most general type of join is called theta-join

$$ \theta \in \{ =, \ne,  <, >, \ge, \le \}$$
---

### INNER and OUTER joins

- **Inner Join:** A tuple is included in the result relation only if matching tuples exist in both relations. By default, just using the JOIN key word will specify INNER JOIN
> - We should still aim to write INNER JOIN instead of JOIN even though the functuonality is the same. Why?


- **Outer Join:** includes the result of the inner join plus unmatched rows in one or both tables can be returned.
  - Left Join: Includes all rows from first table
  - Right Join: Includes all rows from second table
  - Full Outer Join: Includes all rows from both tables

> - Some DBMS (SQLLite) do not have support for a RIGHT JOIN. Why?


![alt text](assets\IMG70.PNG)

> MYSQL does not support ``FULL OUTER JOIN`` operations. How would we achieve the same result without the operation?
>
> ```SQL
> SELECT * FROM t1
> LEFT JOIN t2 ON t1.id = t2.id
> UNION
> SELECT * FROM t1
> RIGHT JOIN t2 ON t1.id = t2.id
> ```
---

## Set operations
- Union
- Intersection
- Difference/Minus


![alt text](assets\IMG71.PNG)

### Use of ALL
Each *automatically eliminates duplicates*; 
- To retain all duplicates use the corresponding multiset versions:
  - UNION ``ALL``, INTERSECT ``ALL`` and EXCEPT ``ALL``.

### UNION

- Produces a relation that includes all tuples that appear only in R1, **or** only in R2, **or in both R1 and R2**.

```SQL
SELECT  starID
FROM  Movie M
JOIN StarsIn S 
ON M.movieID = S.movieID
WHERE year = 1944
UNION
SELECT  starID
FROM  Movie M
JOIN StarsIn S 
ON M.movieID = S.movieID
WHERE year = 1974
```

### INTERSECTION

- Produces a relation that includes the tuples that 
appear in both R1 and R2.

Example: Find IDs of MovieStars who’ve been in a movie in 1944 **and** 1974.

```SQL
SELECT  starID
FROM  Movie M
JOIN StarsIn S 
ON M.movieID = S.movieID
WHERE year = 1944
INTERSECT
SELECT  starID
FROM  Movie M
JOIN StarsIn S 
ON M.movieID = S.movieID
WHERE year = 1974
```

### Difference - EXCEPT/MINUS
- (also referred to as MINUS) produces a relation that includes all the tuples that appear in R1, but do not appear in R2.

Example: Find IDs of stars who have been in a movie in 1944 **but not** in 1974.

```SQL
SELECT   starID
FROM     Movie M
JOIN StarsIn S ON M.movieID = S.movieID
WHERE year = 1944
EXCEPT
SELECT   starID
FROM     Movie M
JOIN StarsIn S ON M.movieID = S.movieID
WHERE year = 1974
```
