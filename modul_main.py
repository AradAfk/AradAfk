from api_get_gold import *
from api_get_dollar import *
import xlsxwriter
class C(A,B):
  def __init__(self,file1):
    A.__init__(self)
    B.__init__(self)
    self.file = xlsxwriter.Workbook(file1)
  def add(self):
    self.sheet1 = self.file.add_worksheet('dollar')
    self.sheet2 = self.file.add_worksheet('gold')
    return self.sheet1,self.sheet2
  def write_sheet(self):
    sheet1,sheet2 = self.add()
    self.sheet1.write('A1','name')
    self.sheet1.write('B1','price')
    self.sheet1.write_column('B2', self.lst1)
    self.sheet1.write_column('A2', self.lst2)
    self.sheet2.write('A1','name')
    self.sheet2.write('B1','price')
    self.sheet2.write_column('B2', self.lst3)
    self.sheet2.write_column('A2', self.lst4)
    self.file.close()

obj = C("file1.xlsx")
obj.write_sheet()

