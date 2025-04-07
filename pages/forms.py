from django import forms

from pages.models import Login

# class LoginForm(forms.Form):
#      username=forms.CharField(max_length=50,initial='enter username',disabled=False)   
#      password=forms.CharField(max_length=50,initial='enter password',widget=forms.PasswordInput,required=True)   
    
class LoginForm(forms.ModelForm):
     class Meta:
          model = Login
          fields = '__all__'