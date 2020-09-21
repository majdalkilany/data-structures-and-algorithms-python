def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2 
        left = my_list[:mid]
        right = my_list[mid:] 

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]:
              my_list[k] = left[i]
              i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            my_list[k] = left[i] 
            i += 1
            k += 1

        while j < len(right):
            my_list[k]=right[j]
            j += 1
            k += 1
    return my_list

if __name__ == "__main__":
    my_list = [54,26,93,17,77,31,44,55,20]
    merge_sort(my_list)
    print(my_list)
