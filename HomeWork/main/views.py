from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("<p><a href='/'>Main Page</a>&nbsp;&nbsp;&nbsp;<a href='/data'>Data Page</a>&nbsp;&nbsp;&nbsp;<a href='/test'>Test Page</a></p><h1>Main Page</h1>")

def data(request):
  return HttpResponse("<p><a href='/'>Main Page</a>&nbsp;&nbsp;&nbsp;<a href='/data'>Data Page</a>&nbsp;&nbsp;&nbsp;<a href='/test'>Test Page</a></p><h1>Date Page</h1>")

def test(request):
  return HttpResponse("<p><a href='/'>Main Page</a>&nbsp;&nbsp;&nbsp;<a href='/data'>Data Page</a>&nbsp;&nbsp;&nbsp;<a href='/test'>Test Page</a></p><h1>Test Page</h1>")