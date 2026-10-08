import time
devices=['switches','routers','ethernet','rs232']
config={'ID':'A-123','app':'demoapp','port':3030,'fname':'etc/app.cfg'}
wobj=open("r2.log","w")
for var in devices:
    wobj.write(f"Device name:{var}\n")

wobj.write("----done-----\n")
'''
ID=A-123
app=demoapp
port=3030
fname=etc/app.cfg
'''
wobj.write(f"created on:{time.ctime()}\n")
wobj.close()