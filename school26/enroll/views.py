from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'enroll/home.html')

def set_session(request):
    request.session['f_name']='Komal'
    request.session['l_name']='Todkar'
    request.session['roll']=50
    request.session['address']='Pune'
    return render(request,'enroll/setsession.html')
    # return HttpResponse("Session is set!!!")

def get_session(request):
    fn=request.session.get('f_name')
    ln=request.session.get('l_name')
    rl=request.session.get('roll')
    ad=request.session.get('address')
    keys=request.session.keys()
    items=request.session.items()
    age=request.session.setdefault('age','26')
    return render(request,'enroll/getsession.html',{'f_name':fn,'l_name':ln,'roll':rl,'address':ad})
    # return HttpResponse("My session name is:{0} and {1}'.format(f_name,l_name))

def del_session(request):
    if 'f_name' is request.session:
        del request.session['f_name']
    if 'l_name' is request.session:
        del request.session['l_name']
    
    del request.session['email']  #not availabe key

    if 'address' is request.session:
        del request.session['address']
    res=render(request, 'enroll/delsession.html')
    return res

# def del_session(request):
#     res=request.session.flush()
#     clear=request.session.clear()
#     return render(request,'enroll/delsession.html',{'res':res})


