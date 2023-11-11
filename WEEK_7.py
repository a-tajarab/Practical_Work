#Task 1 - Introducing Sets

names = {"John", "Eric", "Terry", "Micheal", "Graham", "Terry"}
print(names)

#Task 2 - Set comprehensions
sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence if x != " "}
print(sentence)
print(unique_letters)

#Task 3 - Set Operations
name = input("Enter your name: ")
if name in names:
    print("You are listed in the set of known names")
elif name not in names:
    print("You are not listed in the set of known names")



#Task 5 - Two initial sets - accessors type methods
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}
staff = staff | {"Mark", "Ringo"}
print(staff)
staff_directors = staff & directors
print(staff_directors)
external = directors - staff
print(external)
staff_or_external = directors ^ staff
print(staff_or_external)

#Task 6 - mutator version
vowels = {"a", "e", "i"}
print(vowels)
vowels -= {"o", "u"}

print(vowels)

#Task 7 -
if directors <= staff:
  print("All directors are staff members")
if staff > directors:
  print("All directors are staff members")

#Task 8 - Creating an immutable set
suits = frozenset({"heart", "club", "spade", "diamond"})


#Task 9 - Dictionary Comprehensions
import math
roots = {n: math.sqrt(n) for n in range(1, 26)}
print(roots)

#Task 10 - Manipulating Dictionaries
stock = {"apple": 5, "pear": 10, "kiwi":8, }
if "apple" in stock:
   print("Apples have a stock level")

print("Apple stock level is", stock["apple"])
stock["apple"] += 1
stock["pear"] = 50
stock["kiwi"] = 10
stock.update({"lemon": 15, "strawberry": 99})


#Task 11 - Dictionary methods
# pop the "orange" returning its stock level
if "orange" in stock:
    orange_stock_level = stock.pop("orange")
    print(f"The stock level of orange was {orange_stock_level}")
else:
    print("The fruit 'orange' is not in the stock dictionary")

# update the stock to include two new fruits
stock.update(lemmon=15, strawberry=99)
print("Updated stock:", stock)

#Task 12 - Iterations over Dictionaries
for num, sqrt_value in roots.items():
    print(f"The square root of {num} is {sqrt_value}")
