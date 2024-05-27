'''Фабрика функций'''
def my_operation(operation):
    if operation == "division":     #деление
        def division(x, y):
            return x / y
        return division
    elif operation == "multiply":    #умножение
        def multiply(x, y):
            return x - y
        return multiply
my_func_add = my_operation("division")
print('деление: ',my_func_add(8,2))

my_func_add = my_operation("multiply")
print('умножение: ',my_func_add(8,2))


'''Пример лямбда функции (квадрат числа) с аналогом через def'''

def square_def(x):             #
   return x ** 2
print('квадрат : ',square_def(3))

square = lambda x: x ** 2      #
print('квадрат лямбда: ', square(3))



'''Пример создания вызываемого объекта (площадь прямоугольника)'''
class Rect:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self):
       return self.a * self.b

repeat_five = Rect(5, 4)
print('площадь прямоугольника: ', repeat_five())