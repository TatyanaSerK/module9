
def min_(int_list): # - принимает список, возвращает минимальное значение из него.
    return min(int_list)
def max_(int_list): # - принимает список, возвращает минимальное значение из него.
    return max(int_list)
def len_(int_list): # - принимает список, возвращает кол-во элементов в нём.
    return len(int_list)
def sum_(int_list): # - принимает список, возвращает сумму его элементов.
    return sum(int_list)
def sorted_(int_list):  # - принимает список, возвращает новый отсортированный список на основе переданного.
    return sorted(int_list)


def apply_all_func(int_list, *functions):
    reuslts = {}  # пустой словарь для записи результата
    for fun in functions:  # для каждой функции
        res = fun(int_list) #вызываем функцию
        reuslts[fun.__name__] = res  #записываем в словарь
    return reuslts


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))



