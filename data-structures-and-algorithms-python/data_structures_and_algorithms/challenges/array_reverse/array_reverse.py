def reverse_array(arr):
    """Reverses a list

    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    rev_arr = []
    for i in range(0,len(arr)) :
        rev_arr.append(arr[len(arr)-i -1])
        print(arr[len(arr)-1-i ])
    return rev_arr
print(reverse_array([1,2,3,4]))