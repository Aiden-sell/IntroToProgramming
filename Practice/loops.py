# For Loop Practice - 6 Programming Tasks

# Task 1: Print a Countdown from 10 to 1
print("=" * 50)
print("Task 1: Countdown from 10 to 1")
print("=" * 50)

for i in range(10, 0, -1):
    print(i)

print()

# Task 2: Sum of a List
print("=" * 50)
print("Task 2: Sum of a List of 10 Integers")
print("=" * 50)

numbers = [5, 12, 8, 23, 15, 3, 9, 18, 7, 20]
total = 0

for num in numbers:
    total += num

print(f"List of numbers: {numbers}")
print(f"Sum of all numbers: {total}")

print()

# Task 3: Square Each Number
print("=" * 50)
print("Task 3: Create a List of Squares (1 to 5)")
print("=" * 50)

original_list = [1, 2, 3, 4, 5]
squared_list = []

for num in original_list:
    squared_list.append(num ** 2)

print(f"Original list: {original_list}")
print(f"Squared list: {squared_list}")

print()

# Task 4: Character Count - Count Vowels
print("=" * 50)
print("Task 4: Count Vowels in a String")
print("=" * 50)

user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0

for char in user_string:
    if char in vowels:
        vowel_count += 1

print(f"String: {user_string}")
print(f"Number of vowels: {vowel_count}")

print()

# Task 5: Print Multiplication Table
print("=" * 50)
print("Task 5: Print Multiplication Table")
print("=" * 50)

try:
    number = int(input("Enter a number for the multiplication table: "))
    print(f"\nMultiplication Table for {number}:")
    
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

print()

# Task 6: List of Names - Print Greetings
print("=" * 50)
print("Task 6: Print Greetings for Each Name")
print("=" * 50)

names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(f"Hello, {name}!")
