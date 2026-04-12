"""
Problem Statement: After establishing a connection, a common task in network automation is to gather 
operational data from devices. This lab focuses on using netmiko’s send_command() method to execute a show 
command and display its output.
Instructions:
1.	Create a Python script: Create a new Python file named lab2_get_device_info.py.
2.	Import ConnectHandler: Import the ConnectHandler class.
3.	Define device parameters: Use the same device dictionary as in Lab 1.
4.	Establish connection: Establish a connection to the device.
5.	Send a command: Use net_connect.send_command() to execute a command like show ip interface brief.
6.	Print output: Print the received output. Optionally, explore netmiko’s capabilities for structured 
output parsing (e.g., use_textfsm=True if TextFSM is installed and templates are available).
7.	Disconnect: Ensure to disconnect from the device.
"""

from netmiko import ConnectHandler

# Define device parameters
device = {
    "device_type": "cisco_ios",
    "host": "0.0.0.0",  # Replace with your lab device IP
    "username": "username",
    "password": "password",
    "port": 22,
}

net_connect = None # Initialize net_connect to None

try:
    print(f"Connecting to {device['host']}...")
    net_connect = ConnectHandler(**device)
    print(f"Successfully connected to {device['host']}.")

    print("\nExecuting 'show ip interface brief'...")
    output = net_connect.send_command("show ip interface brief")
    print("\n--- Device Output ---")
    print(output)
    print("---------------------")

except Exception as e:
    print(f"Error: {e}")

finally:
    if net_connect and net_connect.is_alive():
        net_connect.disconnect()
        print(f"Disconnected from {device['host']}.")
