def perm_gen_lex(a): #function that returns all the possible permutations of a string in dictionary order (given in dictionary order)
    new_list=[]
    if(len(a) == 0):
        return new_list
    if(len(a) == 1):
        new_list.append(a)
    else:
        
        for i in range(len(a)):
            char = a[i]
            s = a[:i]+a[i+1:]
            perm_list = perm_gen_lex(s)
            for i in range(len(perm_list)):
                add = char + perm_list[i]
                new_list.append(add) 
    return new_list 

            
        
        
        
        
        

