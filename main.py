import os
from dotenv import load_dotenv
import etl

# Load environment variables
load_dotenv()

print(' [ + ] Starting ETL process')

dataFrame = etl.getDataFromAPI()
print(' [ . ] Getting data from API')

# Check if DataFrame is loaded correctly
if dataFrame is None or dataFrame.empty:
    print('[ - ] No data fetched from API')
else:
    print(' [ + ] Data fetched from API')

print(' [ . ] Starting to load data into SQL table')

if not etl.loadDataIntoDb(dataFrame, os.getenv('server'), os.getenv('database')):
    print(' [ - ] Failed to load data into SQL table')
else:
    print(' [ + ] Data successfully loaded into SQL table')
