from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.webpage1, name='calendar')

]