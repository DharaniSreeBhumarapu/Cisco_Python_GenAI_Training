host = [] # empty list
print(f"Number of elements in the list:{len(host)}") # display number of elements in the list

c = 0
while c < 5:
    h = input("Enter a hostname:")
    host.append(h) 
    c = c + 1

print(f"\nNumber of elements in the list:{len(host)}") 

for var in host:
    print(var)

host_name  = input("Enter a hostname:")
if host_name in host:
    host[-1] = host_name 
else:
    host.append(host_name) 

print("\n") 
for var in host:
    print(var)
    