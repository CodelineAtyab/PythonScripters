"""
Problem Statement: In Day 5, you used paramiko to establish an SSH connection to a network device. For 
this lab, you will refactor that script to leverage the netmiko library, demonstrating its simplified approach 
to device connectivity.
Instructions:
1.	Install netmiko: If you haven’t already, install the netmiko library using pip: bash  pip install netmiko
2.	Create a Python script: Create a new Python file named lab1_netmiko_connect.py.
3.	Import ConnectHandler: Import the ConnectHandler class from the netmiko library.
4.	Define device parameters: Create a dictionary containing the device connection details, 
including device_type, host, username, and password. For device_type, use cisco_ios for a Cisco device or 
an appropriate type for your lab environment.
5.	Establish connection: Use a try-except block to establish a connection using ConnectHandler 
and print a success message. Ensure to disconnect using net_connect.disconnect() in a finally block.
"""

from netmiko import ConnectHandler

# Define device parameters
device = {
    "device_type": "cisco_ios",
    "host": "0.0.0.0",  # Replace with your lab device IP
    "username": "username",
    "password": "password",
    "port": 22,  # Default SSH port
}

try:
    print(f"Attempting to connect to {device['host']}...")
    net_connect = ConnectHandler(**device)
    print(f"Successfully connected to {device['host']} using netmiko!")

except Exception as e:
    print(f"Error connecting to {device['host']}: {e}")

finally:
    if 'net_connect' in locals() and net_connect.is_alive():
        net_connect.disconnect()
        print(f"Disconnected from {device['host']}.")
