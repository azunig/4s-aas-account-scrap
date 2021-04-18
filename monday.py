import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNjA2ODEyLCJ1aWQiOjE2OTI3MzEzLCJpYWQiOiIyMDIwLTExLTIyVDEzOjM4OjQyLjAwMFoiLCJwZXIiOiJtZTp3cml0ZSIsImFjdGlkIjo3Mzc3MjAyLCJyZ24iOiJ1c2UxIn0.N5CQ_ouDs97chj9MIRqxGnkw_CZehUyK0qhZm5qaGy8"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query = '{ boards (limit:1) {name id} }'
data = {'query' : query}

r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())

query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:1166842297, item_name:$myItemName, column_values:$columnVals) { id } }'

vars = {
  'myItemName' : 'Hola :) Como ta?!', #'Creador',
  'columnVals' : json.dumps(
    {
    'status'    : {'label'      : 'Done'      },
    'date4'     : {'date'       : '2021-08-27'},
    'date_1'    : {'date'       : '2021-05-29'},
    'date_2'    : {'date'       : '2021-05-29'},
    'date'      : {'date'       : '2021-05-29'},
    'date5'     : {'date'       : '2021-05-29'},
    'text'      :  'Recurso',
    'text6'     :  'Supervisor',
    'text_1'    :  'Estado'
    }
  )
  }

data = {'query' : query5, 'variables' : vars}
r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())
