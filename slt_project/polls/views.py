from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())