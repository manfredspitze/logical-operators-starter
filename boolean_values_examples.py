# Python: Working with Boolean Values (True/False)

# Example 1
age = 25
is_adult = age >= 18

if is_adult:
    print("You are an adult.")
else:
    print("You are a minor.")


# Example 2
is_raining = True

if is_raining:
    print("Don't forget your umbrella!")
else:
    print("Enjoy the sunny day!")


# Example 3
is_sunny = True
is_warm = False

if is_sunny and is_warm:
    print("Perfect weather for a picnic!")
elif is_sunny or is_warm:
    print("It's a nice day, but not ideal for a picnic.")
else:
    print("Stay indoors, it's not pleasant outside.")



# Example 4
age = 30
is_student = True

if (age < 25) and is_student:
    print("You are eligible for the student discount at the movie theater.")
else:
    print("You are not eligible for the student discount at the movie theater.")
