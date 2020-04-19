#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Перемножить элементы каждого столбца матрицы с соответствующими элементами K-го столбца.
import numpy as np

N = 6
M = 2
K = np.random.randint(0, 10)

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

K_arr = np.array(A[:, K-1])
K_arr = K_arr[: , np.newaxis]
print("K-ый столбец: \r\n{}\n".format(K_arr))
A = A * K_arr

print("Новая матрица:\r\n{}\n".format(A))
