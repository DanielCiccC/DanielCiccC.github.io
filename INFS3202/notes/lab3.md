# Lab 3 - Migrations

### What is a migration
- A migration in CodeIgniter (and many other web development frameworks like Ruby on Rails and Django) is essentially a version-controlled script that allows developers to define database schemas or make changes to an existing database. Migrations manage the evolution of a database schema over time in a systematic and controlled manner. Instead of manually creating tables or altering them through a GUI or command line, migrations let you automate this process with PHP code.

1. Create a migration file
   - ``php spark make:migration create_users_table``
2. Define a Database Table in Migration File
   - Inside the migration file, you will find two methods: public function ``up()`` and public function ``down()``. Use these methods to define the database changes you wish to make and how to revert them, respectively.
3. Run the migration
   - ``php spark migrate``
4. View the Database Table in PHPMyAdmin

### Create the Model

```bash
php spark make:model UserModel --suffix
```

