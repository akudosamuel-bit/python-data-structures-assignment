# Created by Samuel Akudo

# ===========================
# Numeric Types Exercises
# ===========================

import math
from datetime import datetime

# 1. Calculate the area of a circle given a radius
radius = 5  # example radius
pi = 3.14159
area_circle = pi * (radius ** 2)
print(f"Area of circle with radius {radius}: {area_circle}")

# 2. Convert Celsius to Fahrenheit
celsius = 25  # example Celsius temperature
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

# 3. Check if a number is even or odd
number_input = int(input("Enter a number: "))
if number_input % 2 == 0:
    print(f"{number_input} is even")
else:
    print(f"{number_input} is odd")

# 4. Calculate 2^10 without pow()
result_power = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
print(f"2^10 is: {result_power}")

# 5. Take two float inputs and display only the integer part of their sum
float1 = float(input("Enter first float: "))
float2 = float(input("Enter second float: "))
sum_floats = float1 + float2
print(f"Integer part of the sum: {int(sum_floats)}")

# 6. Tip Calculator
bill_amount = float(input("Enter bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))
total = bill_amount + (bill_amount * tip_percentage / 100)
print(f"Total amount with tip: {total:.2f}")

# 7. Round 12.34567 to two decimal places
number = 12.34567
rounded_number = round(number, 2)
print(f"Rounded number: {rounded_number}")

# 8. Swap two integers without a temporary variable
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
a, b = b, a
print(f"After swapping: a={a}, b={b}")

# 9. Floor division and remainder of 100/7
floor_division = 100 // 7
remainder = 100 % 7
print(f"Floor division: {floor_division}, Remainder: {remainder}")

# 10. Calculate age based on birth year
birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"You are {age} years old.")

# ===========================
# String Exercises
# ===========================

# 1. Reverse the string "Python Programming"
string1 = "Python Programming"
reversed_string = string1[::-1]
print(f"Reversed string: {reversed_string}")

# 2. Check if "Logic" exists in "ProgrammingLogicisFun"
string2 = "ProgrammingLogicisFun"
exists = "Logic" in string2
print(f"Does 'Logic' exist? {exists}")

# 3. Convert "nDejje uNiversitY" to all lowercase and all uppercase
string3 = "nDejje uNiversitY"
lowercase_str = string3.lower()
uppercase_str = string3.upper()
print(f"Lowercase: {lowercase_str}")
print(f"Uppercase: {uppercase_str}")

# 4. Extract first 5 and last 5 characters of a 20-character string
string4 = "abcdefghijklmnopqrstuvwxyz"  # 26 characters, but we can use 20
string4 = string4[:20]
first_five = string4[:5]
last_five = string4[-5:]
print(f"First 5: {first_five}, Last 5: {last_five}")

# 5. Replace all spaces with underscores
sentence = "This is a sample sentence"
modified_sentence = sentence.replace(" ", "_")
print(f"Modified sentence: {modified_sentence}")

# 6. Count how many times 'a' appears in "banana"
banana_str = "banana"
count_a = banana_str.count('a')
print(f"Number of 'a's in 'banana': {count_a}")

# 7. Check if a string is a palindrome
user_string = input("Enter a string to check palindrome: ")
if user_string == user_string[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# 8. Concatenate "Year", "2", and "Semester" with spaces
string_concat = "Year" + " " + "2" + " " + "Semester"
print(f"Concatenated string: {string_concat}")

# 9. Split "Civil,Mechanical,Electrical" into a list
specializations = "Civil,Mechanical,Electrical"
split_list = specializations.split(",")
print(f"Split list: {split_list}")

# 10. Use f-string to print course code and unit
course_code = "CS101"
unit = 3
print(f"The course code is {course_code} and the unit is {unit}")

# ===========================
# List Exercises
# ===========================

# 1. Create a list of 5 course codes and append a 6th
course_codes = ["CS101", "MATH201", "PHY301", "ENG102", "HIST210"]
course_codes.append("CHEM110")
print(f"Course codes: {course_codes}")

# 2. Insert "Engineering" at index 2
course_codes.insert(2, "Engineering")
print(f"After insertion: {course_codes}")

# 3. Remove 3rd element using pop() and remove()
pop_element = course_codes.pop(2)
print(f"After pop(): {course_codes}")
course_codes.remove("ENG102")
print(f"After remove(): {course_codes}")

# 4. Change value 30 to 35 in list
nums = [10, 20, 30, 40, 50]
nums[2] = 35
print(f"Modified list: {nums}")

# 5. Sort list of names in reverse order
names = ["Alice", "Bob", "Charlie", "David"]
names.sort(reverse=True)
print(f"Sorted in reverse: {names}")

# 6. Nested list for 2x2 matrix
matrix = [[1, 2], [3, 4]]
element = matrix[1][0]
print(f"Element at row 1, col 0: {element}")

# 7. Slice middle three elements of a 7-element list
list7 = [1, 2, 3, 4, 5, 6, 7]
middle_three = list7[2:5]
print(f"Middle three: {middle_three}")

# 8. Find max and min without loop
int_list = [5, 10, 3, 8, 2]
max_val = max(int_list)
min_val = min(int_list)
print(f"Max: {max_val}, Min: {min_val}")

# 9. Combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(f"Combined list: {combined_list}")

# 10. Clear list
list_clear = [1, 2, 3]
list_clear.clear()
print(f"Cleared list: {list_clear}")

# ===========================
# Dictionary Exercises
# ===========================

# 1. Create a dictionary for a course
course_dict = {"code": "CS101", "name": "Introduction to CS", "CU": 3}
print(f"Course dictionary: {course_dict}")

# 2. Update CU value
course_dict["CU"] = 4
print(f"Updated CU: {course_dict}")

# 3. Add new key-value pair
course_dict["Lecturer"] = "Dr. Smith"
print(f"After adding Lecturer: {course_dict}")

# 4. Print all keys and values
print("Keys:", list(course_dict.keys()))
print("Values:", list(course_dict.values()))

# 5. Check if key "Semester" exists
has_semester = "Semester" in course_dict
print(f"Does 'Semester' exist? {has_semester}")

# 6. Remove a key
del course_dict["Lecturer"]
print(f"After deletion: {course_dict}")

# 7. Dictionary with numbers 1-5 and their squares
squares_dict = {i: i ** 2 for i in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# 8. Merge dictionaries
dictA = {'a': 1}
dictB = {'b': 2}
merged_dict = {**dictA, **dictB}
print(f"Merged dict: {merged_dict}")

# 9. Access values safely
value = merged_dict.get('a', 'Key not found')
print(f"Value for 'a': {value}")
value_missing = merged_dict.get('z', 'Key not found')
print(f"Value for 'z': {value_missing}")

# 10. List of 3 dictionaries and print second's name
courses_list = [
    {"code": "CS101", "name": "Intro to CS", "CU": 3},
    {"code": "MATH201", "name": "Calculus", "CU": 4},
    {"code": "PHY301", "name": "Physics", "CU": 3}
]
second_course_name = courses_list[1]["name"]
print(f"Second course name: {second_course_name}")

# ===========================
# Tuples and Sets Exercises
# ===========================

# 1. Create a tuple with 4 elements and try to change first
tuple1 = (1, 2, 3, 4)
try:
    tuple1[0] = 10
except TypeError as e:
    print(f"Error: {e}")

# 2. Unpack tuple
id, code = (101, "EMT")
print(f"ID: {id}, Code: {code}")

# 3. Convert list to set to remove duplicates
list_with_duplicates = [1, 2, 2, 3, 4, 4]
set_unique = set(list_with_duplicates)
print(f"Unique set: {set_unique}")

# 4. Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"Union: {union_set}")

# 5. Intersection of two sets
setA = {1, 2, 3}
setB = {2, 3, 4}
intersection = setA.intersection(setB)
print(f"Intersection: {intersection}")

# 6. Check subset
subset = {1, 2}
print(f"Is subset? {subset.issubset(setA)}")

# 7. Length of a tuple with 10 floats
float_tuple = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
print(f"Length of tuple: {len(float_tuple)}")

# 8. Convert tuple to list, add item, convert back
tuple2 = (1, 2, 3)
list_from_tuple = list(tuple2)
list_from_tuple.append(4)
new_tuple = tuple(list_from_tuple)
print(f"New tuple: {new_tuple}")

# 9. Unique characters in "MISSISSIPPI"
string_chars = "MISSISSIPPI"
set_chars = set(string_chars)
print(f"Unique characters: {set_chars}")

# 10. Create a frozenset
fset = frozenset([1, 2, 3])
print(f"Frozenset: {fset}")

# ===========================
# Advanced Nested Data Structures
# ===========================

# Given courses_data
courses_data = [
    {"year": 1, "sem": 1, "courses": ["EMT1101 Math", "ENG1101 Comm"]},
    {"year": 1, "sem": 2, "courses": ["EMT1201 Math II", "ELE1201 Systems"]}
]

# 1. Access "ELE1201 Systems"
course_name = courses_data[1]["courses"][1]
print(f"Course name: {course_name}")

# 2. Nested loops to print all courses
print("All courses:")
for term in courses_data:
    for course in term["courses"]:
        print(course)

# 3. Count total courses in Year 1
total_courses_year1 = sum(len(term["courses"]) for term in courses_data if term["year"] == 1)
print(f"Total courses in Year 1: {total_courses_year1}")

# 4. Append new course to sem 2
for term in courses_data:
    if term["sem"] == 2:
        term["courses"].append("DME 1301 Workshop")
        break
print(f"Updated courses data: {courses_data}")

# 5. Create dictionary with course codes as keys
course_code_dict = {}
for term in courses_data:
    for course in term["courses"]:
        code = course.split()[0]
        course_code_dict[code] = course
print(f"Course code dictionary: {course_code_dict}")

# 6. List comprehension to get all year values
years_list = [term["year"] for term in courses_data]
print(f"Years list: {years_list}")

# 7. Print year and sem if number of courses > 1
for term in courses_data:
    if len(term["courses"]) > 1:
        print(f"Year: {term['year']}, Semester: {term['sem']}, Number of courses: {len(term['courses'])}")

# 8. Split course code and name
for term in courses_data:
    for course in term["courses"]:
        code, name = course.split(" ", 1)
        print((code, name))

# 9. Function to find course info
def find_course(course_code):
    for term in courses_data:
        for course in term["courses"]:
            if course.startswith(course_code):
                return {"year": term["year"], "sem": term["sem"]}
    return "Course not found."

# Example usage:
print(find_course("ELE1201"))

# 10. Add "total cu" key with value 0
for term in courses_data:
    term["total cu"] = 0
print(f"Updated courses data with 'total cu': {courses_data}")
