from django.shortcuts import render
from.models import Dm
import requests
from bs4 import BeautifulSoup

# Create your views here.


def dgk(request):
    
    if request.method == 'POST':
        
        url = request.POST.get('url')
        titeles =[]
        stars = []
        prices =[]
        
        for page in range(1,4):
            page = request.get()
        
    
    return render(request,'back/dgk.html')