#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Разделить элементы матрицы на элемент матрицы с наибольшим значением.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Max = A.max()
print(Max)
A = A / Max

print("Новая матрица:\r\n{}\n".format(A))
