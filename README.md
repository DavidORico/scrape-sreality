## How to run this project

Prerequisites: python3, scrapy, scrapyscript, psql

In the repository call:
```
scrapy crawl sreality -O estates.json
```
This launches the spider that scrapes the https://www.sreality.cz/hledani/prodej/byty
and saves the information about the 50 first posts into a JSON file

Then run the python script that transforms the JSON file into an sql query 
that inserts the document into the database.
```
python3 create_insert_query.py
```

Finally connect to a database of your choice (I created a server on local host using pgAdmin)
and run queries in this order
```
create_table.sql
insert_query.sql
view_estates.sql
```