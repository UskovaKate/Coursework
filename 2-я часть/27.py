#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Все элементы имеют целый тип. Дано целое число H.
#Определить, какие строки имеют хотя бы одно такое число, а какие не имеют.
import numpy as np

N = 6
M = 2
H = np.random.randint(0, 10)

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

bool = A == H
col_sum = np.sum(bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())
print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())
