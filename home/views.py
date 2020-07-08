from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, _get_queryset
from .models import Information

def index(request):
    message = get_object_or_404(Information, pk = 1)
    return HttpResponse(message)

def home(response):
    ls = _get_queryset(Information)
    return render(response, "home/base.html", {})