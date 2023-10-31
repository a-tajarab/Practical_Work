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

squares.remove(3)
print("Updated list of square numbers", squares)

# Task 6 - Pop method
squares = [1, 4, 9, 16, 25]
removed_value = squares.pop()
print("Removed value:", removed_value)
print("Updated list:", squares)


