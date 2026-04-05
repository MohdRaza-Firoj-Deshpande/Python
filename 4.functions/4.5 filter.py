"""
Filter function

A filter function constructs an iteratorfrom elements of an iterable for which a function returns true.
 It is used to filter out items from a list (or any other iterable) based on a condition.
"""

def even(num):
    if num%2==0:
        return True
    
print(even(24))   

lst=[1,2,3,4,5,6,7,8,9,10,11,12]

main = list(filter(even,lst))
print(main)

## filter with a Lambda Function
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers))
print(greater_than_five)