from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("<h1>Main Page</h1>")

def new(request):
  return HttpResponse("<h1>NEW Page. NEW. NEW</h1>")
