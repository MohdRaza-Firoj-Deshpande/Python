"""
Conditional Statements (if, elif, else)
1.if Statement
2.else Statement
3.elif Statement
4.Nested Conditional Statements
5.Practical Examples
6.Common Errors and Best Practices

"""

age=20

if age>=20:
    print("You Are aloowed to vote")

# Else
if age>=20:
    print("You Are alowed to vote")
else:
    print("You are a minor")


age=17
if age < 13:
    print("You are a Child")
elif age <18:
    print("You are a Teenager")
else:
    print("You are a Adult")

## Nested Condiitonal Statements

# You can place one or more if, elif, or else statements inside another if, elif, or else statement to create nested conditional statements.

## number even ,odd,negative

num=int(input("Enter the Number"))
if num>0:
    if num%2==0:
        print("The Number is Even")
    else:
        print("The Number is Odd") 

else:
    print("The Number is 0 or Negative")           
    

## Practical Examples

## Determine if a year is a leap year using nested condition statement

year=int(input("Enter the year"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")

else:
    print(year,"is not a leap year")


## Assignment
## Simple Calculator program
# Take user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform the requested operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

print("Result:", result)



# Take user input
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()

# Determine ticket price
if age < 5:
    price = "Free"
elif age <= 12:
    price = "$10"
elif age <= 17:
    if is_student == 'yes':
        price = "$12"
    else:
        price = "$15"
elif age <= 64:
    if is_student == 'yes':
        price = "$18"
    else:
        price = "$25"
else:
    price = "$20"

print("Ticket Price:", price)


"""
Complex Example 3: Employee Bonus Calculation
Calculate an employee's bonus based on their performance rating and years of service.
"""
# Employee bonus calculation

# Take user input
years_of_service = int(input("Enter years of service: "))
performance_rating = float(input("Enter performance rating (1.0 to 5.0): "))

# Determine bonus percentage
if performance_rating >= 4.5:
    if years_of_service > 10:
        bonus_percentage = 20
    elif years_of_service > 5:
        bonus_percentage = 15
    else:
        bonus_percentage = 10
elif performance_rating >= 3.5:
    if years_of_service > 10:
        bonus_percentage = 15
    elif years_of_service > 5:
        bonus_percentage = 10
    else:
        bonus_percentage = 5
else:
    bonus_percentage = 0

# Calculate bonus amount
salary = float(input("Enter current salary: "))
bonus_amount = salary * bonus_percentage / 100

print("Bonus Amount: ${:.2f}".format(bonus_amount))


stored_name = 'Admin'
stored_password = 'Admin@123'

check_1 = input("Please Enter Username")
check_2 = input("Please Enter The Passoword")

if check_1==stored_name:
    if check_2 ==stored_password:
        print("Login Sucessfull")
    else:
        print("Incorrect Password") 
else:
    print("Username Not Found")           
