import os
from dotenv import load_dotenv, dotenv_values
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pyodbc

load_dotenv()

def getDataFromAPI():
    headers = {
    'Content-Type': 'application/json'
    }
    requestResponse = requests.get(f"https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2014-05-20&token="
                               f"{os.getenv('API_TOKEN')}", headers=headers)

    hist_df = pd.DataFrame(requestResponse.json())

    print(hist_df.tail())
    hist_df.dropna()
    return hist_df

def plotData(df):
    df['adjClose'].plot(figsize=(10,7))
    # plt.ylabel('adjClose', fontsize=14)
    # plt.xlabel('date', fontsize=14)

    plt.show()


def loadDataIntoDb(df, dbServer, database):
    driver = '{ODBC Driver 17 for SQL Server}'
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={dbServer};DATABASE={database};Trusted_Connection=yes;')
    #cursor = conn.cursor()

    # Create the connection string
    #engine = create_engine('mssql+pyodbc://@' + dbServer + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
    # Print connection string for debugging
    #print(f'Connection string from loadDataIntoDb: {connection_string}')

    # Create an SQLAlchemy engine
    #engine = create_engine(connection_string)

    for index, row in df.iterrows():
        cursor = conn.cursor()

        # Extract values from the DataFrame row
        date_value = row['date']
        close_value = row['close']
        high_value = row['high']
        low_value = row['low']
        open_value = row['open']
        volume_value = row['volume']
        adjClose_value = row['adjClose']
        adjHigh_value = row['adjHigh']
        adjLow_value = row['adjLow']
        adjOpen_value = row['adjOpen']
        adjVolume_value = row['adjVolume']
        divCash_value = row['divCash']
        splitFactor_value = row['splitFactor']

        insert_query = ("INSERT INTO StockData ([date], [close], [high], [low], [open], [volume], [adjClose], [adjHigh], "
                        "[adjLow], [adjOpen], [adjVolume], [divCash], [splitFactor]) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

        cursor.execute(insert_query, (
        date_value, close_value, high_value, low_value, open_value, volume_value, adjClose_value, adjHigh_value, adjLow_value,
        adjOpen_value, adjVolume_value, divCash_value, splitFactor_value))

        # Commit the transaction
        try:
            conn.commit()
        except Exception as e:
            print(f' [ - ] Failed to commit: {e}')

        # Close cursor
        cursor.close()
    conn.close()
    print(' [ + ] All data added to table')