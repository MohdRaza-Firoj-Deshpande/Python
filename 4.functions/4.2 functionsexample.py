
"""
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
    if not any (char.islower() for char in password):
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