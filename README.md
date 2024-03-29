# lightroom-sqlalchemy2
A repository of SQLAlchemy v2 table objects for manipulating Lightroom Classic 
SQLite libraries. 

The SQLAlchemy ORM classes are in the directory lrcsql2, currently there are a 
few manually created objects, and an automated creation of the orm objects.

The automated creations are created from the `convert_sql_to_tables.ipynb` in
the tools directory. This automation can probably be improved. 

Current Version 0.1.0 - 2024-01-22

## Why? 

Recently I was trying to get some Lightroom information in ArcGIS Pro, and tried to use SQLAlchemy 2 to programmatically get what I wanted. The auto explore functionality in SQLAlchemy could not autogenerate objects to use, so I had to turn to DBeaver. 

With this project I am creating a base SQLAlchemy ORM object set that many can use to perform operations on their Lightroom Classic catalogs. 

## Collaboration

I am organizing the tables with a Google Sheets sheet to be able to build the different ORM objects. You can see the sheet here as I fill in the fields:
https://docs.google.com/spreadsheets/d/e/2PACX-1vRwEc_jG3Fun_Q4PSQzmDgm6BhunHGK3sLcQQjVUkrSUhMYAnLimhmVcOvcuqaS4P12R1CUJROCRt2k/pubhtml

## Goals

* version `0.1` - All tables with all columns
* version `0.2` - All tables with basic column types
* version `0.3` - All tables with nullables, uniques, and indexes
* version `0.4` - Table relations mapped out
* version `1.0` - Relationships added to ORM