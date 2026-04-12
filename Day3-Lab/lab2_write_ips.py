'''
Lab 2: Writing to a File
Objective: Create a list of IP addresses and write them to a new text file, with each IP on a new line.
Scenario: You have a list of IP addresses that you need to save to a file for future use or as part of a report.
Steps:
1.	Define a Python list containing several IP addresses.
2.	Write a Python script to open a new file (e.g., ip_list.txt) in write mode and write 
each IP address from the list to a new line in the file.
'''

# lab2_write_ips.py

# List of IP addresses to write to a file
ip_addresses = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.31.20",
    "192.168.100.2"
]
path = " "
output_filename = "ip_list.txt"

print(f"--- Writing IP addresses to {output_filename} ---")
# Open the file in write mode. The `\n` in f.write() ensures each IP is on a new line.
with open(output_filename, "w") as f:
    for ip in ip_addresses[1:4]:
        f.write(ip + "\n")
print("Writing complete. Content of ip_list.txt:")

# Verify the content by reading the file back
# with open(output_filename, "r") as f:
#     print(f.read())
# print("------------------------------------------")
