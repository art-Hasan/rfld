from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, Django!</h1><br/><a href="/rango/end">Bye</a>')

def say_bye(request):
    return HttpResponse('<p>Bye bye!</p><br/><a href="/rango/">Main Page</a>')
