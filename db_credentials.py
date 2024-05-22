import pyodbc


server = '(LocalDb)\MSSQLLocalDB'  # Replace with your server name
database = 'ETL_Db'  # Replace with your database name
driver = '{ODBC Driver 17 for SQL Server}'  # Make sure you have the appropriate driver installed



conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
cursor = conn.cursor()


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

cursor.execute(create_table_sql)

# commit the changes to the table
conn.commit()
cursor.close()
conn.close()