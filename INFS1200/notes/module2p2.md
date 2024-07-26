# Module 2: ER to Relation Mapping

![alt text](assets\IMG45.PNG)

## Steps for mapping

### 1. Regular Entity
For each entity type
1. Create a relation
2. Choose a key as the primary key
3. Include all simple attributes (e.g., a3 and a4) which arenot composite (e.g.,a2), derived or multivalued (e.g., a5)


![alt text](assets\IMG46.PNG)

### 2. Weak Entity

For each weak entity type
1. Create a relation
2. Set its primary key as the combination of the primary keys of owner
entities and its own partial key.
3. Include a foreign key from the relation to the primary key of the relation of its owner entity types.
4. Include all simple attributes which are not composite, derived or multivalued.

![alt text](assets\IMG47.PNG)

### 3. Binary 1:1 Relationship

For each binary 1:1 relationship type
1. Choose one of the participating entity types (preference is given to entity types with total participation)
2. Include a foreign key from the chosen entity type back to the primary keys of the relation of the other entity type.
3. Include all the simple attributes of the relationship type to the relation of the chosen entity type. 


![alt text](assets\IMG48.PNG)

### Step 4. Binary 1:N Relationship

For each (non-weak) binary 1:N relationship type
1. Identify the participating entity type at the N-side of the relationship type
2. Include a foreign key to the entity type on the N-side. This foreign key should be the primary key of the entity type on the 1-side.
3. Include any simple attributes of the relationship type as attributes of the relation of the N side.

![alt text](assets\IMG49.PNG)

### Step 5. Binary M:N Relationship
For each binary M:N relationship type
1. Create a new relation
2. Include foreign keys from relation to the primary key of the participating
entity types
3. The combination of foreign keys will form the primary key of R
4. R can have its own attributes that contribute to the primary key
5. Include any simple attributes of R as attributes of the new relation
![alt text](assets\IMG50.PNG)

### Step 6: Multivalued Attributes
For each multivalued attribute:
1. Create a new relation.
2. Include a foreign key from the relation to the primary key of the associated entity type.
3. The primary key is the combination of the multivalued attributes and the primary key of its associated entity type.
4. If the multivalued attribute is composite, include its simple components.

![alt text](assets\IMG51.PNG)

### Step 7: N-ary Relationships
For each N-ary relationship type
1. Create a new relation
2. Include foreign keys from the relation to the primary key of the participating entity types
3. The combination of foreign keys from entity types with many cardinality will form the primary key
4. R can have its own attributes that contribute to the primary key
5. Include any simple attributes of R as attributes of the new relation

![alt text](assets\IMG52.PNG)

![alt text](assets\IMG53.PNG)

### Step 8: Super and Subclasses Mapping
The following method works for total/partial and disjoint/overlapping subclasses.
For each subclass entity type
1. Create a relation
2. The primary key of each of the subclasses is the primary key of the superclass.
3. Include a foreign key from the relation to the primary key of the relation of its superclass entity type.
4. Include all simple attributes which are not composite, derived or multivalued.


![alt text](assets\IMG54.PNG)
