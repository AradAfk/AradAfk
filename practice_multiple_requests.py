import requests
import datetime
class get:
    def get_url(self):
       url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime=2011-07-02T12:00'
       request_var = requests.request('GET',url)
       result_var = request_var.json()
       result_var1 = result_var['data']['prefixes']
       for i in result_var1:
        result_var2 = (i['prefix'])
        print(result_var2)
class date:
   def get_date(self):
      day = datetime.datetime.now().day
      month = datetime.datetime.now().month
      year = datetime.datetime.now().year
      if len(str(day)) == 2 and len(str(month)) == 2:
       url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime={}-{}-{}T12:00'.format(year,month,day)
       print(url)
      elif len(str(day)) == 2 and len(str(month)) == 1:
       url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime={}-0{}-{}T12:00'.format(year,month,day)
       print(url)
      elif len(str(day)) == 1 and len(str(month)) == 2:
       url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime={}-{}-0{}T12:00'.format(year,month,day)
       print(url)
      else:
       url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime={}-0{}-0{}T12:00'.format(year,month,day)
       print(url)
class all(get,date):
  def all_data(self):
    self.get_url()
    self.get_date()

    
object1 = all() 
object1.all_data()   
         



      

      
      
    
    

