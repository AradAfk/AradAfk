from random import randint
class first:
    def first_numb(self):
        start = int(input('please enter your start number: '))
        stop = int(input('please enter your stop number: '))
        return start , stop
class second:
    def second_numb(self,start,stop):
        random_numb = randint(start,stop)
        return random_numb
    
class third(first,second):
    def final(self):
        start1,stop1 = self.first_numb()
        result_random = self.second_numb(start1,stop1)
        while True:
            try:
                number_input = int(input('please enter your  guess number: '))
                if result_random > number_input:
                    print('lower')
                elif result_random < number_input:
                    print('higher')
                else:
                    print('done')
                    break
            except ValueError:
                print('please enter correct data type integer ')
object1 = third()
object1.final()


        
    


             