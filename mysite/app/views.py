from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'app/index.html')

def result(request):
    return render(request, 'app/result.html')

