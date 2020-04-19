#Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Найти сумму элементов всей матрицы.
#Определить, какую долю в этой сумме составляет сумма элементов каждой строки.
#Результат оформить в виде матрицы из N строк и M+1 столбцов.
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Sum = A.sum()
print("Сумма элементов всей матрицы: " + str(Sum) + "\n")
Sum_column = A.sum(axis=1)
X = []
for i in range(0, N):
    n = Sum_column[i] / Sum
    X.append(n)
X = np.array(X)[: , np.newaxis]
A = np.hstack((A, X))

print(A)
