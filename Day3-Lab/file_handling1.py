# Example of using 'with' statement for file handling
with open('example.txt', 'w') as f:
    f.write('Hello, Python file handling!\n')
    f.write('This is a new line.')
    
# File 'f' is automatically closed here



# #Dealing with one file (Similar)
# # Writing to a file
with open('output.txt', 'w') as f:
    f.write('First line.\n')
    lines = ['Second line.\n', 'Third line.\n']
    f.writelines(lines)

# Reading from a file
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)

with open('output.txt', 'r') as f:
    for line in f:
        print(line.strip()) # .strip() removes leading/trailing whitespace, including newlines

