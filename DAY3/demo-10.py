import pprint
dict={}
with open('Day-3/network.cfg',"r") as fobj:
    for var in fobj.readlines():
        var=var.strip()
        K,V=var.split('=')
        dict[K]=V # adding new data to dict

        
pprint.pprint(dict)

dict['Interface']='eth1'
dict['bootproto']='static'
dict['onboot']='yes'
dict['IP_Address'] = '192.168.0.1'
dict['prefix'] ='30'
dict['DNS1'] = '122.34.45.67'
dict['DHCP'] = 'yes'
print(f'\n updated Dict details:-')
pprint.pprint(dict)
fobj=open("new_network.cfg","w")
for var in dict:
    fobj.write(f'{var}={dict.get(var)}\n')

fobj.close()