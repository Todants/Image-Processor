from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process/', views.process_image, name='process_image'),
    path('test/', views.send_test_requests, name='send_test_requests'),
]
