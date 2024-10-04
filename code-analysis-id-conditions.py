# Instructions

# Work with your assigned partner
# Review the code snippets below
# Circle each condition in each snippet
# Be prepared to share what you and your partner think the
# output will be for each code snippet

# Example 1
password = input("Enter your network password:\n")
if len(password) <= 8:
    print("Your password is too short! Passwords must be at least 8 characters long!")
else:
    print("Your password contains 8 or more characters!")



# Example 2
fruits = ['apple', 'banana', 'orange']
if 'mango' in fruits:
    print('Mango is in the list!')



# Example 3
passport_expired = False
is_us_citizen = True
if not passport_expired and is_us_citizen:
  print('You are eligible to renew your passport online or at any U.S. embassy.')
else:
  print('Either your passport is expired or you are not a U.S. citizen.')
  print('Please contact the nearest U.S. embassy for assistance with renewing your expired passport.')



# Example 4
age = 25
height = 65

if age >= 18 and height >= 60:
    print("You are eligible to ride the roller coaster.")
else:
    print("You are not eligible to ride the roller coaster.")



# Example 5
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You don't have to go to work today.")
else:
    print("It's a workday.")




# Example 6
is_raining = True
is_sunny = False

if is_raining and not is_sunny:
    print("It's a rainy day.")
else:
    print("It's not raining.")
