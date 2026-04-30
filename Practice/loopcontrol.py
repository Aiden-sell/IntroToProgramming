# Task 1: Loop that prints numbers from 1 to 20, but stops at 15 using break
for i in range(1, 21):
    if i == 15:
        break
    print(i)

print()  # Separator

# Task 2: Program that prints only odd numbers from 1 to 30 using continue
for i in range(1, 31):
    if i % 2 == 0:
        continue
    print(i)

print()  # Separator

# Task 3: Loop with pass statement in place of a future feature
# The intended feature would be to calculate and print the square of each number
for i in range(1, 6):
    pass  # Placeholder for future implementation: print(i ** 2)

print("Pass statement used as placeholder for squaring numbers.")

print()  # Separator

# Task 4: Countdown from 10 to 1, skipping 5 using continue
for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

print()  # Separator

# Task 5: Sum all numbers in a list but stop at negative number using break
numbers = [1, 2, 3, 4, -5, 6, 7]
total = 0
for num in numbers:
    if num < 0:
        break
    total += num
print(f"Sum: {total}")