# Q1

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Q2

num = int(input("Enter an interger: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Q3

num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
elif num1 < num2:
    print(f"{num2} is larger than {num1}.")
else:
    print("Both are equal numbers.")

# Q4

num = float(input("Enter a number: "))
if num < 0:
    absolute_value = -num
else:
    absolute_value = num
print(f"The absolute value of {num} is {absolute_value}.")

# Q5

age = int(input("Enter your age: "))
if age >= 18:
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")

# Q6

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Q7

marks = int(input("Enter your marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Q8

num = int(input("Enter a number: "))
if num % 5 == 0:
    print(f"{num} is a multiple of 5.")
else:
    print(f"{num} is not a multiple of 5.")

# Q9

char = input("Enter a character: ")
if len(char) != 1:
    print("Please enter exactly one character.")
else:
    if char.isupper():
        print(f"{char} is an uppercase letter.")
    elif char.islower():
        print(f"{char} is a lowercase letter.")
    else:
        print(f"{char} is not a letter.")

# Q10

amount = float(input("Enter your purchase amount: "))
if amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0
final_amount = amount - discount
print(f"Purchase amount: ₹{amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"final bill amount: ₹{final_amount:.2f}")

