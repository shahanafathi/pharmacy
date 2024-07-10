from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission



class CustomeUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    dob= models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True, unique=True) 
    usertype=models.CharField(max_length=200)
    certification=models.FileField(null=True,blank=True)
    address=models.CharField(null=True,blank=True,max_length=100)
    confirm_password = models.CharField(null=True, blank=True, max_length=100)
    status=models.CharField(max_length=100,null=True, blank=True,default='pending')
    

class medicine(models.Model):
    pharmacy_id = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=100)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(null=True, blank=True, max_length=100)
    manufacturer = models.DateField()
    quantity = models.IntegerField(null=True, blank=True, unique=True)
    expiry_date = models.DateField()
    status= models.CharField(null=True, blank=True, max_length=100)
    brandname=models.CharField(null=True, blank=True, max_length=100)
    genericname=models.CharField(null=True, blank=True, max_length=100)
    strength=models.IntegerField(null=True, blank=True                                                                  )
    Image=models.FileField(null=True,blank=True)
    
    # def __str__(self):
    #     return self.name
    
        
        
class order(models.Model):
    medicine_id = models.ForeignKey(medicine, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status= models.CharField(null=True, blank=True, max_length=100)
    quantity = models.IntegerField(null=True, blank=True, unique=True)
    
 

class cart(models.Model):
    medicine_id = models.IntegerField(null=True, blank=True, unique=True)
    user_id = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=True, blank=True, unique=True)
    

            
class wishlist(models.Model):
    medicine_id = models.IntegerField(null=True, blank=True, unique=True)
    user_id = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
  