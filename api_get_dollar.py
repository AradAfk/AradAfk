import requests
class B:
  def __init__(self):
    self.lst2 = []
    self.lst1 = []
    self.url1 = 'https://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency_v2.json'
    req_dollar = requests.request('GET', self.url1).json()
    req_api1 = req_dollar['currency']
    for x in req_api1:
      price1 = x.get('price')
      self.lst1.append(price1)
    for y in req_api1:
      name1 = y.get('name')
      self.lst2.append(name1)



