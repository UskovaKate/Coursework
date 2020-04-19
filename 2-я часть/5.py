#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Определить средние значения по всем строкам и столбцам матрицы.
#Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Average_line = A.mean(axis=1)
Average_column = A.mean(axis=0)
Average_line = Average_line[: , np.newaxis]
A = np.hstack((A, Average_line))
Average_column = np.hstack((Average_column, [0.]))
A = np.vstack((A, Average_column))

print("Новая матрица:\r\n{}\n".format(A))
