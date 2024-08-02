import random
first_number = random.randint(3, 20)
result = []
list_ = []
for i in range(first_number + 1):
    if i > 2 and first_number % i == 0:
        list_.append(i)
for j in range(1, int(first_number / 2 + 1)):
    for u in list_:
        if u > j and (u / 2) < (u - j):
            result.append(j)
            result.append(u - j)
print("Первое число :", first_number)
print("Пароль:", result)