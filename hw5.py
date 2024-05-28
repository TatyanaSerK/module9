
def is_prime(func):
    #результат функции - число "Простое" или "Составное"
    def wrapper(a, b, c):
        res = func(a, b, c)
        k = 0
        for i in range(2, (res // 2) + 1):  #на сколько чисел делится res
            if res % i == 0:
                k += 1
        if k == 0:                          #ни на что не делится (только 1 и на себя)
            print('Простое')
        else:
            print('Составное')
        print(res)
    return wrapper                           #возвращает значение функции wrapper в is_prime


@is_prime                    # декоратор
def sum_three(a, b, c):      # сумма 3х чисел
    sum = a + b + c
    return sum

result = sum_three(2, 3, 6)
print(result)


