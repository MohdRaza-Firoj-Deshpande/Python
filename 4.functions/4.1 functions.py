"""
Functions in Python
Video Outline:

Introduction to Functions
Defining Functions
Calling Functions
Function Parameters
Default Parameters
Variable-Length Arguments
Return Statement
Introduction to Functions
Definition:

A function is a block of code that performs a specific task. Functions help in organizing code, 
reusing code, and improving readability.
"""


## syntax
def function_name(parameters):
    """This is functions Docstring"""
    #Function body
    #return expression

#why function
num =10

if num%2==0:
    print("Even")
else:
    print("odd")        


#Now if we want to resue the code we can create a function for it

def even_or_odd(num):
    """This is even odd program"""
    if num%2==0:
        print("Even")
    else:
        print("odd") 

# we can call the even_or_odd program wherever we want 
even_or_odd(20)

def add(a,b):
    """This is a addition program"""
    print(a+b)

add(2,3)    

def greet(name):
    print(f"{name} Welcome to paradise")

greet("Tom")

### Variable Length Arguments
## Positional And Keywords arguments

def print_number(*krish):
    for number in krish:
        print(number)

print_number(1,2,3,4,5,"krish") 

## Positional arguments
def print_numbers(*args):
    for number in args:
        print(number)
        
print_numbers(1,2,3,4,5,6,7,8,"Krish")

### Keywords Arguments
def print_details(**kwrags):
    for key,value in kwrags.items():
        print(f"{key}:{value}")
print_details(name="Krish",age="32",country="India")


def details(*args,**kwrags):
    for v in args:
        print(v)

    for key,value in kwrags.items():
        print(f"{key}:{value}") 

details(1,2,3,4,5,6,"krish",name="krish",age=24)

# Return statement

def add(a,b):
    print(a+b)


### Return statements
def multiply(a,b):
    return a*b

multiply(2,3)    
