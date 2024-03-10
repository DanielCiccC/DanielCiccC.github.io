# Practical 3

Employee [ <ins>id</ins>, firstName, lastName, role]

Project [ <ins>name</ins>, description, funding, projectLeader]

TimeLog [ <ins>employeeID</ins>, projectName, date, hoursWorked, approved]

- Project.projectLeader references Employee.id
- TimeLog.employeeID references Employee.id
- TimeLog.projectName references Project.name

![alt text](assets\IMG41.PNG)

---

## Section A: Identifying Keys

|**Attribute Type** | **Answer**
| --- | ---
| A minimal key |
| A foreign key |


## Section B : Integrity Constraints


### **Operation 1**

Update the tuple (“Website Setup”, “Get a functional website setup”,
12000, 2019) to (“Website Setup”, “Get a functional website setup”,
20000, 1919) in the relation “Project”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | 
| IF YES <br> Type of constraint violated | 
| IF YES <br> Description of violation | 

### Operation 2
Insert the tuple (2014, “Rebecca”, “Zhang”, “Administration”) in the
relation “Employee”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | 
| IF YES <br> Type of constraint violated | 
| IF YES <br> Description of violation | 

### Operation 3
Update the tuple (2020, “2020 Marketing”, 2/1/2020, 5, true) to
(1919, “Overall Marketing”, 2/1/2020, 5, true) in the relation
“TimeLog”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | 
| IF YES <br> Type of constraint violated | 
| IF YES <br> Description of violation | 

### Operation 4
Insert the tuple (, “Test”, “Test”, “Test”) in the relation “Employee”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | 
| IF YES <br> Type of constraint violated | 
| IF YES <br> Description of violation | 

### Operation 5
Delete the tuple (2014, “Daniel”, “Johnson”, “Administration”) in the
relation “Employee”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | 
| IF YES <br> Type of constraint violated | 
| IF YES <br> Description of violation | 

### Operation 6
Insert the tuple (“Talent Recruitment Initiative”, “Get the best and
brightest UQ graduates to work for us!”, 10000, 2014) in the relation
“Project”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | 
| IF YES <br> Type of constraint violated | 
| IF YES <br> Description of violation | 
