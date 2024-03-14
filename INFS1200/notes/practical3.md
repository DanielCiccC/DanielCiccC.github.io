# Practical 3

Employee [ <ins>id</ins>, firstName, lastName, role]

Project [ <ins>name</ins>, description, funding, projectLeader]

TimeLog [ <ins>employeeID, projectName, date</ins>, hoursWorked, approved]

- Project.projectLeader references Employee.id
- TimeLog.employeeID references Employee.id
- TimeLog.projectName references Project.name

#### Semantic constraints
- In addition to this, I thought I’d just mention that in accordance
with company policy, the system does not allow administration staff to be project leaders.


![alt text](assets\IMG41.PNG)

---

## Section A: Identifying Keys

|**Attribute Type** | **Answer**
| --- | ---
| A minimal key | Employee.ID, Project.Name, TimeLog.(employeeID, projectName, date)
| A foreign key |


## Section B : Integrity Constraints


### **Operation 1**

Update the tuple (“Website Setup”, “Get a functional website setup”,
12000, 2019) to (“Website Setup”, “Get a functional website setup”,
20000, 1919) in the relation “Project”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | no
| IF YES <br> Type of constraint violated | 
| IF YES <br> Description of violation | 

### Operation 2
Insert the tuple (2014, “Rebecca”, “Zhang”, “Administration”) in the
relation “Employee”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | yes
| IF YES <br> Type of constraint violated | Key Constraint
| IF YES <br> Description of violation | PK for "employee" is ID, and a tuple with ID = 2014 already exists in the database. Therefore, it will fail because it does not have a unique primary key

### Operation 3
Update the tuple (2020, “2020 Marketing”, 2/1/2020, 5, true) to
(1919, “Overall Marketing”, 2/1/2020, 5, true) in the relation
“TimeLog”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | yes
| IF YES <br> Type of constraint violated | Referential Integrity constraint
| IF YES <br> Description of violation | projectName attribute in TimeLog references the project name in Project. "Overall Marketing" does not exist in the "Project" table and this is an invalid foreign key.

### Operation 4
Insert the tuple (, “Test”, “Test”, “Test”) in the relation “Employee”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | Yes
| IF YES <br> Type of constraint violated | Entity Integrity Constraint
| IF YES <br> Description of violation | Each tuple in a databae must have a non-null primary key. The primary key for the "Employee" relation is id, however, no id is provided in the insertion operation.

### Operation 5
Delete the tuple (2014, “Daniel”, “Johnson”, “Administration”) in the
relation “Employee”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | yes
| IF YES <br> Type of constraint violated | Referential integrity Constraint
| IF YES <br> Description of violation | employee ID attribute in the "TimeLog" relation is a foreign key which reference the id attribute in the "Employee" relation. Hence, deleting this tuple, would cause a tuple with employeeID 2024 in the timelog "TimeLog" table to have no valid reference. Thus, the operation will fail.

### Operation 6
Insert the tuple (“Talent Recruitment Initiative”, “Get the best and
brightest UQ graduates to work for us!”, 10000, 2014) in the relation
“Project”
|**Operation** | **Answer**
| --- | ---
| Integrity constraint violated? (Write either “yes” or “no”) | yes
| IF YES <br> Type of constraint violated | Semantic constraint
| IF YES <br> Description of violation | The "ProjectLeader" attribute in this insert operation reference an employee who has the role "Administration". Inserting this tuple would violate user defined integrity constraints becuase staff with the role "Administration" cannot be assigned as a "projectLeader". Thus, the operation will fail.