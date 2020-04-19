>>> def select_sort(arr, dim):
	alg_count = [0, 0]
	for i in range(0, dim-1):
		min = i
		for j in range(i + 1, dim):
			alg_count[0] += 1
			if arr[j] < arr[min]:
				min = i
		if j !=min:
			alg_count[1] += 1
			arr[i], arr[min] = arr[min], arr[i]
	return alg_count

>>> import random
>>> dim = 30
>>> arr = [random.randint(0, 100) for i in range(dim)]
>>> print(select_sort(arr, dim))
