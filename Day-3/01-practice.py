"""Python Day 3
File: 01-practice.py
Mission AI & ML Engineer - 2030
Author: Aditya"""

print("=" * 50)
# These two numbers are used in 1 - 6  programs .
n1 = int(input("Enter first Number: "))
n2 = int(input("Enter second Number: "))
# Program 1— Take two numbers as input and perform: Addition, Subtraction, Multiplication, Division
add = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

# Program 2— Find: Floor Division, Modulus, Exponent, using two numbers.
print(f"Floor Division: {n1 // n2}")
print(f"Remainder: {n1 % n2}")
print(f"Power: {n1 ** n2}")

# Program 3— Compare two numbers using: ==, !=, >, <, >= ,<=
print(n1 == n2)
print(n1 != n2)
print(n1 > n2)
print(n1 < n2)
print(n1 >= n2)
print(n1 <= n2)

# Program 4— Create two boolean variables and perform: and, or, not
aditya = True
danav = False

print(aditya and danav)
print(aditya or danav)
print(not aditya)
print(not danav)

# Program 5— Use Assignment Operators: +=, -=, *=, /=
n1 += 1
print(" value of n1 after using += operator:  ", n1)
n1 -= 2
print("value of n1 after using -= operator:  ", n1)
n1 *= 5
print("value of n1 after using *= operator:  ", n1)
n1 /= 2
print("value of n1 after using /= operator:  ", n1)

# Program 6— Find the square and cube of a number.
square = n2 **2
cube = n2 ** 3
print("Square of ", n2 , " : " , square)
print("Cube of " , n2 , " : " , cube)

# Program 7— Calculate the Area and Perimeter of a Rectangle.
l = int(input("Enter Length (cm): "))
b = int(input("Enter breadth(cm): "))
print(f"Area: {l*b}")
print(f"Perimeter: {2 * (l + b)}")

# Program 8— Calculate the Simple Interest. Formula: SI = (P × R × T) / 100
p = int(input("Enter Principal(₹): "))
r = int(input("Enter Rate(%): "))
t = int(input("Enter Time: "))
si = (p * r * t) / 100
print(f"Simple Interest: {si}")
print("=" * 50)
