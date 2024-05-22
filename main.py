import os
from dotenv import load_dotenv, dotenv_values
import requests
import pandas as pd
import matplotlib.pyplot as plt
import pyodbc




load_dotenv()

headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get(f"https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2014-05-20&token="
                               f"{os.getenv('API_TOKEN')}", headers=headers)

hist_df = pd.DataFrame(requestResponse.json())

#print(hist_df.head())



hist_df['adjClose'].plot(figsize=(10,7))
# plt.ylabel('adjClose', fontsize=14)
# plt.xlabel('date', fontsize=14)

plt.show()

# date
# close
# high
# low
# open
# volume \
# adjClose
# adjHigh
# adjLow
# adjOpen
# adjVolume
# divCash
# splitFactor