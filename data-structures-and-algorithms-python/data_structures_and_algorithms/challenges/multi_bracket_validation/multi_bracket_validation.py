def multi_bracket_validation(input) :
        sbr = []
        sbl = []
        cbr = []
        cbl = []
        br =  []
        bl =  []

        for i in input : 
            if  i == '{' :
              cbr.append(i)
            elif i =="}" :
                cbl.append(i)

            elif  i == '[' :
                sbr.append(i)
            elif i =="]" :
                sbl.append(i)


            elif i == '(' :
                sbr.append(i)
            elif i ==")" :
                sbl.append(i)
                



        if len(sbl) == 0 and len(sbr) ==0 and len(cbr) == 00 and len(cbl) ==0 and len(bl) == 0 and len(br) == 0: 
            return False

        elif len(sbl) == len(sbr) and( len(cbr) == len(cbl)) and len(bl) == len(br) : 
            return True
        else : 
            return False


if __name__ == "__main__":
    multi_bracket_validation('{{{}m}}}m}}')


