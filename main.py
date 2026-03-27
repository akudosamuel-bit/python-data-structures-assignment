```python
#!/usr/bin/env python3
"""
main.py — Improved Python Data Structures Exercises (single-file, runnable)

Name: Akudo Samuel
Date: 27 March 2026

Notes:
- Uses the original pi value from the assignment: PI = 3.14159 (intentionally unchanged).
- Input helpers validate user input and handle interruptions.
- Functions are non-destructive where sensible and include docstrings.
- CLI supports listing demos, running a demo, running all demos, or an interactive session.
"""

from typing import Any, List, Dict, Tuple, Optional
import argparse
import sys
import copy
import logging

# Keep the original pi value as requested
PI = 3.14159

# Configure a simple logger for debug / info messages
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


# ---------------------------
# Utility input helpers
# ---------------------------

def safe_int(prompt: str, default: Optional[int] = None) -> int:
    """Prompt repeatedly for an integer until valid or user cancels."""
    while True:
        try:
            raw = input(f"{prompt}{' [' + str(default) + ']' if default is not None else ''}: ").strip()
            if raw == "" and default is not None:
                return default
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            raise

def safe_float(prompt: str, default: Optional[float] = None) -> float:
    """Prompt repeatedly for a float until valid or user cancels."""
    while True:
        try:
            raw = input(f"{prompt}{' [' + str(default) + ']' if default is not None else ''}: ").strip()
            if raw == "" and default is not None:
                return float(default)
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            raise


# ---------------------------
# Section 1: Numeric Types
# ---------------------------

def area_circle(radius: float) -> float:
    """Return area of a circle using the original PI constant."""
    return PI * radius ** 2

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def even_odd(num: int) -> str:
    """Return 'Even' or 'Odd' depending on parity of num."""
    return "Even" if num % 2 == 0 else "Odd"

def power_of_two(exp: int = 10) -> int:
    """Return 2 raised to the given exponent (default 10)."""
    return 2 ** exp

def int_sum(a: float, b: float) -> int:
    """Return integer part of the sum of a and b (truncates toward zero)."""
    return int(a + b)

def tip_calc(bill: float, percent: float) -> float:
    """Return bill total after adding percent tip."""
    return bill + (bill * percent / 100)

def round_num(value: float = 12.34567, ndigits: int = 2) -> float:
    """Round value to ndigits and return it."""
    return round(value, ndigits)

def swap(a: Any, b: Any) -> Tuple[Any, Any]:
    """Swap two values and return them (non-destructive)."""
    return b, a

def floor_div_remainder(dividend: int = 100, divisor: int = 7) -> Tuple[int, int]:
    """Return floor division and remainder (dividend // divisor, dividend % divisor)."""
    return dividend // divisor, dividend % divisor

def calculate_age(birth_year: int, current_year: int = 2026) -> int:
    """Return age given birth_year and optional current_year."""
    return current_year - birth_year


# ---------------------------
# Section 2: Strings
# ---------------------------

def reverse_string(s: str) -> str:
    """Return the reversed string using slicing."""
    return s[::-1]

def check_word_exists(text: str, word: str = "Logic", case_sensitive: bool = True) -> bool:
    """Return True if word exists in text. Optionally perform case-insensitive search."""
    if case_sensitive:
        return word in text
    return word.lower() in text.lower()

def change_case(text: str) -> Tuple[str, str]:
    """Return (lowercase, uppercase) tuple for the given text."""
    return text.lower(), text.upper()

def extract_chars(s: str, first_n: int = 5, last_n: int = 5) -> Tuple[str, str]:
    """Return first_n and last_n characters as a tuple. Handles short strings safely."""
    first = s[:first_n]
    last = s[-last_n:] if last_n and len(s) >= last_n else s
    return first, last

def replace_space(s: str, repl: str = "_") -> str:
    """Replace spaces with repl and return the new string."""
    return s.replace(" ", repl)

def count_a(word: str) -> int:
    """Count occurrences of lowercase 'a' in word (case-sensitive)."""
    return word.count('a')

def palindrome(word: str, case_insensitive: bool = False) -> bool:
    """Return True if word is a palindrome. Optionally ignore case."""
    if case_insensitive:
        word = word.lower()
    return word == word[::-1]

def concat() -> str:
    """Return a sample concatenated string."""
    return "Year 2 Semester"

def split_string(s: str, sep: str = ",") -> List[str]:
    """Split string by sep and return list. Strips whitespace from parts."""
    return [part.strip() for part in s.split(sep)]

def course_info(code: str, unit: int) -> str:
    """Return formatted course info using f-string."""
    return f"The course code is {code} and the unit is {unit}"


# ---------------------------
# Section 3: Lists
# ---------------------------

def add_course(lst: List[str], course: str = "CSC1101") -> List[str]:
    """Return a new list with course appended (non-destructive)."""
    new_list = list(lst)
    new_list.append(course)
    return new_list

def insert_item(lst: List[str], index: int = 2, item: str = "Engineering") -> List[str]:
    """Return a new list with item inserted at index (non-destructive)."""
    new_list = list(lst)
    idx = max(0, min(index, len(new_list)))
    new_list.insert(idx, item)
    return new_list

def remove_item(lst: List[Any], index: int = 2) -> List[Any]:
    """Return a new list with the item at index removed (non-destructive)."""
    new_list = list(lst)
    if 0 <= index < len(new_list):
        new_list.pop(index)
    else:
        logger.warning("Index %s out of range; returning original list.", index)
    return new_list

def replace_example() -> List[int]:
    """Return a sample list with a replaced element."""
    nums = [10, 20, 30, 40, 50]
    nums[2] = 35
    return nums

def sort_names(names: List[str], reverse: bool = True) -> List[str]:
    """Return a new sorted list (non-destructive)."""
    return sorted(names, reverse=reverse)

def matrix_access() -> int:
    """Return a sample matrix element (m[1][0])."""
    m = [[1, 2], [3, 4]]
    return m[1][0]

def middle_slice(lst: List[Any]) -> List[Any]:
    """Return a middle slice (example: indices 2:5)."""
    return lst[2:5]

def max_min(lst: List[int]) -> Tuple[int, int]:
    """Return (max, min) of a list. Raises ValueError on empty list."""
    if not lst:
        raise ValueError("List must not be empty.")
    return max(lst), min(lst)

def combine_lists(a: List[Any], b: List[Any]) -> List[Any]:
    """Return concatenation of two lists."""
    return a + b

def clear_list(lst: List[Any]) -> List[Any]:
    """Return an empty list (non-destructive)."""
    return []


# ---------------------------
# Section 4: Dictionaries
# ---------------------------

def create_dict() -> Dict[str, Any]:
    """Return a sample dictionary."""
    return {"code": "EMT", "name": "Math", "CU": 3}

def update_cu(d: Dict[str, Any], cu: int = 4) -> Dict[str, Any]:
    """Return a copy of d with 'CU' updated to cu."""
    new_d = dict(d)
    new_d["CU"] = cu
    return new_d

def add_lecturer(d: Dict[str, Any], lecturer: str = "Dr. Smith") -> Dict[str, Any]:
    """Return a copy of d with 'Lecturer' added."""
    new_d = dict(d)
    new_d["Lecturer"] = lecturer
    return new_d

def keys_values(d: Dict[str, Any]) -> Tuple[List[str], List[Any]]:
    """Return keys and values as lists."""
    return list(d.keys()), list(d.values())

def check_key(d: Dict[str, Any], key: str = "Semester") -> bool:
    """Return True if key exists in dict."""
    return key in d

def delete_key(d: Dict[str, Any], key: str = "CU") -> Dict[str, Any]:
    """Return a copy of d with key removed if present."""
    new_d = dict(d)
    new_d.pop(key, None)
    return new_d

def squares_dict(n: int = 5) -> Dict[int, int]:
    """Return a dict mapping 1..n to their squares."""
    return {x: x**2 for x in range(1, n+1)}

def merge_dicts(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    """Return a new dict merging a and b (b overrides a)."""
    return {**a, **b}

def safe_get(d: Dict[str, Any], key: str = "name") -> Any:
    """Return d.get(key) (None if missing)."""
    return d.get(key)

def second_name(lst: List[Dict[str, Any]]) -> Any:
    """Return the 'name' field of the second dict in a list; raises IndexError if not present."""
    return lst[1]["name"]


# ---------------------------
# Section 5: Tuples & Sets
# ---------------------------

def tuple_test() -> Tuple[int, ...]:
    """Return a sample tuple."""
    return (1, 2, 3, 4)

def unpack_tuple() -> Tuple[int, str]:
    """Unpack and return sample tuple values."""
    id_, code = (101, "EMT")
    return id_, code

def to_set(lst: List[Any]) -> set:
    """Convert list to set and return it."""
    return set(lst)

def union_sets(a: set, b: set) -> set:
    """Return union of two sets."""
    return a | b

def intersection_sets(a: set, b: set) -> set:
    """Return intersection of two sets."""
    return a & b

def subset_check(a: set, b: set) -> bool:
    """Return True if a is subset of b."""
    return a.issubset(b)

def tuple_length(t: Tuple[Any, ...]) -> int:
    """Return length of tuple."""
    return len(t)

def modify_tuple(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """Return a new tuple with an appended element."""
    lst = list(t)
    lst.append(5)
    return tuple(lst)

def unique_chars(s: str = "MISSISSIPPI") -> set:
    """Return unique characters from s."""
    return set(s)

def frozen_set_example() -> frozenset:
    """Return a frozenset example."""
    return frozenset([1, 2, 3])


# ---------------------------
# Section 6: Advanced (nested data)
# ---------------------------

DEFAULT_COURSES_DATA = [
    {"year": 1, "sem": 1, "courses": ["EMT1101 Math", "ENG1101 Comm"]},
    {"year": 1, "sem": 2, "courses": ["EMT1201 Math II", "ELE1201 Systems"]}
]

def deep_access(data: List[Dict[str, Any]]) -> Any:
    """Return a deeply nested element example (data[1]['courses'][1]) safely."""
    try:
        return data[1]["courses"][1]
    except (IndexError, KeyError, TypeError):
        logger.error("Data structure does not match expected format.")
        return None

def print_courses(data: List[Dict[str, Any]]) -> None:
    """Print all course strings from nested data."""
    for item in data:
        for course in item.get("courses", []):
            print(course)

def count_courses(data: List[Dict[str, Any]]) -> int:
    """Return total number of courses across all items."""
    return sum(len(item.get("courses", [])) for item in data)

def add_course_to_sem2(data: List[Dict[str, Any]], course: str = "DME 1301 Workshop") -> List[Dict[str, Any]]:
    """Return a deep copy of data with the course appended to sem==2 items (non-destructive)."""
    new_data = copy.deepcopy(data)
    for item in new_data:
        if item.get("sem") == 2:
            item.setdefault("courses", []).append(course)
    return new_data

def course_dict(data: List[Dict[str, Any]]) -> Dict[str, str]:
    """Return a dict mapping course code to course name."""
    result: Dict[str, str] = {}
    for item in data:
        for course in item.get("courses", []):
            parts = course.split(" ", 1)
            if len(parts) == 2:
                code, name = parts
                result[code] = name
            else:
                result[f"UNK_{len(result)+1}"] = course
    return result

def get_years(data: List[Dict[str, Any]]) -> List[int]:
    """Return list of years present in data (unique, sorted)."""
    years = sorted({item.get("year") for item in data if "year" in item})
    return years

def filter_courses(data: List[Dict[str, Any]]) -> List[Tuple[int, int]]:
    """Return list of (year, sem) for items with more than 5 courses."""
    return [(item.get("year"), item.get("sem")) for item in data if len(item.get("courses", [])) > 5]

def parse_courses(data: List[Dict[str, Any]]) -> List[Tuple[str, str]]:
    """Return list of tuples (code, name) for each course; skip malformed entries."""
    parsed = []
    for item in data:
        for course in item.get("courses", []):
            parts = course.split(" ", 1)
            if len(parts) == 2:
                parsed.append(tuple(parts))
    return parsed

def find_course(data: List[Dict[str, Any]], code: str) -> Optional[Tuple[int, int]]:
    """Return (year, sem) of the first item containing code in its course strings (substring match)."""
    for item in data:
        for course in item.get("courses", []):
            if code in course:
                return item.get("year"), item.get("sem")
    return None

def add_cu_field(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return a deep copy of data with a 'total cu' field initialized to 0 for each item."""
    new_data = copy.deepcopy(data)
    for item in new_data:
        item.setdefault("total cu", 0)
    return new_data


# ---------------------------
# CLI / Demo runner
# ---------------------------

_DEMOS = {
    # Numeric
    "area_circle": lambda: print("Area (r=5):", area_circle(5)),
    "celsius_to_fahrenheit": lambda: print("25°C ->", celsius_to_fahrenheit(25)),
    "even_odd": lambda: print("Even/Odd 7:", even_odd(7)),
    "power_of_two": lambda: print("2^10:", power_of_two()),
    "int_sum": lambda: print("Int part of 3.7 + 2.4:", int_sum(3.7, 2.4)),
    "tip_calc": lambda: print("Tip on 100 at 10%:", tip_calc(100, 10)),
    "round_num": lambda: print("Rounded:", round_num()),
    "swap": lambda: print("Swap 1,2 ->", swap(1, 2)),
    "floor_div_remainder": lambda: print("100//7, 100%7 ->", floor_div_remainder()),
    "calculate_age": lambda: print("Age for birth year 2000:", calculate_age(2000)),
    # Strings
    "reverse_string": lambda: print("Reverse:", reverse_string("Python Programming")),
    "check_word_exists": lambda: print("Contains 'Logic':", check_word_exists("Programming Logic is Fun")),
    "change_case": lambda: print("Lower/Upper:", change_case("nDejje uNiversitY")),
    "extract_chars": lambda: print("Extract:", extract_chars("nDejje uNiversitY")),
    "replace_space": lambda: print("Replace spaces:", replace_space("nDejje uNiversitY")),
    "count_a": lambda: print("Count 'a' in 'banana':", count_a("banana")),
    "palindrome": lambda: print("Is 'radar' palindrome?:", palindrome("radar")),
    "concat": lambda: print("Concat:", concat()),
    "split_string": lambda: print("Split:", split_string("a,b,c")),
    "course_info": lambda: print(course_info("EMT1101", 3)),
    # Lists
    "add_course": lambda: print(add_course(["Math", "Physics"])),
    "insert_item": lambda: print(insert_item(["Science", "Arts"])),
    "remove_item": lambda: print(remove_item(["A", "B", "C", "D"])),
    "replace_example": lambda: print("Replace:", replace_example()),
    "matrix_access": lambda: print("Matrix access:", matrix_access()),
    # Dicts
    "create_dict": lambda: print("Created:", create_dict()),
    "update_cu": lambda: print("Updated CU:", update_cu(create_dict())),
    "squares_dict": lambda: print("Squares:", squares_dict()),
    # Tuples & Sets
    "tuple_test": lambda: print("Tuple:", tuple_test()),
    "unique_chars": lambda: print("Unique chars:", unique_chars()),
    # Advanced
    "deep_access": lambda: print("Deep access:", deep_access(DEFAULT_COURSES_DATA)),
    "course_dict": lambda: print("Course dict:", course_dict(DEFAULT_COURSES_DATA)),
    "find_course": lambda: print("Find EMT1201:", find_course(DEFAULT_COURSES_DATA, "EMT1201")),
}

def list_demos() -> None:
    """Print available demo names."""
    print("Available demos:")
    for name in sorted(_DEMOS.keys()):
        print(" -", name)

def run_demo(name: str) -> None:
    """Run a demo by name; print error if not found and handle exceptions."""
    fn = _DEMOS.get(name)
    if not fn:
        print(f"Demo '{name}' not found. Use --list to see available demos.")
        return
    try:
        fn()
    except Exception as exc:
        logger.exception("Demo '%s' raised an exception: %s", name, exc)

def parse_args(argv: List[str]) -> argparse.Namespace:
    """Parse CLI arguments."""
    p = argparse.ArgumentParser(description="Run assignment demos from main.py")
    p.add_argument("--list", action="store_true", help="List available demos")
    p.add_argument("--run", metavar="NAME", help="Run a specific demo by name")
    p.add_argument("--all", action="store_true", help="Run all demos (in order)")
    p.add_argument("--interactive", action="store_true", help="Run interactive prompts for a few examples")
    return p.parse_args(argv)

def interactive_session() -> None:
    """Small interactive session demonstrating safe input handling."""
    print("Interactive demo (press Ctrl+C to cancel any prompt).")
    try:
        r = safe_float("Enter radius for area calculation", default=5.0)
        print(f"Area for radius {r}: {area_circle(r):.4f}")

        c = safe_float("Enter Celsius temperature to convert", default=25.0)
        print(f"{c}°C -> {celsius_to_fahrenheit(c):.2f}°F")

        birth = safe_int("Enter birth year to calculate age", default=2000)
        print("Age:", calculate_age(birth))

    except KeyboardInterrupt:
        print("Interactive session aborted by user.")

def main(argv: Optional[List[str]] = None) -> None:
    """Main entry point for CLI usage."""
    args = parse_args(argv or sys.argv[1:])
    if args.list:
        list_demos()
        return
    if args.run:
        run_demo(args.run)
        return
    if args.all:
        for name in sorted(_DEMOS.keys()):
            print(f"\n=== {name} ===")
            run_demo(name)
        return
    if args.interactive:
        interactive_session()
        return

    # Default behavior: show summary and a few representative demos
    print("main.py — Python Data Structures Exercises (summary run)\n")
    print("Representative outputs:")
    run_demo("area_circle")
    run_demo("reverse_string")
    run_demo("add_course")
    run_demo("create_dict")
    run_demo("deep_access")
    print("\nUse --list to see all demos, --run NAME to run a specific demo, or --interactive for prompts.")

if __name__ == "__main__":
    main()
```
"""
Python Data Structures Assignment
Author: Akudo Samuel
Course: CIT2201
Date: 27 March 2026
"""

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
result_power = 2 ** 10
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
