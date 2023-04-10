
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    char_list = ['A', 'B', 'C', 'D', 'E', 'F'] #list to assign remainders greater than 10 to numbers
    if(num//b == 0): # bass case for recursive function
        r = num%b    # finding final remainder (first digit in converted number returned)
        if(r >= 10):  #checking if remainder is greater than 10
            r = char_list[r%10] #converting remainders greater than 10 to corresponding letter
        else:
            r = str(r) #if number is not greater than 10, converting it to string
        return r
    else:
        r = num%b #finding initial remainder, to be added to converted number
        num = num//b #finding new number to be implemented again recursively
        if(r >= 10): #same method as in statement in base case, used to convert numbers greater than 10 to numbers
            r = char_list[r%10]
        else:
            r = str(r)
        return convert(num,b) + r #recursive call 
