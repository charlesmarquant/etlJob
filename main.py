import requests
import dbutil
import pandas as pd

## Connect to MySQL database
connectDB = dbutil.connect_to_mysql()
cursor = connectDB.cursor()

## Select data from staging table
try:
    with connectDB.cursor() as cur:
        cur.execute('SELECT * FROM stgPokemon')
        rows = cur.fetchall()
        for row in rows:
            print(row)

finally:
    connectDB.close()

