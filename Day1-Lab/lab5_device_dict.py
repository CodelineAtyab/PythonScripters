# device_dict.py

# --- Creating a dictionary ---
device = {
    "hostname":    "core-switch-1",
    "ip":          "192.168.1.1",
    "device_type": "switch",
    "vendor":      "Cisco",
    "model":       "Catalyst 9300",
    "ports":       48
}


# --- Accessing values ---
print("--- Device Details ---")
print(f"Hostname:    {device['hostname']}")
print(f"IP Address:  {device['ip']}")
print(f"Vendor:      {device['vendor']}")
print(f"Model:       {device['model']}")
print(f"Port Count:  {device['ports']}")


# --- Adding a new key ---
device["location"] = "Data Center A, Rack 3"
print(f"\nLocation:    {device['location']}")


# --- Modifying a value ---
device["ports"] = 52
print(f"Updated Ports: {device['ports']}")


# --- Iterating through all key-value pairs ---
print("\n--- Full Device Profile ---")
for key, value in device.items():
    print(f"  {key:<15}: {value}")


# # --- Creating a list of devices ---
network_devices = [
    {"hostname": "router-1",  "ip": "10.0.0.1", "type": "router"},
    {"hostname": "switch-1",  "ip": "10.0.0.2", "type": "switch"},
    {"hostname": "firewall-1","ip": "10.0.0.3", "type": "firewall"},
]


# print("\n--- Network Inventory ---")
for dev in network_devices:
    print(f"  {dev['type'].upper():<10} | {dev['hostname']:<12} | {dev['ip']}")
user_name=input("Please enter your name")








