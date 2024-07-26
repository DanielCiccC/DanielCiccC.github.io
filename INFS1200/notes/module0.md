# Module 0 - Introduction   

## What is a database?
A database is a collection of related data or 
known facts that:
- represents some aspect of the real world, sometimes called the mini-world or the **universe of discourse (UoD)**.
- is a **logically coherent** collection of data with some **inherent meaning**. 
- is designed, built, and populated with data for a specific purpose for an intended group of users and some preconceived applications.

### What is a Database Management System (DBMS)?
A software system that facilitates the processes of:
- Defining a database includes specifying the types, structures, and constraints for the data
- Constructing the database is the process of storing the data on some storage medium that is controlled by the DBMS.
- Manipulating a database includes functions such as querying the database to retrieve specific data, updating the database to reflect changes in the miniworld, and generating reports from the data.
- Sharing a database allows multiple users and programs to access the
database simultaneously. 

### Components
From bottom to top:
1. The Database, the physical storage of data
2. The DBMS - the systems responsible for the definition, construction and manipulation of the Database
3. Applications and user views of data, either through the DBMS interface or
through application programs

![Alt text](assets\IMG1.PNG)

### UoD


### Features of a DBMS:
- Data Integrity Maintenance
    - DBMS has the capability to define and enforce integrity constraints
- Query Processing
  - A DBMS is equipped with a programming language to run queries and return data. 

```SQL
SELECT * 
FROM ProductVersion
WHERE 1=1
AND CODE LIKE '%MotorMachine%'
AND isLatest = 1
```
- Security Management
  - DBMS's provide various measures for securing databases against a variety of threats.
- Concurrency Control   
  - DBMS utilises control protocols to handle concurrent access to data
files that guarantee serialisability (think like google docs)
- Backup and Recovery
  - DBMS provides facility to recover from hardware and software failures
through its backup and recovery sub-system
```SQL

BEGIN TRANSACTION
GO

CREATE TRIGGER [IncrementPolicyVersionId]...
```

## Three schema architecture - see also [Javapoint.com](https://www.javatpoint.com/dbms-three-schema-architecture)
- External Level: provides access to particular parts of the database to users
- Conceptual Level: describes the structure of the whole database for a community of users.
- Internal Level: describes the physical storage structure of the database

---

**Logical Data Independence:** Ability to change the conceptual schema without changing external views or applications

**Physical Data Independence:** Ability to modify physical schema w/o changing conceptual schema