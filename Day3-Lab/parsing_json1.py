#Example of Parsing JSON Data (Deserialization)
import json

# # Sample JSON data as a string
# json_string = '{"device": "router1", "ip": "192.168.1.1", "status": "up"}'

# # Parse JSON string
# data = json.loads(json_string)
# print(f"Device Name: {data['device']}")
# print(f"IP Address: {data['ip']}")


############################################################


# Sample JSON data in a file
json_file_content = """
{
    "devices": [
        {
            "name": "switch1",
            "ip": "10.0.0.1",
            "vendor": "Cisco"
        },
        {
            "name": "access_point1",
            "ip": "10.0.0.2",
            "vendor": "Aruba"
        }
    ]
}
"""

with open('network_data.json', 'w') as f:
    f.write(json_file_content)


with open('network_data.json', 'r') as jsonfile:
    network_data = json.load(jsonfile)
    for device in network_data['devices']:
        print(f"Device: {device['name']}, IP: {device['ip']}, Vendor: {device['vendor']}")
