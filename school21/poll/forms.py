from django import forms
from django.forms.widgets import PasswordInput

CHOICES = ((True, 'Oui'), (False, 'Non'))
SIZE = [
    ['Large','L'],
    ['Medium','M'],
]

class StudentForm(forms.Form):
    name=forms.CharField(max_length=20,initial='abcd')
    email=forms.EmailField(initial='abc@gmail.com',help_text="Enter your Email")
    contact=forms.IntegerField(initial='6548760')
    salary=forms.HiddenInput()
    age=forms.HiddenInput()
    address=forms.CharField(max_length=20,initial='12 delhi',widget=forms.Textarea)
    pin=forms.CharField(
        required="True",
        label="Pincode",
        label_suffix="+>",
        error_messages={'required':"Please enter your address"},
        )
    gender=forms.CharField(initial='M')
    userpass=forms.CharField(widget=PasswordInput,max_length=15,min_length=4)
    option=forms.BooleanField(initial=False)
    choose=forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
    size=forms.CharField(widget=forms.RadioSelect(choices=SIZE))
    feedback=forms.CharField(widget=forms.TextInput(attrs={'class':"mycss1 mycss2",'id':"uniqueid"}))