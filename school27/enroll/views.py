from django.shortcuts import render

# Create your views here.
def home(request):
    print("hello")
    return render(request, 'home.html')