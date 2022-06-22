import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

USER = os.environ['POSTGRES_USER']
PASS = os.environ['POSTGRES_PASS']
HOST = os.environ['POSTGRES_HOST']
PORT = os.environ['POSTGRES_PORT']
DB = os.environ['POSTGRES_DB']
db_string = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(db_string)

meta = MetaData()

items = Table(
   'items', meta,
   Column('name', String, primary_key = True),
   Column('price', Integer),
)
meta.create_all(engine)

print(engine.table_names())