my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
L = 0
while L <= len(my_list):
    number = my_list[L]
    if number > 0:
        print(number)
    elif number < 0:
        break
    L += 1