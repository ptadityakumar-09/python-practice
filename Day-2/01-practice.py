"""Python Day 2
File: practice.py
Mission AI & ML Engineer - 2030
Author: Aditya"""

print("=" * 50)
# Program 1: Create variables for:Name, Age,CGPA,Student Status
name = input("Enter Name: ")
age = int(input("Enter Age: "))
cgpa = float(input("Enter CGPA: "))
student_status = True

# Program 2: Print all the variables created in Program 1.
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")
print(f"Student Status: {student_status}")

# Program 3: Display the data type of each variable using the appropriate Python function.
print(type(name))
print(type(age))
print(type(cgpa))
print(type(student_status))

# Program 4 :Convert a string containing a number into an integer.
string_number = "48"
integer_number = int(string_number)
print(integer_number)

#Program 5: Convert an integer into a float.
integer_number1 = int(input("Enter Number: "))
float_number = float(integer_number1)
print(float_number)

#Program 6: Convert a float into an integer.
float_number1 = float(input("Enter Number: "))
integer_number2 = int(float_number1)
print(integer_number2)

# Program 7: Create multiple variables in a single line and print them.
student = input(" Enter Student Name: "); city = input("Enter City: "); village = input("Enter Village: ")
print(f"Name: {student}")
print(f"City: {city}")
print(f"Village: {village}")

# Program 8: Swap the values of two variables without using a third variable.
name_1 = input("Enter Name 1: ")
name_2 = input("Enter Name 2: ")
name_1, name_2 = name_2, name_1
print("\nValues after swapping:")
print(f"Name 1: {name_1}")
print(f"Name 2: {name_2}")

print("=" * 50)
