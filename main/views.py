from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def start(request: HttpRequest):
    return render(request, 'main/main_template')