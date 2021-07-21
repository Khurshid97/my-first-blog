from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    new = ""
    n = request.GET.get('n')

    if n is not None:
        for q in n:
            if 'A' == q:
                new += 'А'
    return render(request, 'blog/home.html', {'new':new})


def about(request):
    return render(request, "blog/about.html")

def contacts(request):
    return render(request, "blog/contacts.html")

def news(request):
    return render(request, "blog/news.html")

def homepage(request):
    photos = Photo.objects.all()
    context = {
        'photos':photos,
    }

    return render(request, "blog/homepage.html", context)
def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, "blog/view.html", {'photo':photo})

