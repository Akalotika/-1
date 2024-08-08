def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print()


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ['Sergey', 234, False]
values_dict = ['Anton', 234]
dict_ = {'c': 56}
print_params(*values_list)
print_params(*values_dict, 65)
print_params(*values_dict, **dict_)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)