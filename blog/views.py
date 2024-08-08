from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def homepage(request):
    if request is None:
        raise ValueError("Request object is None")
    return render(request, 'index.html') 

def posts(request):
    pass

def post_detail(request):
    pass



