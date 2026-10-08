wobj=open("r1.log","w")
wobj.write("Sample data\n")
wobj.write("product name is: PA Cost is:4565\n")
pname='p8'
pcost=35353.36
wobj.write(f'productname is: {pname} Cost is: {pcost}\n ')
wobj.write('--------------------------------------\n')
wobj.close()