import sys
sys.setrecursionlimit(2000)
def bears(n): #Method to find if a number can pass the "Teddy Bear Picnic" Game
    bool_1 = False
    if(n == 42):
        return True
    elif(n < 42):
        return False
    elif(n%5 == 0 or n%4 == 0 or n%3 == 0 or n%2 == 0):
        if((n%2 == 0) and not (bool_1)):
            bool_1 = bears(n/2)
        if((n%5 == 0) and not (bool_1)):
            bool_1 = bears(n-42) 
        if((n%4 == 0 or n%3 == 0) and not (bool_1)):
            sub = (n%10)*((n%100)//10)
            if(sub > 0):
                bool_1 = bears(n-sub)
    else:        
        return False

    return bool_1
        
            
            
            
        
