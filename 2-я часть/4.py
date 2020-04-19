#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Найти наименьшее значение среди средних значений для каждой строки матрицы.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}".format(A))

Average = A.mean(axis=1)
index = Average.argmin(axis=0)
min = Average.min(axis=0)

print("Наименьшее среднее значение: {}".format(min))
