# Task 1 - Using List-Methods
import math

if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25]

for num in squares:
    square_root = math.sqrt(num)
    print("The square root of", {num}, " is", {square_root})

# Task 2 - Introducing Methods
squares.append(49)
squares.append(64)
squares.append(81)
print("Updated list of squares:", squares)

# Task 3 - Extend Method - mutuating the list
squares.extend([100, 121, 144, 169])
print("Updated list of squares:", squares)

# Task 4 - Insert method
squares[1:0] = [2]
print("Updated list of square numbers", squares)

# Task 5 - Remove method
squares.remove(49)
print("Updated list of square numbers", squares)


# Task 6 - Pop method
squares = [1, 4, 9, 16, 25]
removed_value = squares.pop()
print("Removed value:", removed_value)
print("Updated list:", squares)

#Task 7 - Pop method_2
removed_value = squares.pop(0)
print("Updated list:", squares)

#Task 8 - Clear Method
#some_list[:] = []

#Task 9 - Sort Method
names = ["Eric", "anna", "Sophie", "sam"]
names.sort()
print(names)

#Task 10 - Sort Method_2
names.sort(key=lambda x: x.upper())
print(names)

#Task 11 - Reverse Method
squares[:] = squares[::-1]
print(squares)

#Task 12 - Index, Count and Copy Methods
colours = ["red", "green", "yellow", "blue", "red"]
print("the colour index of yellow is", colours.index("yellow"))
print("the colour index of blue is", colours.index("blue"))

print("the colour count of red is",colours.count("red"))
print("the colour count of black is", colours.count("black"))

new_colours = colours.copy()
print(new_colours)

#Task 13 - List Comprehensions
squares = []
for x in range(10):
    squares.append(x*x)
squares = [x * x for x in range(10)]
print(squares)

#Task 14 - Cube list
cubes = []
for x in range(20):
    cubes.append(x*x*x)
cubes = [x * x * x for x in range(20)]
print(cubes)
even_nums = [num for num in range(100,201) if num % 2 == 0]

#Task 15 - Intro to Tuple
student = "Griffin, P.", 2, 38.2
print(student)
address = "43","Church Wood Ave", "Leeds", "LS16LSF "
print(address)

#Task 16 - Empty and Single element Tuples
empty = ()
the_one = "Neo",
the_one = ("Neo")
print(type(empty))
print(type(the_one))


#Task 17 - Sequence Unpacking
house_num, street, city, postcode = address
print("Do you live in", city)
print("Are you familiar with the street called", street)
print("Oh the postcode is:",postcode)
print("Look out for the door number", house_num)

print(*address)   #the prefix causes the print statement to have no parenthsesis
print(address)


