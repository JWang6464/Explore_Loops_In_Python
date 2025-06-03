"""
Assignment: Explore Loops in Python
For Cognizant Externship – Python Fundamentals
Description:
This script includes three tasks:
1. Countdown using a while loop
2. Multiplication table using a for loop
3. Factorial calculation using a for loop

Jordan Wang
6/3/2025
"""

# Task 1: Countdown Timer
start = int(input("Enter the starting number for the countdown: "))
while start > 0:
    print(start, end=" ")
    start -= 1
print("Blast off!")

# Task 2: Multiplication Table
num = int(input("\nEnter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Task 3: Factorial Calculation
fact_num = int(input("\nEnter a number to find its factorial: "))
factorial = 1
for i in range(1, fact_num + 1):
    factorial *= i
print(f"The factorial of {fact_num} is {factorial}.")
