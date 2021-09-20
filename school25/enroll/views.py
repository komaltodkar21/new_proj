from django.shortcuts import render

# Create your views here.
from datetime import datetime, timedelta

def home(request):
    return render(request, 'enroll/home.html')

def set_cookie(request):
    res=render(request,'enroll/setcookie.html')
    res.set_cookie('f_name',"Ankit")
    res.set_cookie('l_name',"Kumar",path="/home")
    res.set_cookie('address',"Delhi",max_age=60*60*24*5)
    # res.set_cookie('address',"Delhi",expires= datetime.utcnow() + timedelta(days=2))
    return res
    
def get_cookie(request):
    # nm=request.COOKIES['f_name']
    # ln=request.COOKIES['l_name']
    # ad=request.COOKIES['address']
    nm=request.COOKIES.get('f_name')
    ln=request.COOKIES.get('l_name')
    ad=request.COOKIES.get('address')
    return render(request,'enroll/getcookie.html',{'nm':nm,'ln':ln,'ad':ad})

def del_cookie(request):
    res=render(request,'enroll/delcookie.html')
    res.delete_cookie('f_name')
    res.delete_cookie('l_name')
    res.delete_cookie('address')
    return res