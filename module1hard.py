grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = list(students)
students_.sort()
a = students_.pop(0)
j = students_.pop(1)
s = students_.pop(2)
b = students_.pop(-2)
k = students_.pop(-1)
h = [a, b, j, k, s]
A = sum(grades.pop(0)) / 5
K = sum(grades.pop(1)) / 4
J = sum(grades.pop(2)) / 5
S = sum(grades.pop(-2)) / 4
B = sum(grades.pop(-1)) / 3
H = [A, S, K, B, J]
print(dict(zip(h, H)))