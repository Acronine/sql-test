#sql Day 1:
#Amazon Mock Database

## Problem
We were given a task to create a database capable of storing all relevant data for a transaction from Amazon. We were told what kind of info was available and given free reign to create the relationships.

## Solution:

### ERD

![](https://github.com/Acronine/sql-test/blob/main/Mock-Amazon-ERD.pdf)

## Folder Structure

- gitignore
    - Tell git to ignore env

- .env file
    -   not be uploaded to GitHub. This will house all our local connection variables

- create.sql
    - Table creation for is

- insert.sql
    - Insertion of data
- query.sql
    - All our sql queries

- demo.py
    - House a class that will run all of these at once.