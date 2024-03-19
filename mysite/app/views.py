import os
import chardet

from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render, redirect
import sys
from app.analysis import main

from mysite import settings


def index(request):
    if request.method == 'POST':
        if 'file_upload' not in request.FILES:
            return render(request, 'app/index.html')
        try:
            uploaded_file = request.FILES['file_upload'].read()
            detected_encoding = chardet.detect(uploaded_file)['encoding']
            uploaded_file = uploaded_file.decode(detected_encoding)
        except Exception as e:
            error_message = "Произошла ошибка при чтении файла. Пожалуйста, убедитесь, что файл в поддерживаемом формате."
            print("Error:", e)
            return render(request, 'app/index.html', {'error_message': error_message})
        main.analyse(uploaded_file)
        return render(request, 'app/result.html')
    return render(request, 'app/index.html')


def result(request):
    return render(request, 'app/result.html')


def contact(request):
    return render(request, 'app/contact.html')


def methods(request):
    return render(request, 'app/methods.html')


def download(request):
    pdf_file_path = os.path.join(settings.BASE_DIR, 'canvas.pdf')

    with open(pdf_file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="results.pdf"'
        return response


def unknown_view(request, unknown_path):
    return HttpResponseNotFound("Страница не найдена")