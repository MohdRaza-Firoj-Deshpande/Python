
"""w
Functions Examples
Example 1: Temperature Conversion
"""


def convert_temperature(temp,unit):
    """This function converts temperature between Celsius and Fahrenheit"""
    if unit=='C':
        return temp * 9/5 + 32  ## Celsius To Fahrenheit
    elif unit=="F":
        return (temp-32)*5/9 ## Fahrenheit to celsius
    else:
        return None

print(convert_temperature(25,'C'))
print(convert_temperature(77,'F'))

"""
Example 2: Password Strength Checker
"""

def password_strenght_cheker(password):
    if len(password)<8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isnumeric() for char in password):
        return False
    if not any(char in '@#$%&*' for char in password):
        return False
    return True
    
print(password_strenght_cheker("1235678u")  )  
print(password_strenght_cheker("1235678uE@")  )  


def panlindrome(s):
    s=s.lower().replace(" ","")
    if s==s[::-1]:
        return True


print(panlindrome("A man a plan a canal Panama"))


#factorial( 6! = 1 *2 *3 *4 *5 *6)

def factorial(n):
    if n==0:
        return 1
    else:
         return n* factorial(n-1)

print(factorial(6))

import os

os.chdir(r'4.functions')  # paste your folder path here

print(os.getcwd())  # confirm it changed

print("-->")

def word_counter(filename):
    counter={}
    with open(filename,'r') as file:
        for line in file:
            print (line)
        words=line.split()   
        print(words)
        for word in words:
            word=word.lower().strip('!@#$%^&*')
            print(word)
            counter[word]= counter.get(word,0)+1
    return counter


filename='main.txt'
con =  word_counter(filename)
print(con)


def local_counter(name):
    counts={}

    b= name.split()
    for e in b:
        e=e.lower().strip('!@#$%^')
        print(f"{e},e working")
        counts[e] = counts.get(e,0)+1

    return counts
name ='Aeiou olkjo@#$'
com=  local_counter(name)
print(com)


#Email address Validation
import re

def is_email_valid(email):
    """This function checks if the email is valid."""
    pattern =  r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern,email) is not None

print(is_email_valid("joe.doe@gmail.com"))
print(is_email_valid('joe.doe.,gmail.com'))