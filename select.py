def select_sort_stable(arr):
    if(len(arr) == 0): return
    for j in xrange(len(arr)):
        min = j
        for i in xrange(j+1, len(arr)):
            if(arr[i] < arr[min]): min = i
        if(min !=j):
            value = arr[min]
            for 1 in xrange(min,j-1,-1):
                arr[I] = arr[I-1]
                arr[j] = value
 random = [34,0,1,65,9]
 select_sort_stable(random)
 print(random)
