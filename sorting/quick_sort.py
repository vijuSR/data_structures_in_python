# quick-sort is an inplace sorting algorithm
# space complexity: O(1)
# time complexity: worst-case: O(n^2) best/average-case: O(nlog(n))
# better option for highly unsorted arrays

def quicksort(array):
    """
    param: array: list of integers, floats, characters
    return: array: sorted list

    """

    # select the right most element as the pivot
    pivot_p = len(array) - 1
    if pivot_p < 0:
        return array
    
    # start index
    i = 0

    # until the pivot comes to the perfect position
    # which means all the elements on the LHS of pivot
    # is less and on RHS of pivot is greater that it.
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
    
    # recursively repeat the same steps on both the partitions.
    array = quicksort(array[:pivot_p]) + [array[pivot_p]] + quicksort(array[pivot_p+1:])
            
    # return the sorted array
    return array

if __name__ == '__main__':
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(quicksort(test))

    test = [33.3, 6.6, 23.4, 10.65, 2.4, 45.6]
    print(quicksort(test))

    test = ['c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r']
    print(quicksort(test))
