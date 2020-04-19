#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Разделить элементы каждой строки на элемент этой строки с наибольшим значением.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Max = A.max(axis=1)
Max = np.array(Max)[: , np.newaxis]
A = A / Max

print("Новая матрица:\r\n{}\n".format(A))
