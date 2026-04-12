'''
1.	Define File Path: Choose a path for a file that you know does not exist (e.g., 'non_existent_config.txt').
2.	Implement try-except: Place the file opening operation (open()) inside a try block.
3.	Handle FileNotFoundError: Catch the FileNotFoundError with an except FileNotFoundError: block and print a 
user-friendly message indicating that the file could not be found.
4.	Read and Print (if successful): If the file is opened successfully (which it won’t be in this lab,but good practice), 
you would typically read its content and print it. For this lab, the else block can confirm the file was processed.

'''

file_path = "non_existent_config.txt"

try:
    with open(file_path, 'r') as f:
        content = f.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Successfully processed '{file_path}'.")
