def array_binary_search (val,my_list):
    found = False
    first = 0
    last = len(my_list)-1
    while first <=last and found == False :
        index_item=(first+last)//2
        if my_list[index_item]==val :
            found =True
            return index_item
        else:
            if my_list[index_item]< val :
                first =  index_item+1
            else :
                last = index_item-1
    if found != False :
        return index_item
    else:
        return 'the value is not in the lest '
print(array_binary_search(4,[1,2,3,4,5,6,7,8,9,10,11,12]))
