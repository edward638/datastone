Run the following commands to create the database and load data into it:

```
createdb *dbname*
psql *dbname* -af create.sql
psql *dbname* -af load.sql
```
