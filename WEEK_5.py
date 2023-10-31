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
#Task 2 - Adding comments to each statement# python total.py 25 90 15
import sys
count = len(sys.argv)
total = number + 20
while count > 1:
    count -= 1
    total += float(sys.argv[count])
print("Total is", total)

response = ""
while response != 'x' and response != 'z':
     response = input("x or z")
print("you responded with",response)


#Task 3 - my_utils.py
def average(values):
    """ Calculates the average of the given list. """
    total = 0;
    for n in values:                          #total the given values
        total += float(n)
    return total/len(values)                  #return calculated average
#initialisation statement
print("Welcome, utils module has been imported and initialised!")


#Task 4 - Module Search Path
import sys
print ("The import search path for this program is", sys.path)

