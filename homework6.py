my_dict = {"Egor": 1999, "Petia": 1987, "Dima": 1978}
print(my_dict)
print(my_dict["Egor"])
print(my_dict.get("Kolia"))
my_dict.update({"Kolia": 2000, "Stas": 2001})
a = my_dict.pop("Petia")
print(a)
print(my_dict)
my_set = {1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 'pop', 'pop', 'pop'}
print(my_set)
my_set.add(9)
my_set.add((4, 5, 6))
my_set.remove(2)
print(my_set)