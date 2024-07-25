immutable_var = (256, 387.2, "Python", True)
print(immutable_var)
# объект "кортеж" не поддерживает назначение элементов
mutable_list = [126, 789.6, "Python", False]
mutable_list[3] = 89
print(mutable_list)