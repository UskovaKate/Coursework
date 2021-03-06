#Создать квадратную матрицу A, имеющую N строк и N столбцов со случайными элементами.
#Найти сумму элементов, расположенных выше главной диагонали, и произведение элементов, расположенных выше побочной диагонали (элементы главной диагонали имеют индексы от [0,0] до [N,N], а элементы побочной диагонали — от [N,0] до [0,N]).
import numpy as np

N = 6
M = 6

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

iu = np.triu_indices(N, 1)
a = A[iu]
a = np.sum(np.array(a))
print("\nCумма элементов выше главной диагонали = " + str(a))
b = np.fliplr(A)[iu]
b = np.prod(np.array(b))
print("\nПроизведение элементов выше побочной диагонали = " + str(b))
