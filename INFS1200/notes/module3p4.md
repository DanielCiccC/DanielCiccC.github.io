# Module 3 - nested queries and Views

### Nested queries
- A nested query (often termed subquery) is a query that appears within another query

### Non-Correlated queries
- Results are returned from an inner query to an outer clause
- Subqueries are evaluated from the “inside out”

![alt text](assets\IMG72.PNG)


### Correlated Queries
- Conditions in subquery WHERE clause have references to some attributes of 
a relation in the outer query
- The outer SQL statement provides the values for the inner subquery to use in 
its evaluation
- The **subquery is evaluated once for each (combination of) tuple in the outer query**

![alt text](assets\IMG73.PNG)

## Subquery operators

| **Operator** | Description | Example
| --- | --- | ---
``IN`` | Checked for set membership | List the department names for departments which have a manager named “Jennifer”. ![alt text](assets\IMG74.PNG)
|``ANY/ALL``|Compares with the set returned. Operations use operators $<, >, \ge, \le, <>$| ![alt text](assets\IMG75.PNG)
|Single value operators| Expression is compared with the value(s) returned | Find the names and salaries of employees getting the minimum salary. ![alt text](assets\IMG76.PNG)
| ``EXISTS``| Tests the existence of data that meet the criteria of the subquery. EXISTS evaluates to true if the result of the correlated subquery is a non-empty set.| Find movies that were the only movie produced that year. ![alt text](assets\IMG77.PNG)

### Division and problems with the division problem

![alt text](assets\IMG78.PNG)


### Counting
**“Find the movie star(s) who acted in at least all the movies produced in the year 1934.”**

- Count the number of movies in 1934
- Count the number of movies in 1934 that MoviesStart X acted in

![alt text](assets\IMG79.PNG)

**STEP 1:**

![alt text](assets\IMG82.PNG)

**STEP 2:**

![alt text](assets\IMG83.PNG)



### Double negation
**“Find the movie star(s) who acted in at least all the movies produced in the year 1934.”**

1. Find the negation of the statement - in this case, the blue region of the diagram. We want this section to be EMPTY and apply this negation through the use of a ``NOT EXISTS`` operation
2. Use a correlated inner query to compute the result
   - For instances where the blue is NOT NULL (empty) we will *not* return a result
   - For instances where the blue is NULL (and this is where both the green and the red is true) we *will* return a result

**STEP 1:**


![alt text](assets\IMG84.PNG)

**STEP 2:**

![alt text](assets\IMG85.PNG)


## Views

- **Virtual tables** - that do not physically exist on disk. 
- **Materialized** - by physically creating the view table. These must be updated when the base tables are updated


![alt text](assets\IMG80.PNG)

## Dropping views
Dropping a view does not affect any tuples from the underlying relation.

![alt text](assets\IMG81.PNG)