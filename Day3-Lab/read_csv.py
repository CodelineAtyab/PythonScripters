#Example of READING a CSV file in Python using the csv module
import csv

# Sample CSV content
csv_data = """
hostname,ip_address,location
router1,192.168.1.1,New York
switch1,192.168.1.2,London
firewall1,192.168.1.3,Tokyo
"""

with open('devices.csv', 'w') as f:
    f.write(csv_data)

with open('devices.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) # Read header row
    print(f"Header: {header}")
    for row in reader:
        print(f"Device: {row[0]}, IP: {row[1]}, Location: {row[2]}")
