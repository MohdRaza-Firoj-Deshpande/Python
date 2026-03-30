a=100


## Declaring And Assigning Variables

age=32
height=6.1
name="Krish"
is_student=True

## printing the variables

print("age :",age)
print("Height:",height)
print("Name:",name)

## Naming Conventions
## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive

#valid variable names

first_name="KRish"
last_name="Naik"


# Invalid variable names
#2age=30
#first-name="Krish"
##@name="Krish"


## case sensitivity
name="Krish"
Name="Naik"


## Understnading Variable types
## Python is dynamically typed,type of a variable is determined at runtime
age=25 #int
height=6.1 #float
name="KRish" #str
is_student=True #bool

print(type(name))

## Type Checking and Conversion

type(height)


age=25
print(type(age))

# Type conversion
age_str=str(age)
print(age_str)
print(type(age_str))

age='25'
print(type(int(age)))

name="Krish"
#int(name)

height=5.11
type(height)


float(int(height))  

## Dynamic Typing
## Python allows the type of a vraible to change as the program executes
var = 10
print(var, type(var))

var ="Hello"
print(var,type(var))

var =3.14
print(var,type(var))

#Simple Calculator

num1 = float(input("Please Enter 1st Number "))
num2 = float(input("Please Enter 2nd Number "))

sum=num1+num2
diffrence = num1-num2
product =num1*num2
quotient = num1/num2

print("Sum:",sum)
print("Diffrence:",diffrence)
print("Product:",product)
print("Quotient:",quotient)

'''
Conclusion:
Variables are essential in Python programming for storing and manipulating data. Understanding how to declare, assign, and use variables effectively is crucial for writing functional and efficient code. Following proper naming conventions and understanding variable types will help in maintaining readability and consistency in your code.


'''