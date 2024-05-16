#Функция с произвольным числом параметров разного типа
def test(param, *params_type, name="Student", **params):
    print(param)
    print(params_type)
    print(name)
    for key, value in params.items():
        print(key, value)
    print(params)


test('Параметры всех типов', 5, 6, 10, name='Sergey', course="-Pyhon", modul="-3")


# Рекурсивная функция, которая считает факториал
def factor(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factor(n - 1) * n


print(factor(6))
