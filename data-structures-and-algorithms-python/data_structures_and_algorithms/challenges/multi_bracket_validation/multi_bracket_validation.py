def multi_bracket_validation(input) :
    raight = ["[","{","("] 
    left = ["]","}",")"] 
    check = [] 
    
    for ch in input: 

        if ch in raight: 
            check.append(raight.index(ch)) 

        elif ch in left: 
            if ((len(check) > 0) and (left.index(ch) == check[-1])): 
                check.pop() 
            else: 
                return False

    if len(check) == 0: 
        return True
    else: 
        return False


if __name__ == "__main__":
    print(multi_bracket_validation('(]') )


