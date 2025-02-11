from random import randint
class st_sp_number:
    def __init__(self, start_numb , stop_numb):
        self.start_numb = start_numb
        self.stop_numb = stop_numb
        self.random_value = randint(start_numb , stop_numb)
        return self.random_value
class compare(st_sp_number):
    def __init__(self, start_numb , stop_numb):
        super().__init__(start_numb , stop_numb)
    def compare_method(self, input_numb):
         try:
            if self.random_value > input_numb:
              print('lower')
            elif self.random_value < input_numb:
              print('higher')
            elif self.random_value == input_numb:
              print('done')
         except ValueError:
            print('please enter integer')

class input_number(compare):
   def __init__(self, start_numb, stop_numb):
      super().__init__(start_numb, stop_numb)

   def input_value(self):
       input_numb = int(input('please enter your number: '))
       result = self.compare_method(input_numb)

object1 = input_number(1,4).input_value()