"""
Introduction to Loops

1.for Loop
    Iterating over a range
    Iterating over a string
2.while Loop

3.Loop Control Statements

    break
    continue
    pass

4.Nested Loops

5.Practical Examples and Common Errors

"""

range(5)
print(range)


for i in range(5):
    print(i)

print("----")

for i in range(1,6):
    print(i)    

print("----")

for i in range(1,6,2): # step Current + Preceding One in forward direction
    print(i)    

print("----")

for i in range(10,6,-2):# step Current + Previous One in forward direction the starting number should be greater
    print(i)

print("----")

for i in range(10,1,-2):
    print(i)

print("----")
str ="Python Course"
for i in str:
    print(i)

# while Loop 
# The While Loop will execute as long as the condition is True

count=0

while count<5:
    print(count)
    count=count+1


print("----")
## Loop Control Statements

## break
## The break statement exits the loop permaturely

## break sstatement

for i in range(10):
    if i ==5:
        break
    print(i)

print("----")

## continue

## The continue statement skips the current iteration and continues with the next.
for i in range(10):
    if i%2==0:
        continue
    print(i)

print("----")

## pass
## The pass statement is a null operation; it does nothing.

for i in range(5):
    if i==3:
        pass
    print(i)    

print("----")

for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")    


print("----")

## Examples- Calculate the sum of first N natural numbers using a while and for loop

## while loop 

n=10
sum=0
count=1

while count<=n:
    sum =sum+count
    count= count + 1

print("Sum of first 10 natural number:",sum)



print("----")

sum=0
for i in range(11):
    sum=sum+i

print(sum)