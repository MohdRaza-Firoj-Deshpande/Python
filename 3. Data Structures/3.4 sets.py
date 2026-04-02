"""
Sets
Sets are a built-in data type in Python used to store collections of unique items. 
They are unordered, meaning that the elements do not follow a specific order, and they do not
 allow duplicate elements. Sets are useful for membership tests, eliminating duplicate entries,
   and performing mathematical set operations like union, intersection, difference, and symmetric
     difference.
"""

##create a set
my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))


my_empty=set()
print(type(my_empty))

my_set= set([1,2,3,4,5])
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(5)
print(my_set)

my_set.discard(11)  

"""
The discard() method removes the specified item from the set.

This method is different from the remove() method, because the remove()
 method will raise an error if the specified item does not exist, and the discard()
   method will not.
"""
print(my_set)


my_set.clear()
print(set)


## MAthematical Operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

union_set = set1.union(set2)
print(union_set)

intersection_set=set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2)
print(set1)

set1={1,2,3,4,5,6}
set2={1,2,40,12,45}
## Difference 
print(set1.difference(set2))

print(set2.difference(set1))

##symentric Diffrence

"""
The symmetric_difference() method returns a set that contains all items from both set, 
but not the items that are present in both sets
"""

print(set1.symmetric_difference(set2))

## Sets Methods
set1={1,2,3,4,5}
set2={3,4,5}

## is subset
print(set1.issubset(set2))

print(set1.issuperset(set2))

lst=[1,2,2,3,4,4,5]

set(lst)

### Counting Unique words in text

text="In this tutorial we are discussing about sets"
words=text.split()

## convert list of words to set to get unique words

unique_words=set(words)
print(unique_words)
print(len(unique_words))

"""
Conclusion
Sets are a powerful and flexible data type in Python that provide a way to store collections of 
unique elements. They support various operations such as union, intersection, difference, and symmetric difference, 
which are useful for mathematical computations. Understanding how to use sets and their associated methods can help you 
write more efficient and clean Python code, especially when dealing with unique collections and membership tests.
"""