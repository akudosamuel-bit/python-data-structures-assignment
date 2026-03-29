"""
Python Data Structures Assignment
Author: Akudo Samuel
Course: CIT2201
Instructor: Gabriel Ekodo
Date: 27 March 2026
"""

import math
from datetime import datetime

# ===========================
# INPUT HANDLING FUNCTIONS
# ===========================

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# ===========================
# Numeric Types Exercises
# ===========================

# 1. Calculate the area of a circle given a radius
PI = 3.14159
radius = get_float("Enter radius: ")
area_circle = PI * (radius ** 2)
print(f"Area of circle: {area_circle:.2f}")

# 2. Convert Celsius to Fahrenheit
celsius = get_float("Enter temperature in Celsius: ")
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

# 3. Check if a number is even or odd
number_input = get_int("Enter a number: ")
if number_input % 2 == 0:
    print(f"{number_input} is even")
else:
    print(f"{number_input} is odd")

# 4. Calculate 2^10 without pow()
result_power = 2 ** 10
print(f"2^10 is: {result_power}")

# 5. Take two float inputs and display only the integer part of their sum
float1 = get_float("Enter first float: ")
float2 = get_float("Enter second float: ")
sum_floats = float1 + float2
print(f"Integer part of the sum: {int(sum_floats)}")

# 6. Tip Calculator
bill_amount = get_float("Enter bill amount: ")
tip_percentage = get_float("Enter tip percentage: ")
total = bill_amount + (bill_amount * tip_percentage / 100)
print(f"Total amount with tip: {total:.2f}")

# 7. Round 12.34567 to two decimal places
number = 12.34567
rounded_number = round(number, 2)
print(f"Rounded number: {rounded_number}")

# 8. Swap two integers without a temporary variable
a = get_int("Enter value for a: ")
b = get_int("Enter value for b: ")
a, b = b, a
print(f"After swapping: a={a}, b={b}")

# 9. Floor Division & Remainder
# Calculate and print both results in a single print statement
print(f"100 // 7 = {100 // 7}, 100 % 7 = {100 % 7}")

# 10. Calculate age based on birth year
birth_year = get_int("Enter your birth year: ")
current_year = datetime.now().year
age = current_year - birth_year
print(f"You are {age} years old.")

# ===========================
# String Exercises
# ===========================

# 1. Reverse the string "Python Programming"
string1 = "Python Programming"
print(f"Reversed string: {string1[::-1]}")

# 2. Check if "Logic" exists in a string
text = "Programming Logic is Fun"
print("The word 'Logic' exists." if "Logic" in text else "Not found")

# 3. Change case
text = "nDejje uNiversitY"
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())

# 4. Extract Characters
string4 = "abcdefghijklmnopqrst"
print("First 5:", string4[:5], "Last 5:", string4[-5:])

# 5. Replace Spaces
sentence = "This is a sample sentence"
print(sentence.replace(" ", "_"))

# 6. Count 'a'
print("banana".count('a'))

# 7. Palindrome
user_string = input("Enter a string: ").strip()
if user_string.lower() == user_string[::-1].lower():
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# 8. Concatenate
a = "Year"
b = "2"
c = "Semester"

# Method 1: f-string (recommended)
result_f = f"{a} {b} {c}"
print(result_f)  # Year 2 Semester

# Method 2: join
result_join = " ".join([a, b, c])
print(result_join)  # Year 2 Semester

# Method 3: concatenation with +
result_plus = a + " " + b + " " + c
print(result_plus)  # Year 2 Semester


# 9. Split String
print("Civil,Mechanical,Electrical".split(","))

# 10. f-string
code = "CIT2201"
unit = 3

print(f"The course code is {code} and the unit is {unit}")

# ===========================
# List Exercises
# ===========================

# 1. Append item
course_codes = ["CS101", "MATH201", "PHY301", "ENG102", "HIST210"]
course_codes.append("CSC1101")
print(course_codes)

# 2. Insert item
course_codes.insert(2, "Engineering")
print(course_codes)

# 3. Remove item
# example list
items = ["A", "B", "C", "D", "E"]

# remove the 3rd element (index 2) safely
try:
    removed = items.pop(2)   # removes and returns the element at index 2
    print("Removed with pop:", removed)
    print("List after pop:", items)
except IndexError:
    print("List is too short to pop index 2.")

# example list (reset to original)
items = ["A", "B", "C", "D", "E"]

# remove the 3rd element by value (first find it, then remove)
try:
    value_to_remove = items[2]   # get the third element safely
    items.remove(value_to_remove)  # remove the first occurrence of that value
    print("Removed with remove():", value_to_remove)
    print("List after remove():", items)
except IndexError:
    print("List is too short to access index 2.")
except ValueError:
    print("Value not found in list when attempting remove().")

# 4. Replace value
nums = [10, 20, 30, 40, 50]
nums[2] = 35
print(nums)

