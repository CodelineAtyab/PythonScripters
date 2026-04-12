"""
Problem Statement: Automating configuration changes is a core aspect of network automation. This lab demonstrates how to use netmiko’s send_config_set() method to push configuration commands to a network device.
Instructions:
1.	Create a Python script: Create a new Python file named lab3_send_config.py.
2.	Import ConnectHandler: Import the ConnectHandler class.
3.	Define device parameters: Use the same device dictionary as in previous labs.
4.	Define configuration commands: Create a list of strings, where each string is a configuration command. 
For example, to create a loopback interface: python     config_commands = [         "interface Loopback100",         "description Test Loopback from netmiko",         "ip address 10.10.10.1 255.255.255.0",         "no shutdown"     ] Or to add a static route: python     config_commands = [         "ip route 172.16.0.0 255.255.0.0 192.168.1.1"     ]
5.	Establish connection: Establish a connection to the device.
6.	Send configuration commands: Use net_connect.send_config_set() with your list of commands.
7.	Verify configuration (optional but recommended): After sending configuration, you might want to 
send a show run | section <interface/route> command to verify the changes.
8.	Disconnect: Ensure to disconnect from the device.
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

# Configuration commands to add a new Loopback interface
config_commands = [
    "interface Loopback100",
    "description Test Loopback from netmiko",
    "ip address 10.10.10.1 255.255.255.0",
    "no shutdown"
]

net_connect = None # Initialize net_connect to None

try:
    print(f"Connecting to {device['host']}...")
    net_connect = ConnectHandler(**device)
    print(f"Successfully connected to {device['host']}.")

    print("\nSending configuration commands...")
    output = net_connect.send_config_set(config_commands)
    print("\n--- Configuration Output ---")
    print(output)
    print("----------------------------")

    # Optional: Verify the configuration
    print("\nVerifying configuration...")
    verify_output = net_connect.send_command("show run | section Loopback100")
    print("\n--- Verification Output ---")
    print(verify_output)
    print("---------------------------")

except Exception as e:
    print(f"Error: {e}")

finally:
    if net_connect and net_connect.is_alive():
        net_connect.disconnect()
        print(f"Disconnected from {device['host']}.")
