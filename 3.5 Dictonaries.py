
"""
Dictionaries
Video Outline:

Introduction to Dictionaries
Creating Dictionaries
Accessing Dictionary Elements
Modifying Dictionary Elements
Dictionary Methods
Iterating Over Dictionaries
Nested Dictionaries
Dictionary Comprehensions
Practical Examples and Common Errors
Introduction to Dictionaries
Dictionaries are unordered collections of items. 
They store data in key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any type.
"""

## Creating Dictionaries
empty_dict={}
print(type(empty_dict))

empty_dict=dict()
empty_dict

student={"name":"Krish","age":32,"grade":24}
print(student)
print(type(student))

# Single key is slways used
student={"name":"Krish","age":32,"name":24}
print(student)

## accessing Dictionary Elements
student={"name":"Krish","age":32,"grade":'A'}
print(student)

## Accessing Dictionary elements
print(student['grade'])
print(student['age'])

## Accessing using get() method
print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name',"Not Available"))

## Modifying Dicitonary Elements
## Dictionary are mutable,so you can add, update or delete elements
print(student)

student["age"]=33  ##update value for the key
print(student)
student["address"]="India" ## added a new key and value
print(student)

del student['grade'] ## delete key and value pair

print(student)

## Dictionary methods

keys=student.keys() ##get all the keys
print(keys)
values=student.values() ##get all values
print(values)

items=student.items() ##get all key value pairs
print(items)


## shallow copy
student_copy=student
print(student)
print(student_copy)

student["name"]="Krish2"
print(student)
print(student_copy)

student_copy1=student.copy() ## shallow copy
print(student_copy1)
print(student)

student["name"]="KRish3"
print(student_copy1)
print(student)

### Iterating Over Dictionaries
## You can use loops to iterate over dictionatries, keys,values,or items

## Iterating over keys
for keys in student.keys():
    print(keys)

## Iterate over values
for value in student.values():
    print(value)

## Iterate over key value pairs
for key,value in student.items():
    print(f"{key}:{value}")

## Nested Disctionaries
students={
    "student1":{"name":"Krish","age":32},
    "student2":{"name":"Peter","age":35}
}
print(students)

## Access nested dictionaries elementss
print(students["student2"]["name"])
print(students["student2"]["age"])

students.items()

## Iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")

## Dictionary Comphrehension
squares={x:x**2 for x in range(5)}
print(squares)

## Condition dictionary comprehension
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)

## Practical Examples

## USe a dictionary to count he frequency of elements in list

numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)

## Merge 2 dictionaries into one

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)


"""
Conclusion
Dictionaries are powerful tools in Python for managing key-value pairs. 
They are used in a variety of real-world scenarios, such as counting word frequency, 
grouping data, storing configuration settings, managing phonebooks, tracking inventory, 
and caching results. Understanding how to leverage dictionaries effectively can greatly enhance
 the efficiency and readability of your code.
"""