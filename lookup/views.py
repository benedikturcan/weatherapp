from django.shortcuts import render

# Create your views here. This is a note


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about')
