from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('download/', views.download, name='download'),
    path('methods/', views.methods, name='methods'),
    path('contact/', views.contact, name='contact'),
    path('<path:unknown_path>/', views.unknown_view, name='unknown_view'),
]