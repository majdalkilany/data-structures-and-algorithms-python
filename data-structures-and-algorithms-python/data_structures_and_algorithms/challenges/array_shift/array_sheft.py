def array_sheft(arr,n):
    for i in range(len(arr)) :
        if n>arr[i-1] and n<arr[i] :
            arr.insert(i,n)
    return arr
    print(arr)
print(array_sheft([3,4,6,8],5))
