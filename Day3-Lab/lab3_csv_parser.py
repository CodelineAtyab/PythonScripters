'''
Lab 3: CSV Parsing
Objective: Read a CSV file containing network device information and print it in a formatted way.
Scenario: You receive a CSV file from a network inventory system, and you need to process this data to display device details.
Steps:
1.	Create a CSV file named network_devices.csv with the following content:
 	DeviceName,IPAddress,Location,Status
RouterA,192.168.1.1,Building1,Active
SwitchB,192.168.1.2,Building1,Active
FirewallC,10.0.0.1,Datacenter,Active
AP_D,172.16.0.1,Building2,Inactive
2.	Write a Python script using the csv module to read network_devices.csv and print each device’s information in a user-friendly format.
'''

# lab3_csv_parser.py
import csv

# Create a dummy CSV file for demonstration
csv_content = """
DeviceName,IPAddress,Location,Status
RouterA,192.168.1.1,Building1,Active
SwitchB,192.168.1.2,Building1,Active
FirewallC,10.0.0.1,Datacenter,Active
AP_D,172.16.0.1,Building2,Inactive
"""

with open("network_devices.csv", "w") as f:
    f.write(csv_content)

print("--- Parsing network_devices.csv ---")
# Open the CSV file in read mode
with open("network_devices.csv", "r") as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row
    header = next(reader)
    print(f"Header: {', '.join(header)}")


    # Iterate over each row in the CSV file
    for row in reader:
        # Assuming the order: DeviceName, IPAddress, Location, Status
        device_name, ip_address, location, status = row
        print(f"Device: {device_name:<10} | IP: {ip_address:<15} | Location: {location:<10} | Status: {status}")
print("-------------------------------------")
