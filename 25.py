#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Определить, сколько нулевых элементов содержится в каждом столбце и в каждой строке матрицы.
#Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

bool = A == 0
col = np.sum(bool, axis=1)
A = np.insert(A, M, col, axis=1)
row = np.append(np.sum(bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)
print("Новая матрица:\r\n{}\n".format(A))
