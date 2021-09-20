from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','roll','address']
        labels={'name':"Enter Name",'roll':"Enter Roll",'address':"Enter address"}
        # help_text={'name':"Enter your name here!!!"}
        # error_messages={'name':{'required':'Enter your password'},
        #                 'roll':{'required':'Enter your roll'},
        #                 'address':{'required':'Enter your address'}
        #                 }
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter your name here'}),
        #     'roll':forms.PasswordInput(attrs={'placeholder':'Enter Correct Password'}),
        #     'address':forms.Textarea(attrs={'placeholder':'Enter Correct Address'}),
        #     }

