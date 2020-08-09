from django.shortcuts import render
from .models import ImageData,VideoData, farmhouse_detail
# Create your views here.
def index(request):
    image = ImageData.objects.all()
    return render(request,'index.html',{'image' : image})
def gellery(request):
    image = ImageData.objects.all()

    return render(request,'gellery.html',{'image' : image})
def videosgellery(request):
    video = VideoData.objects.all()
    if request.method == 'POST' :
        cover_image = request.POST['filename']
        video1 = VideoData.objects.filter(cover_image=cover_image)
        print('video files')
        #data = candidate_detail.objects.filter(partyname = 'BJP')
        return render(request,'gellery.html',{'video1' : video1})
    else:
        return render(request,'gellery.html',{'video' : video})

def about(request):
    return render(request,'about.html')
def contect(request):
    return render(request,'contect.html')
def services_d(request):
    service = farmhouse_detail.objects.all()

    return render(request,'services.html',{'service':service})
def details_page(request):
    service = farmhouse_detail.objects.all()

    return render(request,'details.html')
