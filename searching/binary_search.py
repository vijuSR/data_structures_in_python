def binary_search(input_array, value):

    l = 0
    h = len(input_array) - 1
    
    while l <= h:
        mid = (l + h) / 2
        v = input_array[mid]
        
        if value > v:
            l = mid + 1
        elif value < v:
            h = mid - 1
        else:
            return mid
            
    return -1


if __name__ == '__main__':
    test_list = [1,3,9,11,15,29]
    test_val1 = 25
    test_val2 = 15

    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))
