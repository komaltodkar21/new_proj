from django.shortcuts import render
from .forms import StuForm
from .models import User

# Create your views here.
def success(request):
    return render(request, "enroll/success.html")

def home(request):
    if request.method=="POST":
        form=StuForm(request.POST)
        if form.is_valid():
            print("This is validated data")
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            ad=form.cleaned_data['address']
            pwds=form.cleaned_data['password']
            rpws=form.cleaned_data['re_password']
            reg=User(name=nm,email=em,address=ad,password=pwds,re_password=rpws)
            reg.save()
            form=StuForm()
    else:
        form=StuForm()
    return render(request, "enroll/home.html",{'form':form})