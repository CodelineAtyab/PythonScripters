'''
Lab 4: JSON Parsing
Objective: Parse a JSON string containing API response data and extract specific values.
Scenario: You’ve received a JSON response from a network device API call, and you need to extract information like the device’s hostname and uptime.
Steps:
1.	Define a Python string containing a sample JSON payload representing a device’s status.
2.	Write a Python script using the json module to parse this JSON string and extract the hostname, ip_address, and status.
'''

# lab4_json_parser.py
import json

# Sample JSON string representing a device's status from an API response
json_data_string = """
{
    "device_id": "XYZ789",
    "hostname": "core-router-01",
    "ip_address": "10.10.10.1",
    "status": "online",
    "uptime_seconds": 86400,
    "interfaces": [
        {"name": "GigabitEthernet0/1", "status": "up"},
        {"name": "GigabitEthernet0/2", "status": "down"}
    ]
}
"""

print("--- Parsing JSON Data ---")
# Parse the JSON string into a Python dictionary
device_info = json.loads(json_data_string)

# Extract and print specific values
print(f"Hostname: {device_info["hostname"]}")
print(f"IP Address: {device_info["ip_address"]}")
print(f"Status: {device_info["status"]}")
print("-------------------------")
