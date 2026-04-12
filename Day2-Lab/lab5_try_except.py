#1.	Prompt for Input: Use the input() function to ask the user to enter a number.
#2.	Implement try-except: Place the code that converts the input to an integer inside a try block.
#3.	Handle ValueError: If a ValueError occurs during the conversion (i.e., the input is not a valid 
# number), catch it with an except ValueError: block and print an informative error message.
#4.	Success Message: If the conversion is successful, print a message confirming the entered number.

try:
    user_input = input("Please enter a number: ")
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
