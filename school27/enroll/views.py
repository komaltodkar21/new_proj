from django.shortcuts import render

# Create your views here.
def home(request):
    print("hello everyone college")
    return render(request, 'home.html')