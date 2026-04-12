"""
Walkthrough:
1.	Generate an SSH Key Pair (if you don’t have one): Open your terminal 
and run: bash     ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa_paramiko Press Enter for no passphrase (for lab 
purposes). This will create id_rsa_paramiko (private key) and id_rsa_paramiko.pub (public key).
2.	Copy Public Key to Remote Device: You need to copy the content of ~/.ssh/id_rsa_paramiko.pub to the ~/.ssh/authorized_keys file on 
your remote Linux VM or configure it on your network device if it supports SSH key authentication. For a Linux
VM, you can use ssh-copy-id or manually append the public key: bash     ssh-copy-id -i ~/.ssh/id_rsa_paramiko.pub your_username@your_device_ip Or manually: bash     cat ~/.ssh/id_rsa_paramiko.pub | ssh your_username@your_device_ip 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys'
3.	Create the Python script: Create a file named lab3_ssh_key_auth.py and add the 
following code. Update your_device_ip and your_username.
"""
#1. Activate the virtual machine

import paramiko

# Device connection details
hostname = 'your_device_ip'  # e.g., '192.168.1.1'
username = 'your_username' #e.g, vboxuser
private_key_path = '~/.ssh/id_rsa_paramiko' # Path to your private key

client = None
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Load the private key
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

    # Connect using the private key
    print(f"Attempting to connect to {hostname} using SSH key...")
    client.connect(hostname, username=username, pkey=private_key, timeout=5)
    print(f"Successfully connected to {hostname} using SSH key.")

    stdin, stdout, stderr = client.exec_command('hostname') # Example command
    output = stdout.read().decode().strip()
    print(f"Hostname: {output}")

except paramiko.AuthenticationException:
    print(f"Authentication failed for {hostname}. Check username, private key path, or if public key is on device.")
except paramiko.SSHException as ssh_err:
    print(f"SSH error connecting to {hostname}: {ssh_err}")
except FileNotFoundError:
    print(f"Private key file not found at {private_key_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if client:
        client.close()
        print(f"\nConnection to {hostname} closed.")
