# lightroom-sqlalchemy2
A repository of SQLAlchemy v2 table objects for manipulating Lightroom Classic 
SQLite libraries. 

The SQLAlchemy ORM classes are in the directory lrcsql2, currently there are a 
few manually created objects, and an automated creation of the orm objects.

The automated creations are created from the `convert_sql_to_tables.ipynb` in
the tools directory. This automation can probably be improved. 

Current Version 0.1.0 - 2024-01-22

## Goals

* version `0.1` - All tables with all columns
* version `0.2` - All tables with basic column types
* version `0.3` - All tables with nullables, uniques, and indexes
* version `0.4` - Table relations mapped out
* version `1.0` - Relationships added to ORM