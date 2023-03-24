from cmath import sin


try:
    from suds.client import Client
except ImportError :
    print("suds-py3 is not found ")

maths_client=Client('http://127.0.0.1:8000/maths/?wsdl')
print(maths_client) #print the service information
x=input("x= ?")
y=input("y= ?")
max=maths_client.service.max(x,y)
#print("max(",x,",",y,")= ",max)
#or
print(f'max({x},{y}) = {max}')
#or
#print('max(%s,%s)=%s' % (x,y,max))

x=input("x= ?")
y=input("y= ?")
min=maths_client.service.min(x,y)
#print("min(",x,",",y,")= ",min)
#or
print(f'min({x},{y}) = {min}')
#or
#print('min(%s,%s)=%s' % (x,y,min))

y=input("y= ?")
sin=maths_client.service.sin(y)
print('sin(%s)=%s' % (y,sin))


y=input("y= ?")
cos=maths_client.service.cos(y)
print('cos(%s0)=%s' % (y,cos))


