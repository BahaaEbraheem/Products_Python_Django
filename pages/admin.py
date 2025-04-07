from django.contrib import admin

from pages.forms import LoginForm
from .models import Product, User ,Vedio,Login

# Register your models here.


admin.site.register(User)
admin.site.register(Vedio)
admin.site.register(Login)