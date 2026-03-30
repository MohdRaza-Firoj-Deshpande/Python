"""
Introduction To Lists
Lists are ordered, mutable collections of items.
They can contain items of different data types.

"""
lst=[]
print(type(lst))


names=["Krish","Jack","Jacob",1,2,3,4,5]
print(names)

mixed_list=[1,"Hello",3.14,True]
print(mixed_list)

### Accessing List Elements

fruits=["apple","banana","cherry","kiwi","gauva"]
print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-1])

print(fruits[1:])
print(fruits[1:3])

## Modifying The List elements
fruits

fruits[1]="Watermelon"
print(fruits)

fruits[1:]="watermelon"
print(fruits)

fruits=["apple","banana","cherry","kiwi","gauva"]
print(fruits)

fruits.insert(1,"Avacado")
print(fruits)

fruits.remove("banana")
print(fruits)