from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('adminapi/<str:email>/', views.Admin_api.as_view()),
    path('adminapi', views.Admin_api.as_view()),
    path('studetapi/<str:email>/', views.Student_api.as_view()),
    path('studetapi', views.Student_api.as_view()),
]
