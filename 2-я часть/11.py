#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Просуммировать элементы каждой строки матрицы с соответствующими элементами L-й строки.
import numpy as np

N = 6
M = 2
L = np.random.randint(0, 10)

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

L_arr = np.array(A[L-1, :])
print("L страка: \r\n{}\n".format(L_arr))
A = A + L_arr

print("Новая матрица:\r\n{}\n".format(A))
