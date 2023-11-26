from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def home(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')