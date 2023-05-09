from django.shortcuts import render
from django.http import HttpResponse
from .models import carousalImages

# Create your views here.
def index(request):
    obj = carousalImages.objects.all()
    num = len(obj)
    params = {"crImg":obj,"range":range(1,num)}
    return render(request,'index.html',params)
