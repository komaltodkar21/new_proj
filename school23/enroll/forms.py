from django import forms
from .models import User

# class StuForm(forms.Form):
#     name=forms.CharField(max_length=20,error_messages={'required':"This field is required"})
#     email=forms.EmailField(error_messages={'required':"This field is mandatory"})
#     address=forms.CharField(max_length=40)
#     password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':"This field is required"})


class StuForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','address','password','re_password']