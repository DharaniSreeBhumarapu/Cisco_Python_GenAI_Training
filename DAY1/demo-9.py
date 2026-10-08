app_Name = input('Enter app name: ')

if(app_Name == "flask"):
    port = 5000
elif(app_Name == "fastAPI"):
    port = 8080
elif(app_Name == "prometheus"):
    port = 9090
else:
    app_Name = "web2.0"
    port = 8000

print(f"App Name is:{app_Name} Running Port Number is:{port}")
