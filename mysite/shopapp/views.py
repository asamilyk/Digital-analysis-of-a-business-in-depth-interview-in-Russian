from django.http import HttpResponse
from django.shortcuts import render

def upload_file(request):
    if request.method == 'POST':
        if 'file_upload' not in request.FILES:
            return render(request, 'shopapp/first_page.html')
        uploaded_file = request.FILES['file_upload']
        # Здесь вы можете выполнить дополнительные действия с загруженным файлом, например, сохранить его на сервере
        return render(request, 'shopapp/result_page.html', {'uploaded_file': uploaded_file})
    return render(request, 'shopapp/first_page.html')

