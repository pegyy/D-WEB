
from urllib.request import Request
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def login(requset):
    
    if requset.method == 'POST':
    
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        
        if username !="" or password !="":
            user = authenticate(username=username,password=password)
            if user != None:
                login(requset,user)
            return redirect('panel')
           # else:
           #     mgs="user not found!"
          #      return render(requset , 'front/mgs.html' , {'mgs':mgs})
       # else:
       #     mgs="all item is required"
        #    return render(requset,'front/mgs.html',{'mgs':mgs})
        
    return render(requset , 'front/login.html')    


def register(requset):
    
    if requset.method == 'POST':
        
        name = requset.POST.get('name')
        username = requset.POST.get('username')
        phone = requset.POST.get('phone')
        address = requset.POST.get('address')
        password = requset.POST.get('password')
        password2 = requset.POST.get('password2')
        
        if password != password2:
            mgs = "پسورد ها مشابه نیست"
            return render(requset, 'front/mgs.html' , {'mgs':mgs})
        
        #user = User.objects.create_user(username=username,upass=password)
        b=User(name=name, username=username ,upass=password ,phone=phone,address=address) 
        b.save()
        return redirect('panel')
        
        
    return render(requset,'front/register.html')


def panel(request):
    
    
    return render( request , 'back/panel.html')