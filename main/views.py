from django.shortcuts import render
from.models import Main





def home(request):
    
    return render(request,'front/home.html')


def blog(request):
    
    return render(request,'front/blog.html')




def credit(request):
   
    
    return render(request)