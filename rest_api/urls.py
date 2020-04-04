from django.urls import path
from rest_api import views


urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
]
