import requests
class A:
  def __init__(self):
    self.lst3 = []
    self.lst4 = []  
    self.url = 'https://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency_v2.json'
    req_gold = requests.request('GET', self.url).json()
    req_api = req_gold['gold']
    for i in req_api:
      price = i.get('price')
      self.lst3.append(price)
    for j in req_api:
      name = j.get('name')
      self.lst4.append(name)
