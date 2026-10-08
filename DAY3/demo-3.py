fobj=open('C:/Users/Admin/downloads/emp.csv','r')
L=fobj.readlines()
fobj.close()

for var in L:
    print(var.strip())  #strip() removes leading and trailing whitespace characters, including newline characters

print("\n")
total=0
for var in L:
    if 'sales' in var:
        var=var.strip()
        eid,ename,edept,eplace,ecost=var.split(',')
        total+=int(ecost)
        print(f'EMP Nmae is:{ename.title()} and\t Working Dept is:{edept.upper()}')
    print("_"*35)
    print(f"sum of sales dept emp's cost is:{total}")
    print("_"*35)