# 5. Sort names
names = ["Samuel", "Gabriel", "Henry"]
names.sort(reverse=True)
print(names)

# 6. Matrix access
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])

# 7. Middle elements
print([1, 2, 3, 4, 5, 6, 7][2:5])

# 8. Max and Min
values = [5, 10, 3, 8, 2]
print(max(values), min(values))

# 9. Combine lists
print([1, 2, 3] + [4, 5, 6])

# 10. Clear list
temp = [1, 2, 3]
temp.clear()
print(temp)

# ===========================
# Dictionary Exercises
# ===========================

# 1. Create dictionary
course_dict = {"code": "CS101", "name": "Intro", "CU": 3}
print(course_dict)

# 2. Update CU
course_dict["CU"] = 4

# 3. Add lecturer
course_dict["Lecturer"] = "Dr. Smith"
print(course_dict)

# 4. Keys and values
print(course_dict.keys(), course_dict.values())

# 5. Check key
print("Semester" in course_dict)

# 6. Delete key
course_dict.pop("Lecturer")
print(course_dict)

# 7. Squares dictionary
print({i: i**2 for i in range(1, 6)})

# 8. Merge dictionaries
merged = {"a": 1} | {"b": 2}
print(merged)

# 9. Safe get
print(merged.get("z", "Key not found"))

# 10. Second dictionary name
courses = [
    {"code": "EMT1101", "name": "Mathematics I", "CU": 3},
    {"code": "ENG1101", "name": "Communication Skills", "CU": 2},
    {"code": "ELE1201", "name": "Basic Electronics", "CU": 3},
]

# Print the "name" field of the second dictionary (index 1)
print(courses[1]["name"])


# ===========================
# Tuples and Sets Exercises
# ===========================

# 1. Tuple immutability
t = (1, 2, 3)
try:
    t[0] = 10
except TypeError:
    print("Tuples are immutable")

# 2. Unpack tuple
id, code = (101, "EMT")
print(id, code)

# 3. List to set
print(set([1, 2, 2, 3, 4, 4]))

# 4. Union
print({1, 2, 4} | {2, 3, 5})

# 5. Intersection
# two sets of student IDs
group_a = {101, 102, 103, 110}
group_b = {104, 110, 115, 102}

# method 1: using intersection()
common = group_a.intersection(group_b)
print("Common IDs:", common)

# method 2: using & operator
common2 = group_a & group_b
print("Common IDs (using &):", common2)


# 6. Subset
print({1, 2}.issubset({1, 2, 3}))

# 7. Tuple length
print(len((1.4, 2.3, 3.2, 4.0, 5.5, 6.4, 7.3, 8.2, 9.1, 10.0)))

# 8. Modify tuple
t2 = (1, 2, 3)
temp = list(t2)
temp.append(4)
print(tuple(temp))

# 9. Unique characters
print(set("MISSISSIPPI"))

# 10. Frozenset
# create a frozenset from an iterable
fs = frozenset([101, 102, 103])
print("frozenset:", fs)

# set operations still work (return new sets/frozensets)
a = frozenset([101, 102, 103])
b = frozenset([102, 104])
print("intersection:", a & b)        # frozenset({102})
print("union:", a | b)               # frozenset({101,102,103,104})

# because frozensets are hashable, they can be used as dict keys
d = {a: "group A"}
print("dict lookup:", d[a])

# ===========================
# Advanced Nested Data Structures
# ===========================

courses_data = [
    {"year": 1, "sem": 1, "courses": ["EMT1101 Math", "ENG1101 Comm"]},
    {"year": 1, "sem": 2, "courses": ["EMT1201 Math II", "ELE1201 Systems"]}
]

# 1. Access course
print(courses_data[1]["courses"][1])

# 2. Print all courses
for item in courses_data:
    for course in item["courses"]:
        print(course)

# 3. Count courses
print(sum(len(item["courses"]) for item in courses_data))

# 4. Add course
for item in courses_data:
    if item["sem"] == 2:
        item["courses"].append("DME1301 Workshop")

# 5. Create dictionary
course_dict = {}
for item in courses_data:
    for course in item["courses"]:
        code, name = course.split(" ", 1)
        course_dict[code] = name
print(course_dict)

# 6. Get years
print([item["year"] for item in courses_data])

# 7. Filter courses
for item in courses_data:
    if len(item["courses"]) > 5:
        print(item["year"], item["sem"])

# 8. Parse courses
for item in courses_data:
    for course in item["courses"]:
        print(tuple(course.split(" ", 1)))

# 9. Find course
def find_course(code):
    for item in courses_data:
        for course in item["courses"]:
            if course.startswith(code):
                return item["year"], item["sem"]
    return None

print(find_course("ELE1201"))

# 10. Add total CU
for item in courses_data:
    item["total cu"] = 0

print(courses_data)
