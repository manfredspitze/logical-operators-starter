# Student name
# Current date
# Practice: Logical NOT Operator in Python

# Use the logical NOT operator to reverse each condition below
# In other words, use NOT to make a True condition False
# and a False condition True

# Task 1
# HINT: You'll have to update the print statement after you use the NOT operator!
x = True
if x:
    print("x is True")

# SOLUTION
x = True
if not x:
    print("x is False")

# Task 2
age = 18
if age >= 18:
    print("You are an adult")

# SOLUTION

# Task 3
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is in the list!")
# SOLUTION
fruits = ["apple", "banana", "orange"]
if "apple" not in fruits:
    print("Apple is not in the list")
  
# Task 4
# HINT: You'll have to update the print statement after applying the NOT operator
is_raining = True
is_cold = False
if is_raining and is_cold:
    print("It's cold and raining")
# SOLUTION
is_raining = True
is_cold = False
if not (is_raining and is_cold):
    print("It's not cold and raining")
  
# Task 5
# HINT: You'll have to update the print statement after applying the NOT operator
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("It's either a weekend or a holiday")
  
# SOLUTION
is_weekend = True
is_holiday = False
if not (is_weekend or is_holiday):
    print("It's neither a weekend nor a holiday")
