'''
Lab 1: Reading a Config File
Objective: Read a sample router configuration file and print each line.
Scenario: You have a simulated router configuration file (router_config.txt) and you 
need to read its contents line by line.
'''
'''
Steps:
1.	Create a file named router_config.txt with the following content:
 	hostname Router01
interface GigabitEthernet0/1
 ip address 192.168.1.1 255.255.255.0
 no shutdown
interface GigabitEthernet0/2
 ip address 192.168.2.1 255.255.255.0
 no shutdown
line vty 0 4
 password cisco
 login

 2.	Write a Python script to open router_config.txt in read mode and print each line.
'''


# Create a dummy router config file for demonstration
config_content = """
hostname Router01
interface GigabitEthernet0/1
 ip address 192.168.1.1 255.255.255.0
 no shutdown
interface GigabitEthernet0/2
 ip address 192.168.2.1 255.255.255.0
 no shutdown
line vty 0 4
 password cisco
 login
"""

with open("router_config.txt", "w") as f:
    f.write(config_content)




print("--- Reading router_config.txt ---")
# Open the configuration file in read mode
# with open("router_config.txt", "r") as config_file:
#     # Iterate through each line in the file and print it
#     for line in config_file:
#         print(line.strip()) # .strip() removes leading/trailing whitespace, including newline characters
# print("---------------------------------")

