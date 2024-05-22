import os
from dotenv import load_dotenv
import etl

load_dotenv()

print(' [ + ] Starting ETL process')

dataFrame = etl.getDataFromAPI()

print(' [ . ] Getting data from API')

# check for empty data frame
if dataFrame is None or dataFrame.empty:
    print('[ - ] No data fetched from API')

else:
    print(' [ + ] Data fetched from API')

print(' [ . ] Starting to load data into SQL table')

etl.loadDataIntoDb(dataFrame, os.getenv('server'), os.getenv('database'))

print(' [ + ] ETL process compelte')
