#define a function that takes two numbers as input and returns their sum.
def add_numbers(a, b):
    return a + b

#########################################
#define a function 
def no_return_function():
    print("This function does not return anything explicitly.")

##########################################################
#call the add_numbers function and print the result
result = add_numbers(5, 3)
print(f"The sum is: {result}")

########################################################
#call the no_return_function and print the result
none_result = no_return_function()
print(f"Return value of no_return_function: {none_result}")
