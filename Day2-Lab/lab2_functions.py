#Write a function that takes a list of IP addresses and returns the number of addresses in the list.


#1.Define the Function --> general function
def count_ips(ip_list):
    #2.Count Elements and 3. Return Count
    """Returns the number of IP addresses in the provided list."""
    return len(ip_list)

# Sample list of IP addresses
# Define the list outside to reuse the function easily 
network_ips = ["192.168.1.1", "192.168.1.10", "192.168.1.200", "10.0.0.5"]
empty_ips = []


#Reuse the above function to count the number of IP addresses in the sample lists.
# Call the function and print the result
num_addresses = count_ips(network_ips)
print(f"Number of IP addresses in network_ips: {num_addresses}")

num_empty = count_ips(empty_ips)
print(f"Number of IP addresses in empty_ips: {num_empty}")
