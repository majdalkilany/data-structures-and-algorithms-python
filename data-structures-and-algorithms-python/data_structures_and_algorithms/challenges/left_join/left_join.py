def left_join(hashmap1, hashmap2):


    output = []

    for key in hashmap1: 
        row = []
        row.append(key) 
        row.append(hashmap1[key]) 

        try:
            if hashmap2[key]: 
                row.append(hashmap2[key]) 
        except:
            row.append(None)

        output.append(row) 
    return output
