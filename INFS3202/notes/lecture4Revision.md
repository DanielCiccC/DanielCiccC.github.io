# Lecture 4 Revision
# MVC – Databases and CI Models

### What is a Relational Database Server?
- Stores Data Efficiently: 
  - A database organizes and stores data in a manner that makes it easily accessible and manageable. Indexes data so that results are returned fast.
- Multiple Related Tables: 
  - It can consist of several related tables, allowing for the organization of different types of information in a structured way.
- Scales with Needs: 
  - Databases are designed to scale, meaning they can handle an increasing amount of work or data as the need grows.
- Search, Add, Update via SQL: 
  - Utilizes Structured Query Language (SQL) for searching, adding, and updating data, providing a powerful tool for managing the database. 

> - Structured
> - building something that has to scale

### What Database Servers are Available?
- **SQLite:** A lightweight database filesystem database. Ideal for development, 
small applications, and situations where simplicity and minimal setup are 
advantageous.
- **MySQL:** A popular open-source relational database management system known 
for its reliability and ease of use. It's widely used for web applications and 
supports a variety of programming languages.
- **PostgreSQL:** An advanced open-source relational database system, offering 
strong compliance to SQL standards, and known for its robustness, scalability, 
and support for advanced data types and functionalities.
- **MS SQL Server:** A comprehensive, enterprise-level database management 
system developed by Microsoft. Known for its high performance, robust security 
features, data integration, and analysis tools. 
- **Oracle Database:** A comprehensive, enterprise-grade database solution that 
provides robust support for large-scale databases, complex applications, and 
data warehousing needs. Known for its performance, security, and scalability.
- **Local and UQCloud Options:** SQLite can be used locally, providing an easy-to-
manage database environment without the need for a server. Both MySQL and 
PostgreSQL are available on UQCloud.

### Why are databases Essential for Web Development?
- Data Management: 
  - Databases provide a structured and efficient way to store, manage, and retrieve data, which is crucial for dynamic websites and applications.
- User Interaction: 
  - They enable personalized user experiences by storing user preferences, orders, and account information, enhancing engagement and satisfaction.
- Scalability: 
  - Databases can handle increasing amounts of data and user requests, allowing websites to grow and accommodate more traffic seamlessly.
- Data Integrity: 
  - Ensure consistency and accuracy of the data through constraints, transactions, and relational database design, minimizing errors and data duplication.
- Security: 
  - Databases offer robust security features to protect sensitive information, such as user data and financial transactions, from unauthorized access and breaches.

### Structured Query Language
- **Data Definition Language (DDL)** - Defines and modifies a schema e.g. CREATE / DROP /  
ALTER table; does not manipulate data 
- **Data Manipulation Language (DML)** - Language used to retrieve (SELECT), add (INSERT), 
modify (UPDATE) and DELETE data
- **Data Control Language (DCL) statements**. Used for providing  (GRANT) / withdrawing 
(REVOKE) access privileges
- **Transaction Control Language (TCL)** statements are used to manage the changes made 
by DML statements. It allows statements to be grouped together into logical transactions. 
Example: COMMIT, ROLLBACK, etc.

### Deleting Data

```sql
DELETE FROM customers
WHERE name=‘Mary’
```

### Updating Records in a Table
```sql
UPDATE StudentRecord
SET Name=‘Jack’
WHERE studentID = 1234
```

### Codeigniter - with Data Access

- Using a Web Framework should make your life as a developer easier
- A Framework will include a number of abstractions to help you write code to interact with a database
- CodeIgniter 4 has numerous features:
  - Central config file (.env) to store database connections
  - Migrations to help you create tables and have database version control
  - Models to simplify reading, inserting, updating and deleting content from a database table (just use simple objects instead of using SQL)
  - The Spark command line to help you create Migration files and new model files.

> - simplify development
> - deal with extractions

### What is a Migration?
- **Versioned Database Schemas:**
  - Migrations in CodeIgniter 4 provide a method for version controlling your database schema. This allows for easy management of database changes over time.
- **Automated Database Changes:** 
  - They automate the process of applying database changes, such as creating or altering tables, adding indexes, and more, ensuring consistency across different environments.
- **Simplifies Development and Deployment Workflow:** 
  - Migrations simplify the development workflow by allowing team members to share and apply database changes in a controlled and systematic manner. Easy to deploy the schema of a database
- **Programmatic Schema Manipulation**: 
  - Migrations are PHP classes that contain methods to programmatically execute database operations, giving developers a powerful tool to manipulate the schema.

> - Use the features in Codeigniter
> - Web development frameworks come with migrations
>
> - create code to describe the changes to the schema
> - files are versioned and can be stored in file versioning applications (git, etc.)

### Codeigniter - Spark
“spark” is a command-line tool that facilitates the development and management of CodeIgniter applications.

- Running database migrations and seeders to manage database schema and initial data setup
- Starting a development web server
- Generating boilerplate code (new files) for new controllers, models, and other components.

### Create a Migration

- Use the spark make:migration
command
- ``php spark make:migration create_customers_table``
- ``php spark make:migration create_orders_table``

- This will create a new file in the app/Databases/Migrations folder
  - The file will have a data time stamp and be versioned
  - You need to add the fields that need to be created in the table
    - The up() method defines the schema for creating the tables.
    - The down() method defines the schema for dropping the tables.

**Example Migration**
```php
class CreateCustomersTable extends Migration
{
    public function up()
    {
        $this->forge->addField([
            'id' => [
                'type' => 'INT',
                'constraint' => 11,
                'unsigned' => true,
                'auto_increment' => true,
            ],
            'name' => [
                'type' => 'VARCHAR',
                'constraint' => 255,
            ],
            'email' => [
                'type' => 'VARCHAR',
                'constraint' => 255,
            ],
        ]);
        $this->forge->addKey('id', true);
        $this->forge->createTable('customers');
    }

    public function down()
    {
        $this->forge->dropTable('customers');
    }
}
```

### Raw SQL and QueryBuilder Class

**Raw SQL**
- We can use `query()` function to pass in real SQL scripts as a parameter.
- Builder can help you generate the raw SQL scripts, which will be sent to query().
- To load the Query Builder, use the table() method on the database connection. 
- It's important to note that the Query Builder needs to be explicitly loaded if you require.
- Get Data(i.e. SELECT *): \$builder->get()

```php
$db = db_connect();
$db->query('SELECT * FROM STUDENTS')
```
**QueryBuilder**
- CodeIgniter Model has one instance of the Query Builder for that model’s database connection. You can get access to the shared instance of the Query Builder any time you need it:
```php
$builder = $userModel->builder();
```
- Once you get the Query Builder instance, you can call methods of the Query Builder. However, since Query Builder is not a Model, you cannot call methods of the Model.
```php
$customerBuilder = $userModel->builder('customers');
```
- You can also use Query Builder methods and the Model’s CRUD methods in the same chained call, allowing for very elegant use:
```php
$users = $userModel->where('status','active')
    ->orderBy('last_login', 'asc')
    ->findall();
```

### Codeigniter Database Access 

![alt text](assets\IMG96.PNG)

### How does this help developer workflow?

- A few scenarios
  - You develop locally and then deploy to production:
  - You can just run the migration when you deploy and update your application
- You have multiple developers
  - When a database change is made, the code for the change is committed to the code repository
  - Other developers can then run the migration to update their local databases
- You release open source software
  - The same migration code and create SQL create and modify statements for multiple databases
  - Each developer that downloads your software can choose their own database server 
(e.g. Postgres) and not worry about conflicts

> - scripting specific way to manage table changes