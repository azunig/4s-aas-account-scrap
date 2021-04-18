from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time
import pandas as pd
import datetime

import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNjA2ODEyLCJ1aWQiOjE2OTI3MzEzLCJpYWQiOiIyMDIwLTExLTIyVDEzOjM4OjQyLjAwMFoiLCJwZXIiOiJtZTp3cml0ZSIsImFjdGlkIjo3Mzc3MjAyLCJyZ24iOiJ1c2UxIn0.N5CQ_ouDs97chj9MIRqxGnkw_CZehUyK0qhZm5qaGy8"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

url = 'C:\\Users\\aronv\\Documents\\Github\\4s-scrap\\ssrc_exp_032521_1118PM.csv'
url2 = 'C:\\Users\\aronv\\Documents\\Github\\4s-scrap\\ssrc_.csv'

df = pd.read_csv(url, skiprows=2)

df4s = pd.DataFrame({ 'Creador'   : ['Camilo Salvador Valencia Perez', 'Miguel Antonio Alarcon Medina'], 'Status'    : ['Active', 'Inactive'] })
inner_merged_total = pd.merge(df4s, df, on=["Creador", "Creador"])
new_df = inner_merged_total[['Solicitante','Creador','Recurso','Supervisor','Creacion','Estado','Ejecución','Apr. Supervisor','Apr. Dueño', 'Rechazo']]
new_df['Solicitante'] = new_df['Solicitante'].astype(str)
new_df['Creador'] = new_df['Creador'].astype(str)
new_df['Creacion'] = pd.to_datetime(new_df['Creacion']) 
new_df['Recurso'] = new_df['Recurso'].astype(str)
new_df['Supervisor'] = new_df['Supervisor'].astype(str)
new_df['Estado'] = new_df['Estado'].astype(str)

#for index, row in new_df.iterrows():

new_df.iloc[:,6 ] = new_df.iloc[:, 6].replace('--', '12-12-1999' ) 
new_df.iloc[:,7 ] = new_df.iloc[:, 7].replace('--', '12-12-1999' ) 
new_df.iloc[:,8 ] = new_df.iloc[:, 8].replace('--', '12-12-1999' ) 
new_df.iloc[:,9 ] = new_df.iloc[:, 9].replace('--', '12-12-1999' ) 

new_df['Ejecución'] = pd.to_datetime(new_df['Ejecución'])
new_df['Apr. Supervisor'] = pd.to_datetime(new_df['Apr. Supervisor'])
new_df['Apr. Dueño'] = pd.to_datetime(new_df['Apr. Dueño']) 
new_df['Rechazo'] = pd.to_datetime(new_df['Rechazo']) 

new_df.info()
new_df.to_csv(url2, encoding='UTF-8' )

print(inner_merged_total)



query = '{ boards (limit:1) {name id} }'
data = {'query' : query}
query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:1166842297, item_name:$myItemName, column_values:$columnVals) { id } }'

for index, row in new_df.iterrows():
    print('------')
    str(row['Recurso'])
    vars = {
        'myItemName' : row['Solicitante'], 
        'columnVals' : json.dumps(
            {
            'status'    : {'label'      : 'Done'      },
            'date4'     : {'date'       : row['Apr. Supervisor'].strftime("%Y-%m-%d") },
            'date_1'    : {'date'       : '2021-05-29'},
            'date_2'    : {'date'       : '2021-05-29'},
            'date'      : {'date'       : '2021-05-29'},
            'date5'     : {'date'       : '2021-05-29'},
            'text'      :  str(row['Recurso']),
            'text6'     :  str(row['Apr. Supervisor'].strftime("%Y-%m-%d")),
            'text_1'    :  str(row['Estado'])
            })
        }
    data = {'query' : query5, 'variables' : vars}
    r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())




item_name = 'New Subitem'
subitem = item.create_subitem(item_name, 'id', 'name', 'board.name')
subitem
{'id': '1234568', 'name': 'New Subitem', 'board': {'name': 'Some monday.com-generated Board'}}




