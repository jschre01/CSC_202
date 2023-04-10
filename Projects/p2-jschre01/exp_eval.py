from stack_array import Stack 

# You do not need to change this class
class PostfixFormatException(Exception):
    pass



def is_number(input_str):
    "Evaluates an input number and returns if it is a number or not"
    "Input argument: a string that is either an operator, operand, or invalid token"

    try:
        input_str = int(input_str)
        return True
    except ValueError:
        pass
    try:
        input_str = float(input_str)
        return True
    except ValueError:
        return False

def is_operand(input_str):
    "Boolean function that evaluates an input string and decides if it is an operator or not"
    "Input argument: a string that is either an operator, operand, or invalid token"
    if(input_str == '<<' or input_str == '>>'):
        return True
    elif(input_str == '**'):
        return True
    elif(input_str == '/' or input_str == '*'):
        return True
    elif(input_str == '+' or input_str == '-'):
        return True
    else:
        return False

def string_converter(input_str):
    """Function that takes in an input string and formats it into a list. Each new
    character added to the list is everything that is a part of a specific operand or
    operator. Each new addition is cut off when the program reaches a space."""
    """Input argument: a string (in this instance the string that is passed to be converted
    or evaluated."""
    new_list = []
    new = ''
    for i in range (len(input_str)):
        if(input_str[i] == ' '):
            new_list.append(new)
            new = ''
        elif(i == len(input_str)-1):
            new = new + input_str[i]
            new_list.append(new)
        else:
            new = new + input_str[i]
    return new_list
            

    
def postfix_eval(input_str):
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""

    stack = Stack(30)
    postfix_list = string_converter(input_str)    
    for i in range(len(postfix_list)):
        char = postfix_list[i]
        if(is_number(char)):
            if("." in char):
                new = float(char)
            else:
                new = int(char)
            stack.push(new)
        elif(is_operand(char)):
            if(stack.size() == 1):
                raise PostfixFormatException('Insufficient operands')
            else:
                if(char == '+'):
                    two = stack.pop()
                    one = stack.pop()
                    new = one + two
                    stack.push(new)
                elif(char == '-'):
                    two = stack.pop()
                    one = stack.pop()
                    new = one - two
                    stack.push(new)
                elif(char == '*'):
                    two = stack.pop()
                    one = stack.pop()
                    new = one * two
                    stack.push(new)
                elif(char == '/'):
                    two = stack.pop()
                    if(two == 0):
                        raise ValueError('Cannot divide by 0')
                    one = stack.pop()
                    new = one/two
                    stack.push(new)
                elif(char == '**'):
                    two = stack.pop()
                    one = stack.pop()
                    new = one ** two
                    stack.push(new)
                elif(char == '<<'):
                    two = stack.pop()
                    if(isinstance(two, float)):
                        raise PostfixFormatException('Illegal bit shift operand')
                    one = stack.pop()
                    if(isinstance(one, float)):
                        raise PostfixFormatException('Illegal bit shift operand')
                    new = one << two
                    stack.push(new)
                elif(char == '>>'):
                    two = stack.pop()
                    if(isinstance(two, float)):
                        raise PostfixFormatException('Illegal bit shift operand')
                    one = stack.pop()
                    if(isinstance(one, float)):
                        raise PostfixFormatException('Illegal bit shift operand')
                    new = one >> two
                    stack.push(new)
        else:
            print(char)
            print("This is what is screwing up ^^")
            raise PostfixFormatException('Invalid token')
    if(stack.size() > 1):
        raise PostfixFormatException('Too many operands')
    return stack.peek()

def has_lower_precedence(op1, op2):
    """boolean expression that computes whether op2 has lower precedence then op1,
    taking into account associativity as well"""

    """Input argument: op 1 is always an operator, as the method is only called when
    an operator is present in the expression. op 2 is also always an operator"""
    
    if(op1 == '**'):
        if(op2 in '<<>>'):
            return False
        else:
            return True
            
    else:
        if(op2 in '<<>>'):
            return False
        elif(op2 == '**'):
            if(op1 in '<<>>'):
                return True
            else:
                return False
        elif(op2 in '*/'):
            if(op1 == '**' or op1 in '<<>>'):
                return True
            else:
                return False
        else:
            if(op1 == '**' or op1 in '*/' or op1 in '<<>>'):
                return True
            else:
                return False
        
    

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    post = []
    infix_list = string_converter(input_str)
    stack = Stack(30)
    for i in range(len(infix_list)):
        if(is_number(infix_list[i])):
            post.append(infix_list[i])
        elif(infix_list[i] == '('):
            stack.push(infix_list[i])
        elif(infix_list[i] == ')'):
            while(stack.peek() != '('):
                post.append(stack.pop())
            stack.pop()
        elif(is_operand(infix_list[i])):
            while(stack.is_empty() == False and stack.peek() != '(' and not has_lower_precedence(infix_list[i], stack.peek())):
                post.append(stack.pop())
            stack.push(infix_list[i])
    while(stack.is_empty() == False):
        post.append(stack.pop())
    post_str = post[0]
    for i in range (1,len(post)):
        post_str = post_str + ' ' + post[i]   
    return post_str



def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""

    stack = Stack(30)
    prefix_list = string_converter(input_str)
    for i in range(len(prefix_list)-1, -1, -1):
        if(is_number(prefix_list[i])):
            stack.push(prefix_list[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new = op1 + ' ' + op2 + ' ' + prefix_list[i]
            stack.push(new)
    #while(stack.size() != 1):
        #op1 = stack.pop()
        #op2 = stack.pop()
        #new = op1 + ' ' + op2
        #stack.push(new)
    return stack.pop()


