from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        if 'file_upload' not in request.FILES:
            return render(request, 'app/index.html')
        uploaded_file = request.FILES['file_upload']
        # Здесь вы можете выполнить дополнительные действия с загруженным файлом, например, сохранить его на сервере
        return render(request, 'app/result.html', {'uploaded_file': uploaded_file})
    return render(request, 'app/index.html')

def result(request):
    return render(request, 'app/result.html')

