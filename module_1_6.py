my_dict = {'Oleg': 1995, 'Dina': 2001, 'Max': 1986}
print(my_dict)
print(my_dict.get('Oleg'))
print(my_dict.get('Artur'))
my_dict.update({'Roma': 2003, 'Yana': 1996})
s = my_dict.pop('Oleg')
print(s)
print(my_dict)
my_set = {1, 4, 6, 2.5, 'Max'}
print(my_set)
print(my_set.add(7))
print(my_set.discard(1))
print(my_set)