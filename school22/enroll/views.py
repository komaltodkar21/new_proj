from django.shortcuts import render
from .forms import StuForm

# Create your views here.
# def home(request):
#     my_form=StuForm()
#     print(my_form.has_changed())  #False
#     print(my_form.changed_data)  #Returns changed data or []
#     print(my_form.is_valid)  #returns all data in terminal if it is valid
#     return render(request, 'enroll/home.html',{'form':my_form})

def success(request):
    return render(request,'success/success.html')

def home(request):
    if request.method == "POST":
        my_form=StuForm(request.POST)
        print(my_form.has_changed())
        print(my_form.changed_data)
        if my_form.is_valid():
            print('------------------')
            print("Student Name:",my_form.cleaned_data['name'])
            # print("Student Email:",my_form.cleaned_data['email'])
            # print("Student Address:",my_form.cleaned_data['address'])
            print("Student Password:",my_form.cleaned_data['password'])
            print("Student RE_Password:",my_form.cleaned_data['re_password'])
            # nm=my_form.cleaned_data['name']
            # em=my_form.cleaned_data['email']
            # ad=my_form.cleaned_data['address']
            # ps=my_form.cleaned_data['password']
            # print(nm,em,ad,ps)
            my_form=StuForm()
            return render(request, 'success/success.html')
    else:
        my_form=StuForm()
    return render(request, 'enroll/home.html',{'form':my_form})
