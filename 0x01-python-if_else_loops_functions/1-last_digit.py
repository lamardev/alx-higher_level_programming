#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# check the sign of number
if number >= 0:
    last_digit = number % 10
else:
    last_digit = abs(number) % 10 * -1

# print number + last digit
print(f"Last digit of {number} is {last_digit} and", end=" ")

# print comment
if last_digit > 5:
    print(f"is greater than 5")
elif last_digit == 0:
    print(f"is zero")
else:
    print(f"is less than 6 and not 0")
