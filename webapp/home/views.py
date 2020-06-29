from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Information

def index(request):
    message = get_object_or_404(Information, pk = 1)
    return HttpResponse(message)