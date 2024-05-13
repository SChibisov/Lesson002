#"Распаковка параметров и параметры функции"

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10)
print_params(1, 'Hello')
print_params(33, 'World', 56)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'Hi', False]
values_dict = {'a': 1, 'b': 'Hello', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'True']
print_params(*values_list_2, 42)