#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.Найти наибольший элемент столбца матрицы A, для которого сумма абсолютных значений элементов максимальна.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}".format(A))

sum = A.sum(axis=0)
index = sum.argmax(axis=0)
max = A.max(axis=0)
max = max[index]

print("Наибольшее значение: {}".format(max))
