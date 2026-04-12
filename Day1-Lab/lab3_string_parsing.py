# string_parsing.py

log_entry = "[INFO] Device router-1 connected from 192.168.1.10 on port 22"

print("Original log entry:")
print(log_entry)
print()


# --- Method 1: Using split() ---
# split() with no argument splits on any whitespace
parts = log_entry.split()
hostname = parts[2]
ip_address = parts[5]
port = parts[8]
splt= log_entry[0:5:2]
print(splt)


# print("--- Parsed using split() ---")
print(f"Hostname:   {hostname}")
print(f"IP Address: {ip_address}")
print(f"Port:       {port}")
print()



# --- Method 2: Using string methods ---
# strip() to removes unwanted characters
clean_entry = log_entry.replace("[INFO] ", " ")
print("--- Cleaned Entry ---")
print(clean_entry)



# --- Checking string content ---
if "connected" in log_entry:
    print("\nStatus: Device is connected.")
if log_entry.startswith("[INFO]"):
    print("Log Level: Informational")
