from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/prueba")

meta = MetaData()

conn = engine.connect().execution_options(isolation_level='AUTOCOMMIT')

