#Task 1 - Importing and Using Functions
from math import sqrt
root = sqrt(49)
result = sqrt(2401)
print("Square root of 2401 is:", result)

#Task 2
from math import log2
result = log2(1024)
print("Log base 2 of 1024 is:", result)

from math import pi
print("The value of pi is", pi)

#Task 3 - Defining Functions
def displayTwice(msg):
    print(msg)
    print(msg)

displayTwice("From the river to the sea!")
displayTwice("Palestine will free!")
displayTwice("Free Free Palestine🇵🇸🇵🇸!")

#Task 4 - Docstrings
def displayTwice(msg):
    """
    Mary had a little lamb
    His fleece was white as snow
    Everywhere Mary went
    Her little lamb was sure to go

    """
    print(hello)
    print(hello)
help(displayTwice)

#Task 5
def findMax (a,b):
    """Finds the maximum of two values."""
    if (a > b):
        max = a
    else:
        max = b
    return max

#Task 6 - Default Arguements
def displayMessage(msg, suffix = "?"):
    """Prints a message with a suffix."""
    print(msg, suffix)

def multiply_values(num1, num2=None):
    """
    Multiplies two numeric values together.

    :param num1: (int or float): First numeric value.
    :param num2: (int or float, optional): Second numeric value.
    :return: int or float: Result of the multiplication.
    """
    if num2 is not None:
        return num1 * num2
    else:
        return num1 * num1

#Task 7 - Keyboard Arguements
def someFunc(x, y, z):
    print("x is", x, "\ny is", y,"\nz is", z)

    someFunc(1,2,3)

#Task 8 -
print("1", "2", "3", sep= "-")

#Task 9 - Arbitrary Length Arguements Lists
def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)

#Task 10 - Lambda Expressions
hypot = lambda a,b : math.sqrt(a * b + b * b)

#Task 11
to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60
seconds1 = to_seconds(1, 30)
seconds2 = to_seconds(2, 45)

print("Equivalent seconds (1 hour 30 minutes):", seconds1)
print("Equivalent second (2 hours 45 minutes):", seconds2)