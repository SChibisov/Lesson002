my_list = ["banan", "coconut", "pear", 'orange']
print(my_list)
print("First elemet: ", my_list[0])
print("Last element: ", my_list[-1])
print("Sublist: ", my_list[2:5])
my_list[2] = "grape"
print("Modified list:", my_list)
print()

my_dict = {'banan':'банан', 'cocnut':'кокос','pear':'груша','orange':'апельсин' }
print('Dictionary: ', my_dict)
print('Translation: ', my_dict['orange'])
my_dict.update({'kiwi':'киви'})
print('Modified dictionary: ', my_dict)