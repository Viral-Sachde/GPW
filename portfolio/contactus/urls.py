
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('savey/', views.savey,name='savey'),
    path('home' ,views.HomePage,name= 'pacha')
]