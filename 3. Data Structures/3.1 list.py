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

## Remove and return the last element
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)

index=fruits.index("cherry")
print(index)

pop= fruits.pop()
print(pop)

fruits.insert(1,"cherry")
print(fruits)

print(fruits.count("apple"))

fruits.sort() # Sort
print(fruits)

fruits.reverse() # Reverse the fruits
print(fruits)


fruits.clear()## Remove all items from the list
print(fruits)

fruits = ['apple', 'cherry', 'Avacado', 'cherry']
print(fruits)


# slicing List
numbers =[1,2,3,4,5,6,7,8]
print(numbers[1:7])
print(numbers[2:7])
print(numbers[0:5])
print(numbers[1:])
print(numbers[:3])
print(numbers[::-1])
print(numbers[::2])
print(numbers[::3])
print(numbers[::-2])
print(numbers[::3])
print(numbers[::-2])

### Iterating Over List
for number in numbers:
    print(number)

## Iterating with index
for index, number in enumerate(numbers): # enumarate function is used to get the index and the element at the same time
    print(index,number)    

lst=[]
for x in range(10):
    lst.append(x**2)

print(lst)    

lst1=[x**2 for x in range(10)]
print(lst1)


"""
List Comprehension
Basics Syantax [expression for item in iterable]

with conditional logic [expression for item in iterable if condition]

Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]

"""

### Basic List Comphrension

lst=[num**2 for num in range(10)]
print(lst)

lst=[num**3 for num in range(30)]
print(lst)

### List Comprehension with Condition
lst=[]
for i in range(1,10):
    if i%2==0:
        lst.append(i)

print(lst)

odd_number=[num for num in range(1,10) if num%2!=0]
print(odd_number)

even_number=[num for num in range(1,10) if num%2==0]
print(even_number)


# Nested List
lst1 =[1,2,3,4,5]
lst2=['a','b','c','d','e']

lst3=[[lst1,lst2] for i in lst1 for j in lst2]

print(lst3)


## List Comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
check=[len(words) for i in words]
print(check)
