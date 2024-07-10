# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
# список совпадения букв в одинаковой позиции
print(list(map(lambda x, y: x == y, first, second)))



# Замыкание:
def get_advanced_writer(file_name):
    with open(file_name, 'w+', encoding='utf-8'): #файл для записи
        def write_everything(*data_set):
            with open(file_name, 'w', encoding='utf-8') as file:
                for i in data_set: # записываем каждый элемент с новой строки
                    file.write(str(i) + '\n')
            return file
    return write_everything #возвращаем функцию для записи


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



#Метод __call__:

import random

class MysticBall:

    def __init__(self, *words): #
        self.words = words

    def __call__(self): #случайным образом выбирает слово из words
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

