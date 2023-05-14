from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse('<html><h1>Markiyan</h1><title>Markiyan</title></html>')
