#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Все элементы имеют целый тип. Дано целое число H.
#Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.
import numpy as np

N = 6
M = 2
H = np.random.randint(0, 10)

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

a = []
b = []
for i in range(M):
    if H in A[:, i]:
        a.append(i+1)
    else:
        b.append(i+1)
print("Столбцы, которые имеют хотя бы одно число H - {}\n".format(a))
print("Столбцы, которые не имеют это число - {}\n".format(b))
