"""
Walkthrough:
1.	Install paramiko: If you haven’t already, install the paramiko library using pip: bash pip install paramiko
2.	Create the Python script: Create a file named lab1_ssh_connect.py and add the following code.
Replace your_device_ip, your_username, and your_password with your lab device’s credentials.
"""

import paramiko

# Device connection details
hostname = 'hostname'  # e.g., '192.168.1.1'
username = 'username'
password = 'password'

client = None
try:
    # Create an SSH client
    client = paramiko.SSHClient()

    # Automatically add the server's host key (not recommended for production)
    # For production, you should manage known_hosts file properly.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the device
    print(f"Attempting to connect to {hostname}...")
    client.connect(hostname, username=username, password=password, timeout=5)
    print(f"Successfully connected to {hostname}")

except paramiko.AuthenticationException:
    print(f"Authentication failed for {hostname}. Check username and password.")
except paramiko.SSHException as ssh_err:
    print(f"SSH error connecting to {hostname}: {ssh_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if client:
        client.close()
        print(f"Connection to {hostname} closed.")
