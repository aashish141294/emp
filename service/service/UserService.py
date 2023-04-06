from sqlite3 import Cursor
from service.models import User
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection

'''
It contains User business logics.
'''
class UserService(BaseService):
   
    def authenticate(self,params):
        userList = self.search2(params)
        print("----USerservice authenticate params = {} ,userList = {} -----".format(params,userList)) 
        if (userList.count() == 1):
            return userList[0]
        else:
            return None

    
    def search2(self,params):
        q = self.get_model().objects.filter()
        print("----userService search2 q ={}----".format(q))

        val = params.get("login_id", None)
        if(DataValidator.isNotNUll(val)):
            q= q.filter(login_id = val)

        val =params.get("password", None)
        if(DataValidator.isNotNUll(val)):
            q =q.filter(password = val)
        return q

    
    
    def get_login_id(self,login_id):
        self.get_model().objects.all()

    
    def get_model(self):
        return User
