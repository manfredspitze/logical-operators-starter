## Python: Logical Operators
## Practice
---
### Getting Started
- Start by creating NEW project folder on your workstation desktop
- Use VS Code to save your work (temporarily) to your workstation folder
  
- Create a GitHub repo named: **logical_operators_starter**
    - Upload your project files to the repo
    - **No need to share your repo with your teacher**
    - Teacher will discuss your work with you **during Teacher Time**
---

### Coding Tasks

- Use comments to label each task in your script
  - Example: # Task 1, # Task 2, etc.
- Use f-strings to display the output for each task

#### Task 1

- Define a variable `grade` and assign it a numeric value
- Define a variable `is_extra_credit* and assign it a Boolean value of either `True` or `False`
- If the condition is true, let the user know they earned an A on their quiz
- Otherwise, let the user know they got a grade lower than an A on their quiz

#### Task 2

- Define two variables, `age` and `height`, and assign a numeric value to each
  - The user's height should be stated in inches (so 5'10" would be equal to **60** inches, for example)
- Create a compound condition that checks the user's age and height to see if they are eligible to drive an ATV at an ATV course
- If the user is 18 or older **and** at least 60 inches tall, print a message informing them that they can purchase a ticket to run the ATV course
- Otherwise, let the user know they haven't met the minimum requirements to drive the ATV on the course

#### Task 3

- Define a Python list of fruits named `fruits`
- Add 3 - 5 fruits to the list, all in lowercase characters
- Prompt the user to enter the name of a fruit
- Write an if statement with a compound condition that checks to see if the user's input:
  - is contained in the list of fruits
  - starts with a lowercase 'a'
- If the user's input meets both criteria, let the user know that the name of the fruit they entered starts with a lowercase 'a'
- Otherwise, tell the user that their fruit wasn't found in the list or that their fruit didn't start with a lowercase 'a'

#### Task 4

- Define a Python list of colors named `colors`
- Add 4 - 5 colors to the list, all in lowercase characters
- Prompt the user to enter a color
- Write an if statement with a compound condition that checks to see if the user's input was found in the list or if the user's input -- in lowercase -- was the color *purple*
- If the color the user entered is present in the list or equal to *purple*, display a message to that effect
- Otherwise, tell the user the color was not found or was not the color *purple*

#### Task 5

- Define a Python list of integers named `numbers`
- Prompt the user to enter an integer
- Write an if statement with a compound condition that:
  - uses the `in` operator to check to see if the integer the user entered is present in the list **and** has a remainder of zero (0) **or** is the number 3
- If the compound condition evaluates to `True`, let the user know the integer they entered was even or the number three
- Otherwise, tell the user the integer they entered was not even and was not the number three
