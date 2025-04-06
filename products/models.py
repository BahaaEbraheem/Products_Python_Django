from django.db import models

# Create your models here.
class Product(models.Model):

    productList=[
         ('phone','phone'),
          ('computer','computer'),
           ('hand wash','hand wash'),
    ]
      
    name=models.CharField(max_length=100,default='Default Product Name',verbose_name='Title')
    category=models.CharField(max_length=100,choices=productList,null=True,blank=True)
    content=models.TextField(null=True,blank=True,verbose_name='Description')  #يمكن حفظه بشكل فارغ null=True # blank=True وهذا الحقل غير مطلوب
    price=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    image=models.ImageField(upload_to='photos/%y/%m/%d',default='photos/no_image.png',verbose_name='Photo')
    isActive=models.BooleanField(default=True)

    
    def __str__(self): return self.name
    
    class Meta :
         verbose_name = 'المنتجات'