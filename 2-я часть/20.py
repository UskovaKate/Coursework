#Создать квадратную матрицу A, имеющую N строк и N столбцов со случайными элементами.
#Определить произведение элементов, расположенных параллельно побочной диагонали (ближайшие к побочной).
#Элементы побочной диагонали имеют индексы от [N,0] до [0,N].
import numpy as np

N = 6
M = 2

A = np.random.randint(low=-4, high=9, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

a = b = np.fliplr(A).diagonal(1)
a_prod = a.prod()
print("Элементы которые выше побочной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_prod))
b = np.fliplr(A).diagonal(-1)
b_prod = b.prod()
print("Элементы которые ниже побочной диагонали: \n" + str(b) + "\nИх сумма = " + str(b_prod))
