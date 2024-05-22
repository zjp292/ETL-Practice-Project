import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=(LocalDb)\MSSQLLocalDB;"
    "Database=ETL_Db;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute(    """
    CREATE TABLE test (
    date date primary key,
    product_name nvarchar(50),
    price int
    )
    """
)