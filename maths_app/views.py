from email.mime import application
from wsgiref.validate import validator
from spyne.service import ServiceBase
from spyne.model.primitive import Double
from spyne.decorator import rpc
import math
from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django .views.decorators.csrf import csrf_exempt
class MathService(ServiceBase):
    
    @rpc (Double (nillable=False),Double (nillable=False),_returns =Double)
    def min(self,x,y):
        if(x<y):
            return x
        return y 
    @rpc (Double (nillable=False),Double (nillable=False),_returns =Double)
    def max(self,x,y):
        if(x>y):
            return x
        return y 
    @rpc (Double (nillable=False),_returns =Double)
    def sin(self,x):
        return math.sin(x)
    @rpc (Double (nillable=False),_returns =Double)
    def cos(self,x):
        return math.cos(x)
 
#création de l'application Django 
soap_app= Application([MathService],
                       tns='math.isg.tn',
                        in_protocol= Soap11(validator='lxml'), #for the soap request message
                         out_protocol= Soap11(), #for the soap response message
                      )
# lxml is a validator library. it's used if the soap request is well written 
django_app=DjangoApplication(soap_app)
my_app=csrf_exempt(django_app)

       
 
    