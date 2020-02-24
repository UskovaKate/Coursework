def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) -  1):
            if nums[ i] >>  nums[ i +  1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
random = [ 9 , 10 , 45 , 1 , 30]
bubble_sort(random)
print(random)
