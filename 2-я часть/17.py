#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Добавить к матрице строку и вставить ее под номером L.
import numpy as np

N = 6
M = 2
L = np.random.randint(0, 10)

A = np.random.randint(low=-4, high=4, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

print("L = " + str(L))
A = np.delete(A, (L-1), axis=0)

print("Новая матрица:\r\n{}\n".format(A))
