import requests
import json

lst = []

url = 'https://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency_v2.json'
url_req = requests.request('GET',url).json()
req0 = url_req["gold"]

for i in req0:
    name = i.get('name')
    price = i.get('price')
    req1 = {'name': name , 'price' : price}
    lst.append(req1)

with open('file1.json', 'w') as f:
    json.dump(lst,f)
    

