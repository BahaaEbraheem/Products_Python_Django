from django.db import models
from products.models import Product

# Create your models here.


class Vedio(models.Model):
    name=models.CharField(max_length=50,default='أدخل اسم المستخدم')

    def __str__(self):
       return self.name

class User(models.Model):
    name=models.CharField(max_length=50,default='أدخل اسم المستخدم')
    products=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    vedios=models.ManyToManyField(Vedio)

    def __str__(self):
       return self.name
    
    
class Login(models.Model):
    username=models.CharField(max_length=50)   
    password=models.CharField(max_length=50)   
    
    
    def __str__(self):
       return self.username


