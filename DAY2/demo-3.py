hosts = {}
print(f"Number of elements in the dictionary:{len(hosts)}") 
count = 0
while(count < 5):
    h = input("Enter a hostname:")
    ip = input("Enter a IP address:")
    hosts[h] = ip 
    count += 1
print(f"Number of elements in the dictionary:{len(hosts)}") 
for var in hosts:
    print(f"Hostname:{var}\t IP Address:{hosts[var]}") 
h = input("Enter a hostname:")
if h in hosts:
    hosts[h] = "127.0.0.1"  
else:
    print("sorry hostname {h} is not exists")
    hosts[h] = "127.0.0.1"
    print("Updated dict")
for var in hosts:
    print(f"\nHostname:{var}\t IP Address:{hosts[var]}") # iterate through the dictionary and display each hostname and IP address
