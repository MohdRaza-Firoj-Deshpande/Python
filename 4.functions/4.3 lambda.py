"""

Lambda Functions in Python
Lambda functions are small anonymous functions defined using the lambda keyword.
 They can have any number of arguments but only one expression. 
 They are commonly used for short operations or as arguments to higher-order functions.
"""

def add(a,b):
    return(a+b)
print(add(5,4))


addition = lambda a,b:a+b
print(addition(5,6))

substraction = lambda a,b :a-b
print(substraction(4,6))

multiplication = lambda a,b :a*b
print(multiplication(4,6))

division = lambda a,b: a/b
print(division(4,2))

addition1=lambda x,y,z:x+y+z
print(addition1(12,13,14))


## map()- applies a function to all items in a list
numbers=[1,2,3,4,5,6]
def sqaure(numbers):
    return numbers**2

#print(sqaure(numbers))
 # we will get error TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

## map()- applies a function to all items in a list
maping = list(map(lambda x:x**2 , numbers))
print(maping)
