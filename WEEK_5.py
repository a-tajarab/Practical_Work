# my_program.py
#Task 1 - Executing a file
number = input ("Enter a number:")
number = int(number)
print("The number entered was", number)
if (number %2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")

#Task 2 - Adding comments to each statement


#Task 3 - Independent execution
number_2 = input ("Enter a number:")
number_2 = int(number_2)
print("The number you entered was", number_2)
if (number_2 %10) == 0:
    print("That number is divisible by 10")
else:
    print("That number is not divisible by 10")

#Task 4 - total.py
import sys
count = len(sys.argv)
total = number + number_2
while count > 1:
    count -= 1
    total += 1
print("Total is", total)
number_3 = input("Enter in your age:")
number_3 = int(number_3)
print("Wow what a lovely number", number_3, "love it")
print("Right! Let's get onto some fun stuff")
print("Disclaimer there is insensitive words")
print("Would you like to proceed?")
response = input("Y or N:")
if response == "Y":
    print("Fabulous!")
    if 0<= number_3 < 10:
            print("You are boss!")
    elif 10<= number_3 < 20:
            print("You will become a star!")
    elif 20<= number_3 < 30:
            print("Life will get easier. Hang on.")
    elif 30<= number_3 < 40:
            print("You feel old now?")
    elif 40<= number_3 < 50:
            print("Happy days")
    elif 50<= number_3 < 60:
            print("Half-life hahaha")
    elif 60<= number_3 < 70:
            print("Are you depressed?")
    elif 70<= number_3 < 80:
            print("You seem wise!")
    elif 80<= number_3 < 90:
            print("You have a bright future ahead of you")
    elif 90<= number_3 < 100:
            print("Stay healthy!")
if response == "N":
    print("Oh well I guess you will miss the fun!:(")


#Task 5 - Module test
def average(numbers):
    return sum(numbers) / len(numbers)
from my_utils import average
number1 = [10, 23, 30]
result1 = average(number1)
print("Average is", result1)

#Task 6
import show_path
print("Here is the path of the python", show_path)