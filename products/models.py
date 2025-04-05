from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100,default='Default Product Name')
    content=models.TextField(default='Default Product Content')
    price=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    image=models.ImageField(upload_to='photos/%y/%m/%d',default='photos/no_image.png')
    isActive=models.BooleanField(default=True)


    
    
    
