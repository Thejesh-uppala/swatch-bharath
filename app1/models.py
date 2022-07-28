from django.db import models
class User(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Servicetype = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    Phonenumber = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Confirmpassword = models.CharField(max_length=50)

    #converts objects to string 
    def __str__(self) -> str:
        return self.Username

class Item(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Itemname = models.CharField(max_length=50)
    Price= models.CharField(max_length=50)
    Image = models.ImageField(upload_to="img/")
    #converts objects to string 
    def __str__(self) -> str:
        return self.Username   

class Posts(models.Model):
    Postno = models.CharField(max_length=10)
    Image = models.ImageField(upload_to="img/")
    Postdetails = models.CharField(max_length=1000)
    #converts objects to string 
    def __str__(self) -> str:
        return self.Postno   
