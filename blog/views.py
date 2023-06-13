from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
request = HttpRequest
response = HttpResponse

def index(request):
    return HttpResponse("Main page")

def test_page(request):
    return HttpResponse("Test", status=404)
# Create your views here.
