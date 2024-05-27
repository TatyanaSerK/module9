
class EvenNumbers:
    '''перебор чётных чисел в определённом числовом диапазоне'''

    def __init__(self, start = 0, end = 1):   #
        self.start = start                    #начальное значение (если значение не передано, то 0)
        self.end = end                        #конечное значение (если значение не передано, то 1)
        self.i = 0

    def __iter__(self):                       #обнуляем счетчик перед циклом
        self.i = 0
        return self

    def __next__(self):                       #возвращаем значения по требованию
        self.i += 1                           #каждый раз +1
        if self.i >= self.start:              #если больше/равно начальному значению
            if self.i % 2 == 0:               #делится на 2 (без остатка)
                return self.i                 #число четное!

        if self.i >= self.end or self.start > self.end:  #если больше конечного значения или начало больше конца
            raise StopIteration()                        #прерываем итерацию


en = EvenNumbers(start=10, end=25)             #найти четные значения в диапазоне

for numb in en:                                #выводим на экран
    print(numb)



