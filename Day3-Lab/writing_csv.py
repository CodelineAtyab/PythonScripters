#Example of WRITING to a CSV file in Python using the csv module
import csv

devices = [
    ['router2', '10.0.0.1', 'Paris'],
    ['switch2', '10.0.0.2', 'Berlin']
]

with open('new_devices.csv', 'w', newline='') as csvfile: #newline='' prevents Python from adding extra blank lines between rows in the CSV.
    writer = csv.writer(csvfile)
    writer.writerow(['hostname', 'ip_address', 'location']) # Write header
    writer.writerows(devices)
