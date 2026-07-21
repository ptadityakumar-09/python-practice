"""Python Day 4
File:01-practice.py
Mission AI & ML Engineer - 2030
Author: Aditya"""

print("=" * 50)
# Program 1: Take a number as input and check whether it is Positive, Negative, or Zero.
number = int(input("Enter Number: "))
if number>0:
    print("This is Positive number")
elif number<0:
    print("This is Negative number")
else:
    print("This is zero ")

# Program 2: Check whether a person is Eligible for Voting (Age ≥ 18).
age = int(input("Enter Age: "))
if age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

# Program 3: Take two numbers and print the greater number.
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
if number1>number2:
    print("Greater Number: ", number1)
elif number2>number1:
    print("Greater Number: ", number2)
else:
    print("Both numbers are same ")

# Program 4: Take three numbers and print the largest number.
no_1 = int(input("Enter 1st number: "))
no_2 = int(input("Enter 2nd number: "))
no_3 = int(input("Enter 3rd  number: "))
if no_1 > no_2 and no_1 > no_3:
    print("Largest number is ", no_1)
elif no_2 > no_1 and no_2 > no_3:
    print("Largest number is ", no_2)
else:
    print("Largest number is ", no_3)
# Program 5: Check whether a number is Even or Odd.
number_check = int(input("Enter Number: "))
if number_check%2 == 0:
    print("This is Even number")
else:
    print("This is Odd number")

# Program 6: Take marks as input and print the grade: 90–100 → A+, 80–89 → A , 70–79 → B, 60–69 → C, Below 60 → Fail
marks = float(input("Enter Marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >= 80 and marks <= 89:
    print("Grade: A")
elif marks >= 70 and marks <= 79:
    print("Grade: B")
elif marks >= 60 and marks <= 69:
    print("Grade: C")
elif marks < 60:
    print("Fail")

# Program 7: Check whether a year is a Leap Year.
year = int(input("Enter Year: "))
if year%4 == 0 and (year%100 !=0 or year%400 == 0):
    print("This is Leap year")
else:
    print("This is not Leap year")

# Program 8: Check whether a character is: Vowel, Consonant
character = input("Enter Character: ")
if character.lower() in "aeiou":
    print("Character is Vowel")
else:
    print("Character is consonant")
       
print("=" * 50)
