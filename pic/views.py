import json
from django.shortcuts import render , redirect, resolve_url
from.models import Pic
from django.core.files.storage import FileSystemStorage
from selenium import webdriver
from selenium import*
import time
import random
import requests
from bs4 import *
import os
import bs4
import urllib
from selenium.webdriver.common.by import By
from icrawler.examples import GoogleImageCrawler
from google_images_download import google_images_download
import io
from PIL import Image




def pic(request):
    
    if request.method == 'POST':
        
        # keyword for search
        keyword =  request.POST.get('keyword')
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        # Create url variable containing the webpage for a Google image search.
        
        url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")
        # Launch the browser and open the given url in the webdriver.
        driver.get(url.format(s=keyword))
        # Scroll down the body of the web page and load the images.
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
        # Find images.
        imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
        # Access and store the scr list of image url's.
        src = []
        for img in imgResults :
            src.append(img.get_attribute('src'))
            #break
        # Retrieve and download the images.
        for i in range(10):    
            urllib.request.urlretrieve(str(src[i]),"pic/img/pic{}.jpg".format(i))

    return render(request , 'back/pic.html')













            #myfile = request.FILES['myfile']
            #fs = FileSystemStorage()
            #filename = fs.save(myfile.name, myfile)
            #url=fs.url(filename) 
            
    #b=Pic(picurl=url , pic=filename)
    #b.save()
    #pic=Pic.objects.all()
    #, {'pic':pic}