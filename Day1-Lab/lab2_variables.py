# variables.py

# --- Defining Variables ---
device_count = 5          # int: number of devices
average_latency = 15.5    # float: latency in milliseconds
hostname = "router1"      # str: device name
is_active = True          # bool: device status
name="Sarah"


# --- Displaying Variable Values ---
print("--- Device Information ---")
print(f"Hostname:        {hostname}")
print(f"Device Count:    {device_count}")
print(f"Avg Latency:     {average_latency} ms")
print(f"Active Status:   {is_active}")




# # --- Checking Data Types ---
print("\n--- Data Types ---")
print(f"Type of device_count:    {type(device_count)}")
print(f"Type of average_latency: {type(average_latency)}")
print(f"Type of hostname:        {type(hostname)}")
print(f"Type of is_active:       {type(is_active)}")



# # --- Type Conversion ---
# print("\n--- Type Conversion ---")
# device_count_float = float(device_count)
# print(f"device_count as float: {device_count_float}")

# port_str = "48"
# port_int = int(port_str)
# print(f"String '48' converted to integer: {port_int + 2}")  # Should print 50
