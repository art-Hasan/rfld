from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I'm a bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse('<p>About Page.</p><br/><a href="/rango/">Main Page</a>')
