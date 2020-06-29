from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')), # This sets the path to the home screen to the home url 
    path('admin/', admin.site.urls),
]
