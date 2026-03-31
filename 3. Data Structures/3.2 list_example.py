"""
Real-World Examples Using Lists in Python
Lists are one of the most commonly used data structures in Python, thanks to their versatility and ease of use. 
Here are several practical examples that illustrate their use in real-world scenarios

"""

"Example 1. Manage A To Do List"

"Create a To Do List To Keep Track OF Tasks"



to_do_list=["Buy Groceries","Clean the house","Pay bills"]

## Adding to task
to_do_list.append("Schedule meeting")
to_do_list.append( "Go For a Run")

## Removing a completed task
to_do_list.remove("Clean the house")

## checking if a task is in the list
if "Pay bills" in to_do_list:
    print("Don't forgrt to pay the utility bills")

print("To Do List remaining")
for task in to_do_list:
    print(f"{task}") 


"""
Example 2: Organizing Student Grades
Create a list to store and calculate average grades for students

"""  

# Organizing student grades
grades = [85, 92, 78, 90, 88]

# Adding a new grade
grades.append(95)


# Calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"{average_grade:.2f}")

higest_grade= max(grades)
lowest_grade = min(grades)

print(f"Higest Grade : {higest_grade}")
print(f"Lowest Grade :{lowest_grade}")


"""Example 3: Managing An Inventory
Use a list to manage inventory items in a store"""

# Managing an inventory
inventory = ["apples", "bananas", "oranges", "grapes"]

# Adding a new item
inventory.append("strawberries")

# Removing an item that is out of stock
inventory.remove("bananas")

# Checking if an item is in stock
item = "oranges"
if item in inventory:
    print(f"{item} are in stock.")
else:
    print(f"{item} are out of stock.")

# Printing the inventory
print("Inventory List:")
for item in inventory:
    print(f"- {item}")


"""
Example 4:Collecting User Feedback
Use a list to collect and analyze user feedback.
...

"""    