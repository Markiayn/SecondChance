from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<html><title>Markiyan</title><h1>Markiyan</h1></html>')
