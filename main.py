import requests
import dbutil
import pandas as pd

## Connect to MySQL database
connectDB = dbutil.connect_to_mysql()
cursor = connectDB.cursor()

## Read staging table
# stgPokemonData = []
sql = "SELECT * FROM stgPokemon"
# cursor.execute(sql)
# columns = cursor.description 
# for value in cursor.fetchall(): 
#     tmp = {}
#     for (index, column) in enumerate(value): 
#         tmp[columns[index][0]] = column
#     stgPokemonData.append(tmp)
# print(stgPokemonData)

stgPokemonData = pd.read_sql_query(sql, connectDB)
print(stgPokemonData)

