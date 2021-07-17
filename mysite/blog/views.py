from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {})


def about(request):
    return render(request, "blog/about.html")

def contacts(request):
    return render(request, "blog/contacts.html")


def homepage(request):
    return render(request, "blog/homepage.html")

def news(request):
    return render(request, "blog/news.html")