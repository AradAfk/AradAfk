from random import randint
class random:
    def __init__(self,start,stop):
        self.start = start 
        self.stop = stop
        self.random = randint(start,stop)
        return self.random
class input_guess(random):
    def __init__(self,start,stop):
        super().__init__(start,stop)
    def input_numb(self):
        while True:
            try:
              input_number = int(input('please enter your guess number: '))
              assert 1 <= input_number <= 4
              if self.random > input_number:
                  print('lower')
              elif self.random < input_number:
                  print('higher')
              else:
                  print('done')
                  break
            except  AssertionError as f:
                f = 'between 1 till 4'
                print(f)

                
object1 = input_guess(1,4).input_numb()
