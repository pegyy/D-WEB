from django.shortcuts import render
from.models import Twt
import twitter
# Create your views here.


def twt(request):
    
    keyword = request.get('keyword')
    
    
    
    
    
    return render(request , 'back/twt.html')