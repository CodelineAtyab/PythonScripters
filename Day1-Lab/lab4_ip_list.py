# ip_list.py

# --- Creating a list ---
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
print("Initial list:", ip_addresses)


# # --- Adding elements ---
ip_addresses.append("10.0.0.4")
print("After append:", ip_addresses)


# # --- Removing an element ---
ip_addresses.remove("10.0.0.2")
print("After remove:", ip_addresses)


# # --- Accessing elements ---
element = ip_addresses[0]
print(element)
print(len(ip_addresses))

print(f"\nFirst IP:  {ip_addresses[0]}")
print(f"Last IP:   {ip_addresses[-1]}")
print(f"Total IPs: {len(ip_addresses)}")




# ##########################################################################


#NOT NEEDED
# --- Iterating through the list ---
print("\n--- All IP Addresses ---")
for index, ip in enumerate(ip_addresses, start=1):
    print(f"  {index}. {ip}")


# --- Checking membership ---
target = "10.0.0.3"
if target in ip_addresses:
    print(f"\n{target} is in the list.")
else:
    print(f"\n{target} is NOT in the list.")
