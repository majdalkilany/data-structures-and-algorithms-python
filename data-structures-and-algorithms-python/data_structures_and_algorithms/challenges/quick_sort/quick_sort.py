def quick_sort(alist, left, right):
    """sorts array using partition and pivot value"""
    if left < right:
        position = partition(alist, left, right)
        quick_sort(alist, left, position - 1)
        quick_sort(alist, position + 1, right)

def partition(alist, left, right):
    pivot = alist[right]

    low = left - 1

    for i in range(left, right):
        if alist[i] <= pivot:
            low += 1
            swap(alist, i, low)

    swap(alist, right, low + 1)
    return low + 1

def swap(alist, i, low):
    temp = alist[i]
    alist[i] = alist[low]
    alist[low] = temp
