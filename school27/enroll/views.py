from django.shortcuts import render

# Create your views here.
def home(request):
    print("hello everyone college digital")
    return render(request, 'home.html')