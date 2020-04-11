from django.urls import path
from .import views

app_name = 'upload'
urlpatterns = [
    path('', views.home, name='home'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('model_form_upload/', views.model_form_upload, name='model_form_upload'),
]