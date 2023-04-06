from email.policy import default
from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def to_json(self):
        data={
            "id": self.id,
            "name": self.name,
            "descriotion": self.description 
        }
        return data
    
    class Meta:
        db_table = "SOS_ROLE"


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login_id = models.EmailField()
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=50, default='')
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=50,default='')
    mobilenumber = models.CharField(max_length=50,default='')
    role_Id = models.IntegerField()
    role_Name = models.CharField(max_length=50)

    def to_json(self):
        data = {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "login_id": self.login_id,
            "password": self.password,
            "confirmpassword": self.confirmpassword,
            "dob": self.dob,
            "address": self.address,
            "gender": self.gender,
            "mobilenumber": self.mobilenumber,
            "role_Id": self.role_Id,
            "role_Name": self.role_Name,
        }
        return data
    class Meta:
        db_table = "SOS_USER"

class UserData(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length =20)
    Gender = models.CharField(max_length=20,default='')
    Email = models.EmailField()
    Password = models.CharField(max_length=20,default='')
    ConfirmPassword = models.CharField(max_length=20,default='')
    City = models.CharField(max_length=20,default='')
    State = models.CharField(max_length=20,default='')
    Zip = models.IntegerField()
    Country = models.CharField(max_length=20,default='')

    def to_jason(self):
        data = {
            "id" : self.id,
            "FirstName" : self.FirstName,
            "LastName" : self.LastName,
            "Gender" : self.Gender,
            "Email": self.Email,
            "Password" : self.PASSWORD,
            "ConfirmPassword" : self.ConfirmPassword,
            "City" : self.City,
            "State" : self.State,
            "Zip" : self.Zip,
            "Country" : self.Country

        }
        return data
    class Meta:
        db_table = "SOS_USERDATA"