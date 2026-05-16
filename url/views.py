from django.shortcuts import render
from .models import Url

def index(request):
    if request.method == 'POST':
        links = request.POST['link']
    else:
        return render(request,'index.html')