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
number_3 =input ("Type a number of your choice:")
number_3 = int(number_3)
print("Wow what a lovely number", number_3, "love it")
print("Right! Let's get onto some fun stuff")
print("Would you like to proceed?")
response = input("Y or N:")
if response == "Y":
    print("Fabulous!")
elif response == "N":
    print("Oh well I guess you will miss the fun!:(")
