from django.urls import path
from . import views

urlpatterns = [
    path('company-info/', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
]
