import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn = pyodbc.connect(f'DRIVER={os.getenv("driver")};SERVER={os.getenv("server")};DATABASE={os.getenv("database")};Trusted_Connection=yes;')
cursor = conn.cursor()

# creates a sql table for dataframe row values
create_table_sql = """
CREATE TABLE StockData (
    date DATE PRIMARY KEY,
    [close] FLOAT,
    [high] FLOAT,
    [low] FLOAT,
    [open] FLOAT,
    volume BIGINT,
    adjClose FLOAT,
    adjHigh FLOAT,
    adjLow FLOAT,
    adjOpen FLOAT,
    adjVolume BIGINT,
    divCash FLOAT,
    splitFactor FLOAT
)
"""

# run the sql query
cursor.execute(create_table_sql)

# create table and close the connections/cursor
conn.commit()
cursor.close()
conn.close()