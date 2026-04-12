#Example of serializing a Python dictionary to JSON format and writing it to a file.
import json

python_dict = {
    "server": "webserver01",
    "os": "Linux",
    "services": ["http", "https", "ssh"]
}

# Serialize to JSON string
json_output_string = json.dumps(python_dict, indent=4)
print(json_output_string)

###################################

# Serialize to JSON file
with open('server_info.json', 'w') as f:
    json.dump(python_dict, f, indent=4)
