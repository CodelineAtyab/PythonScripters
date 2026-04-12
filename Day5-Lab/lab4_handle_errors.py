"""
Walkthrough:
1.	Create the Python script: Create a file named lab4_handle_errors.py and add
the following code. Use your device details.
"""

import paramiko

# Device connection details
hostname = 'your_device_ip'  # e.g., '192.168.1.1'
username = 'your_username'
password = 'your_password'
# A command that will likely fail on a Linux/Cisco device
command_to_execute = 'showw version' # Typo for 'show version' or 'nonexistent_command'

client = None
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password, timeout=5)
    print(f"Successfully connected to {hostname}")

    print(f"Executing command: '{command_to_execute}' (expecting error)")
    stdin, stdout, stderr = client.exec_command(command_to_execute)

    output = stdout.read().decode().strip()
    errors = stderr.read().decode().strip()

    if output:
        print("\n--- Command Output (unexpected) ---")
        print(output)
    if errors:
        print("\n--- Command Errors ---")
        print(errors)
    else:
        print("No errors reported by the remote device, but command might not have run as expected.")

except paramiko.AuthenticationException:
    print(f"Authentication failed for {hostname}. Check username and password.")
except paramiko.SSHException as ssh_err:
    print(f"SSH error connecting to {hostname}: {ssh_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if client:
        client.close()
        print(f"\nConnection to {hostname} closed.")
