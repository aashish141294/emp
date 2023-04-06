from django.views.decorators.csrf import csrf_exempt
from .restctl.ForgetPasswordCtl import ForgetpasswordCtl
from .restctl.LoginCtl import LoginCtl
from .restctl.RegistrationCtl import RegistrationCtl
from .restctl.UserRegCtl import UserRegCtl


# Create your views here.

def info(request,page,action):
    print("request method -->",request.method)
    print("page -->",page)
    print("action -->",action)
    print("Base path -->",__file__)

@csrf_exempt
def action(request,page,action='get',id=0,pageNo=1):
    print("Id -->",id)
    info(request,page,action)
    methodCall = page + "Ctl()." + action + "(request,{'id':id,'pageNo':pageNo})"
    response = eval(methodCall)
    return response