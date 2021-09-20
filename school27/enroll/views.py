from django.shortcuts import render

# Create your views here.
def home(request):
    print("hello everyone")
    return render(request, 'home.html')