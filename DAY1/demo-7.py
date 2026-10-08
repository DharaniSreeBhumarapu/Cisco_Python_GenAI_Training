port = input('Enter port_Number: ')

if int(port) > 5000 and int(port) <6000:
    app_name = 'Flask'
else:
    app_name = 'WebApp'
    
print(f"App Name is:{app_name} Running Port Number is:{port}")