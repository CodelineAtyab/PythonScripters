#Example
try:
    # Code that might raise an exception
    result = 10 / 0
except:
    # Code to handle the exception
    print("Error: Cannot divide by zero!")
print()
print()
"=================================================="

#Example with try, except, else, and finally
def safe_division(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution of safe_division complete.")

print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division(10, "a"))
