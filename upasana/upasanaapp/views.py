from django.shortcuts import render
from .models import ImageData,VideoData
# Create your views here.
def index(request):
    image = ImageData.objects.all()
    return render(request,'index.html',{'image' : image})
def gellery(request):
    image = ImageData.objects.all()

    return render(request,'gellery.html',{'image' : image})
def videosgellery(request):
    video = VideoData.objects.all()
    return render(request,'gellery.html',{'video' : video})

def about(request):
    return render(request,'about.html')
def contect(request):
    return render(request,'contect.html')
