from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.
# def home(request,id,check,errors):
#     print(id)
#     print(check)
#     print(errors)
#     val=id
#     err=errors
#     print(val)
def home(request):
    if request.method=="POST":
        print("Post request")
        form=StudentForm(request.POST)
        if form.is_valid():
            # nm=form.cleaned_data['name']
            # rl=form.cleaned_data['roll']
            # ad=form.cleaned_data['address']
            # stu=Student(name=nm,roll=rl,address=ad)  #Update
            # stu=Student(id=1)   #Delete
            form.save()        #Update
            # stu.delete()        #Delete
            # messages.add_message(request, messages.SUCCESS, 'Your data has been saved!!!')
            messages.success(request, "Your data has been saved!!!")
            # form=StudentForm()
    else:
        form=StudentForm()
        # return render(request, "enroll/home.html",{'form':form,'id':val,'err':err})
    return render(request, "enroll/home.html",{'form':form})