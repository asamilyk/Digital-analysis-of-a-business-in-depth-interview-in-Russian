from django.http import HttpResponse
from django.shortcuts import render, redirect
import sys
from app.analysis import main


def index(request):
    #if request.method == 'POST':
        #if 'file_upload' not in request.FILES:
           # return render(request, 'app/index.html')
        #uploaded_file = request.FILES['file_upload']
        #file = uploaded_file.readAsText
        #result_file = main.analyse(file)
        #return render(request, 'app/result.html', {'uploaded_file': uploaded_file})
    return render(request, 'app/index.html')

def result(request):
    return render(request, 'app/result.html')

