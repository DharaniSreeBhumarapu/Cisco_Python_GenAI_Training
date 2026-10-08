elogin_status = True

ename = input("Enter employee name: ")

eage = input(f"Enter {ename} age: ")

ecost = input(f"Enter {ename} basic salary: ")

tax = float(ecost) * 0.18 
gs = tax + float(ecost)

print(f'''Employee Name:{ename}
---------------------------------------
{ename} Age is:{eage}
---------------------------------------
{ename} Basic Salary is:{ecost}
---------------------------------------
{ename} Login Status is:{elogin_status}
-----------------------------------------
Tax is:{tax}
-----------------------------------------
Total Salary is:{gs}
----------------------------------------''')