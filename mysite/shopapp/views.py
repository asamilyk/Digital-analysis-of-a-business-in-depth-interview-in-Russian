from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        with open('path/to/save/' + uploaded_file.name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return HttpResponse('Файл успешно загружен.')
    return render(request, 'shopapp/index.html')