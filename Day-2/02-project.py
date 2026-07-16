"""
Python Day 2
File: project.py
Project: Student Academic Profile
Mission AI & ML Engineer - 2030
Author: Aditya
"""

"""📝 Project Name
Student Academic Profile
🎯 Objective
Variables, data types aur type conversion ka practical use karna.
📥 User Input
Full Name
Roll Number
Age
Branch
Semester
CGPA"""

print("=" * 50)
print("=" * 30)
print("          STUDENT ACADEMIC PROFILE")
print("=" * 30)
print("=" * 50)
name = input("Enter Name: ")
roll_no = input("Enter Roll No.: ")
age = int(input("Enter age: "))
branch = input("Enter branch: ")
semester = int(input("Enter Semester: "))
cgpa = float(input("Enter CGPA: "))
print(f"Name    : {name}")
print(f"Roll no.    : {roll_no}")
print(f"Age    : {age}")
print(f"Branch    : {branch}")
print(f"Semester    : {semester}")
print(f"CGPA    : {cgpa}")
print("=" * 50)