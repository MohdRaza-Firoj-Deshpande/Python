"""

Introduction to Tuples
Creating Tuples
Accessing Tuple Elements
Tuple Operations
Immutable Nature of Tuples
Tuple Methods
Packing and Unpacking Tuples
Nested Tuples
Practical Examples and Common Errors
Introduction to Tuples
Explanation:

Tuples are ordered collections of items that are immutable. They are similar to lists, but their immutability makes them different.

"""

tuple=()
print(tuple)
print(type(tuple))

lst =list()
print(type(lst))


tpl=()
print(type(tpl))

numbers=(1,2,3,4,5,6)
print(type(numbers))

print(numbers)

lst = list((1,2,3,4,5,6))
print(lst)

mixed_tuple=(1,"Hello World",3.14, True)
print(mixed_tuple)

print(numbers)

print(numbers[2])
print(numbers[-1])

print(numbers[0:4])
print(numbers[::-1])

## Tuple Operations

concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)

print(mixed_tuple * 3)

print(numbers *3)


## Immutable Nature Of Tuples
## Tuples are immutable, meaning their elements cannot be changed once assigned.
"""
lst=[1,2,3,4,5]
print(lst)

lst[1]="Krish"
print(lst)

numbers[1]="Krish"

"""

## Tuple Methods
print(numbers.count(1))
print(numbers.index(3))

## Packing and Unpacking tuple
## packing
packed_tuple=1,"Hello",3.14
print(packed_tuple)

a,b,c =packed_tuple
print(a)
print(b)
print(c)


print("---")

## Unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last,code=numbers
print(first)
print(middle)
print(last)


## Nested Tuple
## Nested List
lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"]]
lst[0][0:3]

lst=[[1,2,3,4],[6,7,8,9],(1,"Hello",3.14,"c")]
lst[2][0:3]

nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))

## access the elements inside a tuple
print(nested_tuple[0])
print(nested_tuple[1][2])

print("#----#")
## iterating over nested tuples
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")#Printing on the same line (with a space)
    print()
    

"""
 Conclusion
Tuples are versatile and useful in many real-world scenarios where an immutable and ordered collection of items is required. They are commonly used in data structures, function arguments and return values, and as dictionary keys. Understanding how to leverage tuples effectively can improve the efficiency and readability of your Python code.

 
 """   