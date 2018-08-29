def quicksort(array):
    pivot_p = len(array) - 1
    if pivot_p < 0:
        return array
    
    i = 0
    while i < pivot_p:
        if array[i] > array[pivot_p]:
            t = array[i]
            array[i] = array[pivot_p-1]
            array[pivot_p-1] = array[pivot_p]
            pivot_p = pivot_p - 1
            array[pivot_p+1] = t
            i = 0
        else:
            i += 1
    
    array = quicksort(array[:pivot_p]) + [array[pivot_p]] + quicksort(array[pivot_p+1:])
            
    return array

if __name__ == '__main__':
	test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
	print(quicksort(test))
