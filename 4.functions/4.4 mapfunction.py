"The map() Function in Python "
"A map() function applies a given function to list  or any other iterable and return a map object (itreator)"
"This is particularly helfull in transforing data in a list comprehensievly"
" "

def square(x):
    return x*x

square(10)

numbers=[1,2,3,4,5,6,7,8]
a = list(map(square,numbers))
print(a)


## Lambda function with map
numbers=[1,2,3,4,5,6,7,8]
b =list(map(lambda x:x**2, numbers))
print(b)


### Map multiple iterables

numbers1=[1,2,3]
numbers2=[4,5,6]

add=list(map(lambda x,y:x+y, numbers1,numbers2))
print(add)

### Map update to uppper
words=['apple','banana','cherry']
con_upper=list(map(str.upper,words))
print(con_upper)

words=['APPLE', 'BANANA', 'CHERRY']
con_lower=list(map(str.lower,words))
print(con_lower)


def get_name(person):
    return person['name']

people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33}
]

get = list(map(get_name,people))
print(get)