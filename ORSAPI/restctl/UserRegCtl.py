from .BaseCtl import BaseCtl
from ORSAPI.utility.DataValidator import DataValidator
from service.models import UserData
from service.service.UserDataService import UserDataService
from service.service.EmailMessage import EmailMessage
from service.service.EmailService import EmailService
from django.http.response import JsonResponse
import json

class UserRegCtl(BaseCtl):
    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form["FirstName"] = requestForm["FirstName"]
        self.form["LastName"] = requestForm["LastName"]
        self.form["Gender"] = requestForm["Gender"]
        self.form["Email"] = requestForm["Email"]
        self.form["Password"] = requestForm["Password"]
        self.form["ConfirmPassword"] = requestForm["ConfirmPassword"]
        self.form["City"] = requestForm["City"]
        self.form["State"] = requestForm["State"]
        self.form["Zip"] = requestForm["Zip"]
        self.form["Country"] = requestForm["Country"]

    def input_validation(self):
        super().input_validation()
        inputError =  self.form["inputError"]
        if(DataValidator.isNull(self.form["FirstName"])):
            inputError["FirstName"] = "First Name can not be null"
            self.form["error"] = True
        if(DataValidator.isNull(self.form["LastName"])):
            inputError["LastName"] = "Last Name can not be null"
            self.form["error"] = True
        if(DataValidator.isNull(self.form["Email"])):
            inputError["Email"] = "Email Id can not be null"
            self.form["error"] = True
        if(DataValidator.isNotNull(self.form["Email"])):
            if(DataValidator.isemail(self.form["Email"])):
                self.form["error"] = True
                inputError["Email"] = "Email Id must be like abc@gmail.com"
        if(DataValidator.isNull(self.form["Password"])):
            inputError["Password"] = "Password can not be null"
            self.form["error"] = True
        if(DataValidator.isNull(self.form["ConfirmPassword"])):
            inputError["ConfirmPassword"] = "Confirm password can not be null"
            self.form["error"] = True  
        if(DataValidator.isNotNull(self.form["ConfirmPassword"])):
            if(self.form["Password"] != self.form["ConfirmPassword"]):
                inputError["ConfirmPassword"] = "Passwords are not Same"
                self.form["error"] = True
        if(DataValidator.isNull(self.form["Gender"])):
            inputError["Gender"] = "Gender can not be null"
            self.form["error"] = True
        
        if(DataValidator.isNull(self.form["City"])):
            inputError["City"] = "City can not be null"
            self.form["error"] = True 
        if(DataValidator.isNull(self.form["State"])):
            inputError["State"] = "State can not be null"
            self.form["error"] = True    
        if(DataValidator.isNull(self.form["Zip"])):
            inputError["Zip"] = "Zip can not be null"
            self.form["error"] = True
        if(DataValidator.isNull(self.form["Country"])):
            inputError["Country"] = "Country can not be null"
            self.form["error"] = True
        
        return self.form["error"]        

    def get(self,request,params={}):
        c = self.get_service().get(params["id"])
        res = {}
        if (c != None):
            res["data"] = c.to_json()
            res["error"] = False
            res["message"] = "Data found"
        else:
            res["error"] = True
            res["message"] = "No record found"
        return JsonResponse({"data":res["data"]})

    def form_to_model(self, obj):
        pk = int(self.form["id"])
        if (pk>0):
            obj.id = pk
        obj.FirstName = self.form["FirstName"]
        obj.LastName = self.form["LastName"]
        obj.Email = self.form["Email"]
        obj.Password = self.form["Password"] 
        obj.ConfirmPassword = self.form["ConfirmPassword"]
        obj.Gender = self.form["Gender"]
        obj.City = self.form["City"]
        obj.State = self.form["State"]
        obj.Zip = self.form["Zip"]
        obj.Country  = self.form["Country"]
        return obj

    def save(self,request,params={}):
        print('request body ---->',request.body)
        json_request = json.loads(request.body)
        self.request_to_form(json_request) 
        res = {}

        if (self.input_validation()):
            res["error"] = True
            res["message"] = ""
        else:
            user = UserData.objects.filter(Email = self.form["Email"])
            if (user.count()>0):
                res["error"] = True
                res["message"] = "Email Id already exists"
            else:
                emsg = EmailMessage()
                emsg.to = [self.form["Email"]]
                emsg.subject = "Registraion Successful"
                e = {}
                e["Email"] = self.form["Email"]
                e["Password"] = self.form["Password"]
                mailResponse = EmailService.send(emsg,"signup",e)
                if mailResponse == 1:
                    r = self.form_to_model(UserData())
                    UserDataService().save(r)
                    print('---->user reg r',r)
                    if (r != None):
                        
                        res["error"] = False
                        res["message"] = "Data has been Saved Successfully"
                    else:
                        res["error"] = True
                        res["message"] = "Data was not saved"
        return JsonResponse({"form":self.form,"data":res})

    def get_service(self):
        return UserDataService()