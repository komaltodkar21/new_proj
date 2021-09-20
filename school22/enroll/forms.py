from django import forms
from django.forms.widgets import PasswordInput
from django.core import validators 

# class StuForm(forms.Form):
#     name=forms.CharField(max_length=20,error_messages={'required':"This field is required"})
#     email=forms.EmailField(error_messages={'required':"This field is required"})
#     address=forms.CharField(max_length=40,error_messages={'required':"This field is required"})
#     password=forms.CharField(Widget=forms.PasswordInput,error_messages={'required':"This field is required"})

# To print error messages
# class StuForm(forms.Form):
#     name=forms.CharField(validators=[validators.MaxLengthValidator(10)])
#     email=forms.EmailField()
#     address=forms.CharField(validators=[validators.MaxLengthValidator(20)])
#     password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':"This field is required"})

    # def clean_name(self):
    #     name=self.cleaned_data['name']
    #     if len(name)<4:
    #         raise forms.ValidationError("Enter more than 4 characters")

    # def clean_email(self):
    #     email=self.cleaned_data['email']
    #     if len(email)<15:
    #         raise forms.ValidationError("Enter more than 15 characters")

    # def clean_address(self):
    #     address=self.cleaned_data['address']
    #     if len(address)<20:
    #         raise forms.ValidationError("Enter more than 20 characters")

    # def clean_password(self):
    #     password=self.cleaned_data['password']
    #     if len(password)<8:
            # raise forms.ValidationError("Enter more than 8 characters")

# complete form validation in django
# class StuForm(forms.Form):
#     name=forms.CharField(max_length=20,error_messages={'required':"This field is required"})
#     email=forms.EmailField(error_messages={'required':"This field is required"})
#     address=forms.CharField(max_length=40,error_messages={'required':"This field is required"})
#     password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':"This field is required"})

#     def clean(self):
#         cleaned_data=super().clean()
#         valname=self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
#         valaddress=self.cleaned_data['address']
#         valpassword=self.cleaned_data['password']
#         if len(valname)<4:
#             raise forms.ValidationError[("Enter more than 4 characters")]

#         valemail=self.cleaned_data['email']
#         if len(valemail)<15:
#             raise forms.ValidationError("Enter more than 15 characters")

#         valaddress=self.cleaned_data['address']
#         if len(valaddress)<20:
#             raise forms.ValidationError("Enter more than 20 characters")

#         valpassword=self.cleaned_data['password']
#         if len(valpassword)<8:
#             raise forms.ValidationError("Enter more than 8 characters")

class StuForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            validators.MaxLengthValidator(4),
            validators.MaxLengthValidator(10)]
            )
    re_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd=cleaned_data['password']
        valre_pwd=cleaned_data['re_password']
        if valpwd != valre_pwd:
            raise forms.ValidationError('Please enter correct password')