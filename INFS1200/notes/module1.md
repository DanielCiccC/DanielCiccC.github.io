# Module 1 : Entity-Relationship (ER) diagrams

### Conceptual Database Design
-  Identify the “Universe of Discourse” (UoD). The database to be built will not model everything in the world, but rather some “mini-
world” or “Universe of Discourse”.'
- Step 2: Convert the UoD to a data model, which can be captured by a database.

### The Entity - Relationship Model
- The Entity-Relationship (ER) model at its core provides a graphical representation of data entities.

It helps:

- Define constraints in the ER model 
- Gauge how the system works, how various data within the system is connected
- The ER diagram can also be extended to allow for generalisations and specialisations of data to be stored

## Entities

An entity is essentially a physical or conceptual object which has data associated with it.

| Type | Description | Representation
| --- | --- | --- |
| Entity | An entity type provides a format for the data which needs to be recorded to represent a particular entity. The entity type is described by its name and attributes. Represented as a rectangular box | ![Alt text](assets\IMG2.PNG) | 
| Key Attributes| All entity types have at least one key (or uniqueness) constraint. The key must hold for every possible extension of the entity type (see super/subclasses in later slides). Represented as an udnerlined attribute | ![Alt text](assets\IMG3.PNG)
| Simple Attributes | | ![Alt text](assets\IMG4.PNG)
| Composite attributes |Composite attributes can be divided into smaller parts which represent simple attributes with independent meaning.| ![Alt text](assets\IMG5.PNG)
|Composite Key attribute (Several Attribute Keys)| A composite key is combination of simple attributes which make up the composite key that must be unique. |![Alt text](assets\IMG6.PNG)
| Multivalued attrbutes |  Multivalued attributes are shown with double-lined ovals and can have multiple values (e.g., one person can hold multiple degrees) | ![Alt text](assets\IMG7.PNG)
|Derived Attributes|In some cases, attribute values can be derived from related attribute values (e.g., age can be derived from BirthDate).| ![Alt text](assets\IMG8.PNG)
|Weak Entities| Entity types that do not have key attributes of their own are called weak entities. | ![Alt text](assets\IMG9.PNG)

### Entity Concepts
**Value sets of attributes**

Value sets specify the set of values that may be assigned to a particular attribute of an entity 
 - E.g.  employeeAge: integers between 21 & 65
 - A particular entity may not have an applicable value for an attribute. A null value may be used for representing this.

**Entity Set**

The collection of all entities of a particular entity type in the database at any point in time is referred to as an entity set.
 - The entity set can be mapped to a table

![Alt text](assets\IMG10.PNG)

## Relationships
A **relationship** is an association among two or more entities  
-  e.g., Paris Lane works on the project FileZilla 
  
A **relationship type** defines the relationship.
- A relationship type may have descriptive attributes.
- A relationship type may have key attributes

| Relationship concept | Desciption | graphical representation
| --- | --- | --- |
| Relationship | In the ER model, relationships are represented using a diamond that is connected to the associated entity types. A relationship type may have descriptive attributes. A relationship type may have key attributes | ![Alt text](assets\IMG11.PNG)
| Relationship Degree | The degree of a relationship type is the number of participating entity types. 2 Entities: Binary relationship. 3 entities: Ternary relationship. n entities: n-ary relationship (3 + entities) |  ![Alt text](assets\IMG12.PNG)  ![Alt text](assets\IMG13.PNG)
| Entity Roles | The role name signifies the role that a participating entity from the entity type plays in each relationship instance. That is to say, *it explains what the relationship means.* | *WorksOn* ![Alt text](assets\IMG14.PNG)
|Recursive Relatiuonships| Same entity types can participate more than once in the same relationship type under different “roles”. | ![Alt text](assets\IMG15.PNG) 
| Relationship set | The collection of all relationships of a particular relationship type in the database at any point in time is referred to as a relationship set | ![Alt text](assets\IMG16.PNG)

### Relationship Constraints
#### Cardinality Constraints
A cardinality ratio for a relationship set specifies the number of relationships in the set that an entity can participate in.

![Alt text](assets\IMG17.PNG)

Example | Cardinality | representation |
| --- | --- | --- |
“Each employee can work on any number of projects, and each project can have any number of employees working on it.” | Many-To-Many | ![Alt text](assets\IMG18.PNG) 
| “Each department can have any number of employees, but an employee can work for at most one department.”|Many-To-One or One-To-Many | ![Alt text](assets\IMG19.PNG)
|“Each department can have at most one manager and each employee can manage at most one department.”| One-to-One | ![Alt text](assets\IMG20.PNG)

#### Participation constraints

**Existance Dependency**

Existence dependency indicates whether the existence of an entity depends on its relationship to another entity.

Example: Every employee must work for a department. Employee is *existentially dependent* on Department via the WORKSFOR relationship type.

![Alt text](assets\IMG21.PNG)

### Weak Entities

- A weak entity can be identified uniquely only by considering the primary key 
of another owner entity and its own partial key, which is underlined with a 
dotted line.
- The relationship type that relates a weak entity to its owner is called the 
identifying relationship. A weak entity and its identifying relationship are 
represented with double lines.

![Alt text](assets\IMG22.PNG)


### Superclasses and Subclasses
Entities in the same class have the same attributes. Class can be a superclass or subclass
- Attributes of a superclass are inherited by the subclasses
- Subclass can have its own specific attributes
- Subclass can have its own specific relationships

![Alt text](assets\IMG23.PNG)

**Specialisation**
- Define a number of subclasses of an entity type
- Each subclass contains a subset of entities from the superclass
- A subclass is defined based on more specific 
distinguishing characteristic on entities of the superclass

**Generalisation**
- Abstraction is the process of ignoring differences 
amongst some subclasses and generalise them 
into a superclass

#### Constraints
Specialisation may be:
![Alt text](assets\IMG24.PNG)

### Notation Guide

![Alt text](assets\IMG25.PNG)

![Alt text](assets\IMG26.PNG)