from django.shortcuts import render

# Create your views here.

def home(request) :
    str = '大艺数'
    return render(request, 'blog/home.html', {'home': str})