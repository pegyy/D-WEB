from urllib.request import Request
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from.models import Management
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def adlogin(request):
    
    if request.method == 'POST':
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username !="" or password !="":
            user = authenticate(username=username,password=password)
            if user != None:
                login(request,user)
            return redirect('managerpanel')
    
    return render(request , 'back/management/adlogin.html')





def management(request):
    
    
    return render(Request , 'back/management/managerpanel.html')