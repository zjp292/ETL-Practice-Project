# ETL Practice Project
---
## This project uses a couple libraries. These libraries, as well as their uses are:

- requests - Used to get data from API
- pandas - Used to store API data in a DataFrame
- dotenv - Used to keep API and SQL server keys seperate from the main project
- pyodbc - Used to connect to SQL server
- matplotlib - Used for plotting (WIP)
---

![image](https://github.com/zjp292/ETL-Practice-Project/assets/72166103/e022d208-8289-4240-84c4-2f0774009b72)

![image](https://github.com/zjp292/ETL-Practice-Project/assets/72166103/ad89d8c7-75cb-453b-a432-fce30ac04cc2)

---
## Extract
The extraction process started with the Tiingo API. I collected historical Apple stock data from the dates **2014-05-20** to **2024-05-21**. 

## Transform

This step is fairly straight forward. Since the data is uniform in its type and doesnt have any null values, I did not transform the data in any way. An expansion of this project could see me take an incomplete data source and transform it further.

## Load

For this section, I used a Microsoft SQL Server hosted on my local machine. I used the db_credentials.py file to create the StockData table. From there, I created used the loadDataIntoDb function to load the data held in the DataFrame into the SQL server
