def calculate_structure_sum(*args):
    summa_values = 0
    for item in args:
        if isinstance(item, list):
            for values in item:
                summa_values += calculate_structure_sum(values)
        elif isinstance(item, tuple):
            for values in item:
                summa_values += calculate_structure_sum(values)
        elif isinstance(item, set):
            for values in item:
                summa_values += calculate_structure_sum(values)
        elif isinstance(item, dict):
            for key, value in item.items():
                summa_values += calculate_structure_sum(key, value)
        elif isinstance(item, str):
            summa_values += len(item)
        elif isinstance(item, int):
            summa_values += item
    return summa_values


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)