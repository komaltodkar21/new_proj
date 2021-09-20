from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def homeview(request):
    # stuform=StudentForm()
    # stuform=StudentForm(auto_id=False)
    # stuform=StudentForm(auto_id=True)
    # stuform=StudentForm(auto_id="myform")
    stuform=StudentForm(label_suffix=':')
    stuform.order_fields(field_order=[
        'email',
        'name',
        'contact',
        'option',
        'gender',
        'salary',
    ])
    # print(stuform)
    return render(request,'poll/home.html',{'form':stuform})