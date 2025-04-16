import requests
import inquirer
import dbutil
import pandas as pd

## Connect to MySQL database
# pip

## Filter from staging table
confirm = {
    inquirer.Confirm('confirmed',
                     message="Do you want filter data ?" ,
                     default=False),
}
confirmation = inquirer.prompt(confirm)


# ## Select data from staging table
# try:
#     with connect_db.cursor() as cur:
#         cur.execute('SELECT * FROM stgPokemon')
#         rows = cur.fetchall()
#         for row in rows:
#             response = requests.get(row['pokemonUrl'])
#             json_data = response.json()
#             wk_id = json_data['forms'][0]['url'].split('/')[-2]
#             wk_name = json_data['forms'][0]['name']
#             wk_type = json_data['types'][0]['type']['name']
            
#             print(wk_id+': '+wk_name + ' - ' + wk_type)

# finally:
#     connect_db.close()

