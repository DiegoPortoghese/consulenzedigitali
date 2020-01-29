from django.shortcuts import get_object_or_404 , Http404, render

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def chisono(request):
    return render(request, "chisono.html")

def servizi(request):
    return render(request, "servizi.html")

def contatto(request):
    return render(request, "contatto.html")
