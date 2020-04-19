#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Определить, сколько отрицательных элементов содержится в каждом столбце и в каждой строке матрицы.
#Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

X = []
for i in range(0, N):
    K = 0
    for j in range(0, M):
        if A[i,j] < 0:
            K += 1
    X.append(K)
Y = []
for i in range(0, M):
    K = 0
    for j in range(0, N):
        if A[j,i] < 0:
            K += 1
    Y.append(K)
X = np.array(X)[: , np.newaxis]
A = np.hstack((A, X))
Y = np.hstack((Y, [0.]))
A = np.vstack((A, Y))

print("Новая матрица:\r\n{}\n".format(A))
