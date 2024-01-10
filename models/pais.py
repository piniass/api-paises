from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Date  
from config.db import meta, engine

paises = Table(
    "paises_api",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name",String(255)),
    Column("capital", String(255)),
    Column("habitantes", Integer),
    Column("diaNacional", Date),
)

meta.create_all(bind=engine,tables=[paises])