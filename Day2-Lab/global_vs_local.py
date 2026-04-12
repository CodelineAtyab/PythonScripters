#Global vs Local Variables
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(global_var) # Accessible
    print(local_var)  # Accessible

my_function()
print(global_var) # Accessible
# print(local_var) # This would cause an error (NameError)

def modify_global():
    global global_var
    global_var = "I am modified global"

modify_global()
print(global_var)
