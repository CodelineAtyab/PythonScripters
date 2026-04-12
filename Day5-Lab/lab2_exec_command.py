"""
Walkthrough:
1.	Create the Python script: Create a file named lab2_exec_command.py and add 
the following code. Remember to replace the placeholder credentials and IP.
"""
#You can try it with the VirtualBox machine 
import paramiko

# Device connection details
hostname = 'hostname'  # e.g., '192.168.1.1'
username = 'username'
password = 'password'
command_to_execute = 'show version' # Or 'ls -l' for a Linux VM

client = None
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password, timeout=5)
    print(f"Successfully connected to {hostname}")

    print(f"Executing command: '{command_to_execute}'")
    stdin, stdout, stderr = client.exec_command(command_to_execute)

    output = stdout.read().decode().strip()
    errors = stderr.read().decode().strip()

    if output:
        print("\n--- Command Output ---")
        print(output)
    if errors:
        print("\n--- Command Errors ---")
        print(errors)

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
