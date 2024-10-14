def print_params(a = 1, b = 'line', c = True):
     print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print()
values_list = ('line', 123, True)
print_params(*values_list)
values_dict = {'a': 'text', 'b': False, 'c': 33}
print_params(**values_dict)

values_list_2 = [54.32, 'line']
print_params(*values_list_2, 42)